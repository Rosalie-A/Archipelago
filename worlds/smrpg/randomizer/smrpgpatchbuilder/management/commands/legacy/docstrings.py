import ast
import sys
import re

from pathlib import Path

def format_opcode(opcode: int | list[int] | None) -> str:
    if opcode is None:
        return "*No `_opcode` found*"
    if isinstance(opcode, list):
        return "`" + " ".join(f"0x{b:02X}" for b in opcode) + "`"
    return f"`0x{opcode:02X}`"
    return "*Invalid `_opcode` format*"

def format_size(size: int | None) -> str:
    return (
        f"{size} byte{"s" if size != 1 else ""}"
        if size is not None
        else "*No `_size` found*"
    )

def has_existing_docstring(cls: ast.ClassDef) -> bool:
    docstring = ast.get_docstring(cls)
    if not docstring:
        return False
    required_sections = ["## Lazy Shell command", "## Opcode", "## Size", "Args:"]
    return all(section in docstring for section in required_sections)

def parse_class_attrs(cls: ast.ClassDef):
    opcode = None
    size = None
    attributes = []

    for node in cls.body:
        # Handle both annotated and non-annotated assignments
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            # Get the variable name
            if isinstance(node, ast.AnnAssign):
                target = node.target
                value = node.value
            else:  # ast.Assign
                if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
                    continue
                target = node.targets[0]
                value = node.value

            if not isinstance(target, ast.Name):
                continue

            name = target.id
            attributes.append(name)

            if name == "_opcode":
                if isinstance(value, ast.Constant) and isinstance(value.value, int):
                    opcode = value.value
                elif (
                    isinstance(value, ast.Call)
                    and getattr(value.func, "id", "") == "bytearray"
                    and value.args
                    and isinstance(value.args[0], ast.List)
                ):
                    elements = value.args[0].elts
                    if all(
                        isinstance(e, ast.Constant) and isinstance(e.value, int)
                        for e in elements
                    ):
                        opcode = [e.value for e in elements]

            elif name == "_size":
                if isinstance(value, ast.Constant) and isinstance(value.value, int):
                    size = value.value

    # Infer size if missing and class inherits from CommandNoArgs
    if size is None and any(
        isinstance(base, ast.Name) and "CommandNoArgs" in base.id for base in cls.bases
    ):
        if isinstance(opcode, int):
            size = 1
        elif isinstance(opcode, list):
            size = len(opcode)

    return opcode, size, attributes

def parse_constructor_args(cls: ast.ClassDef):
    args_with_types = {}
    class_annotations = {}

    # Collect class-level annotated attributes
    for node in cls.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            if isinstance(node.annotation, ast.Name):
                class_annotations[name] = node.annotation.id
            elif isinstance(node.annotation, ast.Subscript):
                class_annotations[name] = ast.unparse(node.annotation)

    # Find __init__ method
    for node in cls.body:
        if isinstance(node, ast.FunctionDef) and node.name == "__init__":
            for arg in node.args.args[1:]:  # skip self
                arg_name = arg.arg
                if arg.annotation:
                    args_with_types[arg_name] = ast.unparse(arg.annotation)
                elif arg_name in class_annotations:
                    args_with_types[arg_name] = class_annotations[arg_name]
                else:
                    args_with_types[arg_name] = "type"
            return args_with_types

    # No __init__, fall back to class-level annotations
    return {
        name: type_
        for name, type_ in class_annotations.items()
        if not name.startswith("_")
    }

def extract_property_docs(cls: ast.ClassDef):
    docs = {}
    for node in cls.body:
        if isinstance(node, ast.FunctionDef):
            for deco in node.decorator_list:
                if isinstance(deco, ast.Name) and deco.id == "property":
                    name = node.name
                    docstring = ast.get_docstring(node)
                    if docstring:
                        docs[name] = docstring.strip().split("\n")[0]  # first line
    return docs

def inherits_from_command_with_jmps(cls: ast.ClassDef) -> bool:
    return any(
        "CommandWithJmps" in getattr(base, "id", "")
        for base in cls.bases
        if isinstance(base, ast.Name)
    )

def generate_docstring(cls: ast.ClassDef):
    if has_existing_docstring(cls):
        return ""

    class_name = cls.name
    opcode, size, attributes = parse_class_attrs(cls)
    args = parse_constructor_args(cls)
    prop_docs = extract_property_docs(cls)

    original_doc = ast.get_docstring(cls) or ""
    normalized_doc = re.sub(
        r"(?<!\n)\n(?![\n\s])", " ", original_doc
    )  # Single newline -> space
    normalized_doc = re.sub(
        r"\n[\n\s]*", "  \n    ", normalized_doc.strip()
    )  # Multiple newlines -> soft break

    docstring_lines = [
        f'    """{normalized_doc}  \n',
        "    ## Lazy Shell command",
        "        `TBD, to be filled in manually by me`  \n",
        "    ## Opcode",
        f"        {format_opcode(opcode)}\n",
        "    ## Size",
        f"        {format_size(size)}\n",
    ]

    docstring_lines.append("    Args:")

    if args:
        for arg, type_ in args.items():
            if arg == "identifier" or (
                arg == "destinations" and inherits_from_command_with_jmps(cls)
            ):
                continue
            description = prop_docs.get(arg, "Description here to be filled out by me")
            docstring_lines.append(f"        {arg} ({type_}): {description}")

    if inherits_from_command_with_jmps(cls):
        docstring_lines.append(
            "        destinations (list[str]): This should be a list of exactly one `str`. "
            "The `str` should be the label of the command to jump to."
        )

    docstring_lines.append(
        "        identifier (str | None): Give this command a label if you want another command to jump to it."
    )
    docstring_lines.append('    """')

    return f"\nClass: {class_name}\n" + "\n".join(docstring_lines) + "\n"

def process_file(filepath: Path):
    with filepath.open("r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=str(filepath))

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            doc = generate_docstring(node)
            if doc:
                print(doc)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_docstrings.py <path_to_file.py>")
        sys.exit(1)

    process_file(Path(sys.argv[1]))
