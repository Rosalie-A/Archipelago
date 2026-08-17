import os.path
import pkgutil
import sys
import tempfile

rando_zip = pkgutil.get_data(__name__, "randomizer.zip")
patcher_zip = pkgutil.get_data(__name__, "smrpgpatchbuilder.zip")
markdown_zip = pkgutil.get_data(__name__, "markdown.zip")

td = tempfile.TemporaryDirectory()

with open(os.path.join(td.name, "rando.zip"), "wb") as file:
    file.write(rando_zip)

with open(os.path.join(td.name, "patcher.zip"), "wb") as file:
    file.write(patcher_zip)

with open(os.path.join(td.name, "markdown.zip"), "wb") as file:
    file.write(markdown_zip)

sys.path.append(td.name + "\\rando.zip")
sys.path.append(td.name + "\\patcher.zip")
sys.path.append(td.name + "\\markdown.zip")
