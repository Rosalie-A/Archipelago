from markdown import markdown
from enum import StrEnum, Enum
from typing import Generic, TypeVar, TYPE_CHECKING, Any
from ..data.spells.spells import ALL_SPELLS
from ..types.spell import CharacterSpell
from ..data.allies.allies import ally_collection
from .base import CategorizationOption, ClassCategorizationOption
from copy import deepcopy
import random

if TYPE_CHECKING:
    ShuffledBossEnumType = Enum
else:
    ShuffledBossEnumType = Any


class FlagError(ValueError):
    pass


class FlagType(StrEnum):
    BOOLEAN = "boolean"
    CATEGORIZATION = "categorization"
    CATEGORIZATION_WITH_ORDINANCE = "categorization_with_ordinance"
    RANGE = "number"  # Frontend expects "number" not "range"
    SELECT_ONE = "select_one"


class Flag:
    """Class representing a flag with its description, and possible values/choices/options."""

    _name = ""
    _description = ""
    _default = None
    _id = ""
    _requires_all = []
    _requires_any = []
    _disabled_if_all = []  # Disable this flag if ALL of these conditions are met
    type: FlagType
    modes = ["open"]

    @property
    def description(self):
        return markdown(self._description)

    @property
    def description_or_name(self):
        if self._description:
            return self.description
        else:
            return markdown(self._name)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id


# TypeVars for generic flag classes
from enum import Enum

T = TypeVar("T", bound=Enum)


class CategorizationFlag(Flag, Generic[T]):
    """For things like selecting which locations can and cannot contain progression"""

    type = FlagType.CATEGORIZATION
    _options: dict[T, bool] = {}
    _default: dict[T, bool] = {}

    @property
    def enabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if enabled]

    @property
    def disabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if not enabled]

    def enable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        self.options[option] = True

    def disable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        self.options[option] = False

    @property
    def default(self) -> dict[T, bool]:
        return self._default

    @property
    def options(self) -> dict[T, bool]:
        return self._options or self.default.copy()

    @staticmethod
    def _get_option_text(value: Any) -> str:  # noqa: C901
        """Get a JSON-serializable text representation of an enum value.

        Priority order for descriptive names:
        1. _text (boss fights)
        2. _name (battle music classes)
        3. _title (spells)
        4. Tuple with string second element (e.g., MusicTrack)
        5. _id.value (prize locations with ShuffleLocationSelector enum)
        6. value (if string, for simple enums)
        7. name attribute (allies)
        8. __name__ (class types)
        9. str() fallback
        """
        if isinstance(value, str):
            return value
        # Tuple values where second element is the display name (e.g., MusicTrack)
        if isinstance(value, tuple):
            if len(value) >= 2 and isinstance(value[1], str):
                return value[1]
            return str(value)
        # Boss fights have _text
        if hasattr(value, "_text"):
            return value._text  # type: ignore[union-attr]
        # Battle music classes have _name
        if hasattr(value, "_name") and isinstance(value._name, str):  # type: ignore[union-attr]
            return value._name  # type: ignore[union-attr]
        # Spells have _title
        if hasattr(value, "_title"):
            return value._title  # type: ignore[union-attr]
        # Prize locations have _id which is a ShuffleLocationSelector enum
        if hasattr(value, "_id"):
            id_val = value._id  # type: ignore[union-attr]
            if hasattr(id_val, "value") and isinstance(id_val.value, str):
                return id_val.value
        # Simple enum with string value
        if hasattr(value, "value") and isinstance(value.value, str):  # type: ignore[union-attr]
            return value.value  # type: ignore[union-attr]
        # Allies have name attribute
        if hasattr(value, "name") and isinstance(value.name, str):  # type: ignore[union-attr]
            return value.name  # type: ignore[union-attr]
        # Class types have __name__
        if hasattr(value, "__name__"):
            return value.__name__  # type: ignore[union-attr]
        return str(value)

    @property
    def options_dict(self) -> list[dict[str, str]]:
        """All options as a dict for JSON serialization, sorted alphabetically by text."""
        options = [
            {"id": c.name, "text": self._get_option_text(c.value)}
            for c in self.options.keys()
        ]
        return sorted(options, key=lambda x: x["text"].lower())

    @property
    def default_dict(self) -> list[dict[str, str]]:
        """Enabled options as a dict for JSON serialization, sorted alphabetically by text."""
        options = [
            {"id": c.name, "text": self._get_option_text(c.value)} for c in self.enabled
        ]
        return sorted(options, key=lambda x: x["text"].lower())

    def reset(self) -> None:
        self._options = self.default.copy()

    def __init__(self, options: dict[T, bool] | None = None) -> None:
        if options is not None:
            for option, enabled in options.items():
                if enabled:
                    self.enable(option)
                else:
                    self.disable(option)
        else:
            self._options = self.default.copy()


class CategorizationFlagWithOrdinance(Flag, Generic[T]):
    """For thing like choosing your starting party where order matters"""

    type = FlagType.CATEGORIZATION_WITH_ORDINANCE
    _options: dict[T, int | None] = {}
    _default: dict[T, int | None] = {}

    @property
    def default(self) -> dict[T, int | None]:
        return self._default

    @property
    def options(self) -> dict[T, int | None]:
        return self._options or self.default.copy()

    @staticmethod
    def _get_option_text(value: Any) -> str:  # noqa: C901
        """Get a JSON-serializable text representation of an enum value.

        Priority order for descriptive names:
        1. _text (boss fights)
        2. _name (battle music classes)
        3. _title (spells)
        4. Tuple with string second element (e.g., MusicTrack)
        5. _id.value (prize locations with ShuffleLocationSelector enum)
        6. value (if string, for simple enums)
        7. name attribute (allies)
        8. __name__ (class types)
        9. str() fallback
        """
        if isinstance(value, str):
            return value
        # Tuple values where second element is the display name (e.g., MusicTrack)
        if isinstance(value, tuple):
            if len(value) >= 2 and isinstance(value[1], str):
                return value[1]
            return str(value)
        # Boss fights have _text
        if hasattr(value, "_text"):
            return value._text  # type: ignore[union-attr]
        # Battle music classes have _name
        if hasattr(value, "_name") and isinstance(value._name, str):  # type: ignore[union-attr]
            return value._name  # type: ignore[union-attr]
        # Spells have _title
        if hasattr(value, "_title"):
            return value._title  # type: ignore[union-attr]
        # Prize locations have _id which is a ShuffleLocationSelector enum
        if hasattr(value, "_id"):
            id_val = value._id  # type: ignore[union-attr]
            if hasattr(id_val, "value") and isinstance(id_val.value, str):
                return id_val.value
        # Simple enum with string value
        if hasattr(value, "value") and isinstance(value.value, str):  # type: ignore[union-attr]
            return value.value  # type: ignore[union-attr]
        # Allies have name attribute
        if hasattr(value, "name") and isinstance(value.name, str):  # type: ignore[union-attr]
            return value.name  # type: ignore[union-attr]
        # Class types have __name__
        if hasattr(value, "__name__"):
            return value.__name__  # type: ignore[union-attr]
        return str(value)

    @property
    def options_dict(self) -> list[dict[str, str | int | None]]:
        """All options as a dict for JSON serialization, sorted alphabetically by text."""
        options = [
            {
                "id": c.name,
                "text": self._get_option_text(c.value),
                "order": self.options.get(c),
            }
            for c in self.options.keys()
        ]
        return sorted(options, key=lambda x: str(x["text"]).lower())

    @property
    def default_dict(self) -> list[dict[str, str | int | None]]:
        """Default options as a dict for JSON serialization, sorted alphabetically by text."""
        options = [
            {
                "id": c.name,
                "text": self._get_option_text(c.value),
                "order": self.default.get(c),
            }
            for c in self.default.keys()
        ]
        return sorted(options, key=lambda x: str(x["text"]).lower())

    @property
    def enabled(self) -> list[T]:
        return sorted(
            [option for option, enabled in self.options.items() if enabled is not None],
            key=lambda x: (
                self.options[x] is None,
                self.options[x] if self.options[x] is not None else 0,
            ),
        )

    @property
    def disabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if enabled is None]

    def enable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        max_value = max((v for v in self.options.values() if v is not None), default=-1)
        self.options[option] = max_value + 1

    def disable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        previous_value = self.options[option]
        self.options[option] = None
        if previous_value is not None:
            for opt, val in self.options.items():
                if val is not None and val > previous_value:
                    self.options[opt] = val - 1

    def reset(self) -> None:
        self._options = self.default.copy()

    def __init__(self, options: dict[T, int | None] | None = None) -> None:
        self._options = self.default.copy()
        if options is not None:
            for k in options.keys():
                assert k in self._options
            self._options = deepcopy(options)


class SelectOneFlag(Flag, Generic[T]):
    """For things like choosing an area gating option can and cannot contain progression"""

    type = FlagType.SELECT_ONE
    choices: list[T] = []
    _selected: T
    _default: T

    @property
    def selected(self) -> T:
        return self._selected or self._default

    def select(self, choice: T) -> None:
        if choice not in self.choices:
            raise FlagError(f"Choice {choice} is not a valid option for this flag.")
        self._selected = choice

    @property
    def default(self) -> T:
        return self._default

    @property
    def choices_dict(self) -> list[dict[str, str]]:
        """All choices as a dict for JSON serialization."""
        return [{"id": c.name, "text": c.value} for c in self.choices]

    @property
    def default_dict(self) -> dict[str, str]:
        """Selected option as a dict for JSON serialization."""
        return {"text": self.default.value, "id": self.default.name}

    def reset(self) -> None:
        self._selected = self.default

    def __init__(self, choice: T | None = None) -> None:
        if choice is not None:
            self.select(choice)
        else:
            self.select(self.default)


class BooleanFlag(Flag):
    """For simple true/false flags"""

    type = FlagType.BOOLEAN
    enabled: bool = False
    _default: bool = False

    @property
    def default(self) -> bool:
        return self._default

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def reset(self):
        self.enabled = self.default

    def __init__(self, enabled: bool | None = None) -> None:
        if enabled is not None:
            self.enabled = enabled
        else:
            self.enabled = self.default


class RangeFlag(Flag):
    """For flags that have a range of integer values"""

    type = FlagType.RANGE
    min_value: int = 0
    max_value: int = 100
    _value: int = 0
    _default: int = 0

    @property
    def default(self) -> int:
        return self._default

    @property
    def value(self) -> int:
        return self._value or self.default

    def set_value(self, value: int):
        if value < self.min_value or value > self.max_value:
            raise FlagError(f"Value {value} is out of range for this flag.")
        self._value = value

    def reset(self):
        self._value = self.default

    def __init__(self, threshold: int | None = None) -> None:
        if threshold is not None:
            self.set_value(threshold)
        else:
            self.set_value(self.default)


# ✅ = implemented


# ******** Party


# ✅
class ShuffleCharacters(BooleanFlag):
    _name = "Randomize party recruitment order"
    _description = """If enabled, the order in which each ally joins your party will change.
<br>
<br>If disabled, you will start with Mario and recruit characters near their original locations."""
    _id = "rchars"


# ✅
class MaxCharacters(RangeFlag):
    _name = "Total playable allies"
    _description = "The number of allies that can appear in the seed (including starting characters). Set this to 1 if you are attempting a solo challenge."
    min_value = 1
    max_value = 5
    _default = 5
    _id = "max"
    _requires_all = [(ShuffleCharacters(), True)]


# ✅
# Build StartingCharacterEnum dynamically - use ally instances as values (not class, to avoid aliases)
_inclusion_members = {}
for ally in ally_collection._allies:
    attr_name = ally.name.replace(" ", "_").replace("-", "_")
    _inclusion_members[attr_name] = ally
IncludedCharacterEnum = ClassCategorizationOption(
    "IncludedCharacterEnum", _inclusion_members
)


class AvailableCharacters(CategorizationFlag[IncludedCharacterEnum]):
    _name = "Available Allies"
    _description = """Highlighted (white text over blue) allies are eligible to be one of your "Total playable allies". Un-highlight any characters you wish to exclude from the game entirely."""
    _default = {o: True for o in IncludedCharacterEnum.__members__.values()}
    _id = "avail_chars"


# ✅
# Build StartingCharacterEnum dynamically - use ally instances as values (not class, to avoid aliases)
_starting_char_members = {}
for ally in ally_collection._allies:
    attr_name = ally.name.replace(" ", "_").replace("-", "_")
    _starting_char_members[attr_name] = ally
# Add 5 "Random" options - these are special markers, not actual allies
# The Settings object will interpret these as "pick a random ally"
for i in range(1, 6):
    _starting_char_members[f"Random_{i}"] = f"Random_{i}"
StartingCharacterEnum = ClassCategorizationOption(
    "StartingCharacterEnum", _starting_char_members
)


class StartingCharacters(CategorizationFlagWithOrdinance[StartingCharacterEnum]):
    _name = "Starting Characters"
    _default: dict[StartingCharacterEnum, int | None] = {
        o: (0 if i == 0 else None)
        for i, o in enumerate(StartingCharacterEnum.__members__.values())
    }
    _description = "The allies who will be in your party at the start of the game. Your first pick is your <b>starter ally.</b>"
    _id = "starters"
    _requires_all = [(ShuffleCharacters(), True)]

    def resolve_random_selections(self, rng: "random.Random | None" = None) -> list:
        """Resolve enabled selections, replacing Random_X with actual allies.

        Args:
            rng: Optional random.Random instance for reproducible randomization.
                 If None, uses the global random module (which should be seeded).

        Returns a list of Ally instances in the order they should be assigned.
        """
        from ..data.allies.allies import ally_collection

        # Get all available allies
        available_allies = list(ally_collection._allies)

        # Track which allies have already been selected
        used_allies: list = []
        result: list = []

        for option in self.enabled:
            value = option.value
            # Check if this is a "Random_X" string value
            if isinstance(value, str) and value.startswith("Random_"):
                # Pick a random ally from those not yet used
                remaining = [a for a in available_allies if a not in used_allies]
                if remaining:
                    chosen = rng.choice(remaining) if rng else random.choice(remaining)
                    used_allies.append(chosen)
                    result.append(chosen)
            else:
                # This is an actual ally instance
                used_allies.append(value)
                result.append(value)

        return result


class PlayAsStarter(BooleanFlag):
    _name = "Play as starter ally everywhere"
    _description = """If enabled, your starter ally will also be the protagonist outside of battle.
<br>
<br>If disabled, you will always play as Mario outside of battle, regardless of whether or not he is in your party."""
    _id = "protag"
    _requires_all = [(ShuffleCharacters(), True)]


# ******** Equipment


# ✅
class EquipmentCharactersOptions(CategorizationOption):
    """Enumeration for character equipment guidelines"""

    VANILLA = "Default"
    VANILLA_ACCESSORIES_ALL = "Default, except anyone can wear any accessory"
    RANDOM_ACCESSORIES_ALL = "Random, except anyone can wear any accessory"
    RANDOM = "Completely random"
    EQUIP_ALL = "Anyone can equip anything"


# ✅
class EquipmentCharacters(SelectOneFlag[EquipmentCharactersOptions]):
    _name = "Equipment permissions"
    _description = """<b>Default</b>: The list of allies who are permitted to equip each item remains unchanged from the original game.
<br>
<br><b>Default, except anyone can wear any accessory</b>: Armor and weapon permissions are unchanged from the original game, but all accessories can be equipped by anyone.
<br>
<br><b>Random, except anyone can wear any accessory</b>: Armor and weapon permissions are randomized, but all accessories can be equipped by anyone.
<br>
<br><b>Completely random</b>: All equips' permissions are randomized.
<br>
<br><b>Anyone can equip anything</b>: No equips are restricted by ally at all."""
    choices = [o for o in EquipmentCharactersOptions]
    _default = EquipmentCharactersOptions.VANILLA
    _id = "perms"


# ✅
class EquipmentPropertiesOptions(CategorizationOption):
    VANILLA = "Default"
    SOME = "Some buffs added"
    RANDOM = "Completely random"


# ✅
class EquipmentProperties(SelectOneFlag[EquipmentPropertiesOptions]):
    _name = "Equipment stats & buffs"
    _description = """<b>Default</b>: The stats and buffs on equipment are unchanged from the original game.
<br>
<br><b>Some buffs added</b>: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks). Additionally, some weapons will boost magic attack instead of physical attack.
<br>
<br><b>Completely random</b>: The stats and buffs on each piece of equipment is randomized."""
    choices = [o for o in EquipmentPropertiesOptions]
    _default = EquipmentPropertiesOptions.VANILLA
    _id = "props"


# ✅
class IgnoreNamesakeProperties(BooleanFlag):
    _name = "No equipment property guarantees"
    _description = "Normally, certain namesake items retain their protections: <b>Fearless Pin</b>, <b>Antidote Pin</b>, <b>Trueform Pin</b>, and <b>Wakeup Pin</b>. In addition, at least four equips will have OHKO protection. This flag removes those guarantees."
    _id = "unsafe"
    _requires_all = [(EquipmentProperties(), [EquipmentPropertiesOptions.RANDOM])]


# ✅
class StarPieceHints(BooleanFlag):
    _name = "Signal Ring Star Piece hints"
    _description = """If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.  
<br>
<br>The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a Star Piece, but rather that at least one room in the area does. (Note: Belome Temple and Land's End are considered different areas.)"""
    _id = "hints"


# ******** Stats & Spells


# ✅
class EXPMultiplierOptions(CategorizationOption):
    """Enumeration for EXP scaling from enemy battles"""

    VANILLA = "Default"
    DOUBLE = "Double"
    TRIPLE = "Triple"


# ✅
class EXPMultiplier(SelectOneFlag[EXPMultiplierOptions]):
    _name = "EXP multiplier"
    _description = (
        """If not set to "Default", all EXP gained will be doubled or tripled."""
    )
    choices = [o for o in EXPMultiplierOptions]
    _default = EXPMultiplierOptions.VANILLA
    _id = "exp"


# ✅
class CharacterStats(BooleanFlag):
    _name = "Randomize ally stats"
    _description = """If enabled, stats and stat curves for each ally will be randomized, as well as the levels at which they learn their spells. This also randomizes the max FP you start with.
<br>
<br>If disabled, allies retain their original stats and stat curves."""
    _id = "stats"


# ✅
class CharacterLearnedSpells(BooleanFlag):
    _name = "Randomize ally learned spells"
    _description = "The pool of spells that each ally can learn will be randomized. This does not include enemy spells."
    _id = "charspells"


# ✅
class CharacterSpellStats(BooleanFlag):
    _name = "Randomize ally spell stats"
    _description = "The power and FP cost of ally magic spells will be randomized."
    _id = "spellstats"


# ✅
class InfuseSpellElements(BooleanFlag):
    _name = "Infuse more spells with elements"
    _description = "Geno Beam becomes an ice spell, Geno Flash and Psych Bomb become fire spells, and Crusher and Bowser Crush become earth (jump) spells."
    _id = "infuse"


# ✅
class CharacterSpellElements(BooleanFlag):
    _name = "Randomize ally spell elements"
    _description = "Ally spells with elements will have their elements randomized. Non-elemental spells will remain non-elemental."
    _id = "spellelements"


# ✅
class UncapSuperJumps(BooleanFlag):
    _name = "Uncap Super Jumps"
    _description = "If enabled, you can do more than 100 Super Jumps per turn."
    _id = "uncap"


# ✅
# Build LearnableSpellEnum members dynamically
_learnable_spell_members = {}
for spell in ALL_SPELLS.spells:
    if isinstance(spell, CharacterSpell):
        attr_name = spell.title.replace(" ", "_").replace("-", "_")
        _learnable_spell_members[attr_name] = type(spell)
LearnableSpellEnum = ClassCategorizationOption(
    "LearnableSpellEnum", _learnable_spell_members
)


class AvailableSpells(CategorizationFlag[LearnableSpellEnum]):
    _name = "Available Ally Spells"
    _description = """Highlighted (white text over blue) spells will be learned by at least one ally. Spells that are not highlighted will not be learned by any ally.
<br>
<br>Excluded spells are not replaced in allies' learnsets by other spells, so some allies will learn less than six total.
<br>
<br>Note: You must include at least one of Geno Whirl, Star Rain, Terrorize, or Poison Gas to ensure you can transform Mokura regardless of your other settings."""
    _default = {o: True for o in LearnableSpellEnum.__members__.values()}
    _id = "avail_spells"


# ******** Star Pieces and Bosses


# ✅
class ShuffleStarPieces(BooleanFlag):
    _name = "Randomize the locations of Star Pieces"
    _description = """If enabled, the Star Pieces may be found in places other than their original locations.
<br>
<br>If disabled, they will be rewarded by defeating the final bosses of Mushroom Kingdom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill."""
    _id = "rstars"


# ✅
class TotalStarPieces(RangeFlag):
    _name = "Total Star Pieces available"
    _description = (
        "The total number of Star Pieces (0-7) that can be collected in the seed."
    )
    _default = 6
    min_value = 0
    max_value = 7
    _id = "total_sp"
    _requires_all = [(ShuffleStarPieces(), True)]


# ✅
class ProgressionLogicDifficultyOptions(CategorizationOption):
    """Enumeration for progression logic difficulty levels"""

    NORMAL = "Default"
    HARD = "Hard"


# ✅
class ProgressionLogicDifficulty(SelectOneFlag[ProgressionLogicDifficultyOptions]):
    _name = "Progression logic difficulty"
    _description = """<b>Normal</b> - Your expected early progression items are most likely to be found earlier in the game.
<br>
<br><b>Hard</b> - Your early progression items may be found in lategame areas.
<br>
<br>This setting assumes you are scaling boss fights according to their location. It is effectively useless if you don't."""
    choices = [o for o in ProgressionLogicDifficultyOptions]
    _id = "proglogic"
    _default = ProgressionLogicDifficultyOptions.NORMAL
    _requires_all = [(ShuffleStarPieces(), True)]


# ✅
class DisperseStarPieces(BooleanFlag):
    _name = "Disperse Star Pieces evenly across the map"
    _description = """If enabled, each of the seven overworld map areas (Mario's Pad - Bandit's Way, Kero Sewers - Pipe Vault + Yo'ster Isle, Moleville - Marrymore, Star Hill - Sunken Ship, Land's End - Grate Guy's Casino, Nimbus Land - Barrel Volcano, and Bowser's Keep - Factory) may only contain up to one Star Piece each."""
    _id = "disperse"
    _requires_all = [(ShuffleStarPieces(), True)]


# ******** Item shuffle


# ✅
# if this is disabled, no options in this category can be changed
class ShuffleItems(BooleanFlag):
    _name = "Randomize item rewards"
    _description = """If enabled, the contents of treasure chests, quest rewards, and freestanding small items (including Midas River cave items) will be shuffled.
<br>
<br>If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game."""
    _id = "ritems"


# ✅
class ItemQualityOptions(CategorizationOption):
    """Enumeration for item quality options"""

    ORIGINAL_POOL = "Original item pool"
    COMPLETELY_RANDOM = "Completely random items"
    MOSTLY_RANDOM = "Random items, biased toward low-impact items"
    COMPLETELY_EMPTY = "Completely empty except for progress items"


# ✅
class ItemQuality(SelectOneFlag[ItemQualityOptions]):
    _name = """Item pool quality"""
    _description = """Determines how non-required items are distributed."""
    choices = [o for o in ItemQualityOptions]
    _default = ItemQualityOptions.ORIGINAL_POOL
    _id = "itemqual"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class BiasItemShuffle(BooleanFlag):
    _name = "Bias better items to gated locations"
    _description = (
        """If enabled, gated areas will be more likely to house better items."""
    )
    _id = "biasitems"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class AnnoyingChests(BooleanFlag):
    _name = 'Empty chests should perform the "You Missed" animation'
    _description = """If disabled, empty chests will simply appear as pre-opened. Only relevant if your Item Pool Quality is set to "Completely empty." """
    _id = "ym"
    _requires_all = [(ItemQuality(), ItemQualityOptions.COMPLETELY_EMPTY)]


# ✅
class NoStarEgg(BooleanFlag):
    _name = "No Star Egg"
    _description = """If enabled, no check will grant the Star Egg."""
    _id = "noegg"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class RestrictSpecialEquips(BooleanFlag):
    _name = 'Shuffle "Special Item" exchange equips & Monstro Town reward equips'
    _description = """If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will be shuffled within each other's original locations, and will not be accessible anywhere else, regardless of your chosen Item Pool Quality setting.
<br>
<br>If remake content is enabled, the Wonder Chomp, Stella 023, Sage Stick, Enduring Brooch, and Teamwork Band and their respective original locations are included in this pool.
<br>
<br>If disabled, all ten or fifteen locations will simply contain random items, like every other item location."""
    _id = "restrict_monstro"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class EXPStarsAnywhere(BooleanFlag):
    _name = "Shuffle EXP stars"
    _description = """If enabled, EXP stars may appear in chests that don't house them in the original game. Only one EXP star can appear per world area.
<br>
<br>If disabled, EXP stars will be restricted to their original locations in Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano."""
    _id = "xpstars"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class ShuffleHillFlowers(BooleanFlag):
    _name = "Shuffle Booster Hill flowers"
    _description = """If enabled, all sixteen Booster Hill flowers will be item checks.
<br>
<br>There are no missable flowers on Booster Hill in the randomizer. You can return to the hill as many times as you like to collect any you missed the first time."""
    _id = "hill"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class ShuffleCoins(BooleanFlag):
    _name = "Shuffle regular coins"
    _description = """If enabled, all freestanding gold coins will be item checks."""
    _id = "coins"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class MimicsAnywhere(BooleanFlag):
    _name = "Shuffle mimic chests"
    _description = """If enabled, any three chests in the world may be mimics. You will be able to run away from them. The Bean Valley mimic and Sunken Ship mimic will not appear before Land's End and Moleville respectively (except in the Rose Town Lazy Shell chests).
<br>
<br>If disabled, mimic chests will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley. You will not be able to run away from these fights."""
    _modes = ["open"]
    _id = "mimics"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class SlotsAnywhere(BooleanFlag):
    _name = "Shuffle slot machine chests"
    _description = """If enabled, the three slot machine chests in Bean Valley may be moved elsewhere.
<br>
<br>If disabled, the three original slot machines in Bean Valley will be unchanged."""
    _id = "slots"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class ShuffleBeetlemania(BooleanFlag):
    _name = "Shuffle Beetlemania"
    _description = """If enabled, the Mushroom Kingdom inn kid will give you a random item check for 500 coins. Beetlemania will appear in a random location."""
    _id = "beetle"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class ShuffleMagikoopaChest(BooleanFlag):
    _name = "Shuffle Magikoopa's coin chest"
    _description = """If enabled, the chest in Magikoopa's room will contain a random item check. A random chest somewhere in the game will contain infinite coins."""
    _id = "kamek"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class ShuffleWeddingGear(BooleanFlag):
    _name = "Shuffle Marrymore wedding gear"
    _description = """If enabled, the four pieces of wedding gear required to initiate the Marrymore boss fight will be located randomly within the world (not necessarily key item locations). The four NPCs in the chapel become item checks.
<br>
<br>If disabled, the Marrymore chapel minigame will behave as normal."""
    _id = "marry"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class FireworksOptions(CategorizationOption):
    """Enumeration for Fireworks flag option"""

    VANILLA = "Default"
    SHUFFLE_ONE = "Shuffle Fireworks"
    PROGRESSIVE = "Shuffle Progressive Fireworks"


# ✅
class FireworksSetting(SelectOneFlag[FireworksOptions]):
    _name = """Fireworks trade sequence"""
    _description = """<b>Default</b>: Unchanged from the original game. Buy from fireworks guy's house, trade for Shiny Stone, etc.
<br>
<br><b>Shuffle Fireworks</b>: One Fireworks is added to the "Special Item" pool, and the Fireworks shop becomes a "Special Item" location. The trading sequence is otherwise unchanged. The Monstro Town sealed door opens automatically if you trade away the Shiny Stone before using it.
<br>
<br><b>Shuffle Progressive Fireworks</b>: One Fireworks, Shiny Stone, and Carbo Cookie are each shuffled somewhere completely random in the game, and you will always receive them in order. The fireworks shop, Pur-Tend store, and cookie girl become key item checks. The Monstro Town sealed door opens automatically if you trade away the Shiny Stone before using it."""
    choices = [o for o in FireworksOptions]
    _default = FireworksOptions.VANILLA
    _id = "fireworks"
    _requires_all = [(ShuffleItems(), True)]


# ******** Progression availability


# ✅
class KeyItemsAnywhere(BooleanFlag):
    _name = '"Special Items" can appear in the general item pool'
    _description = """If enabled, items belonging to your "Special Items" pocket can appear in any item location.
<br>
<br>If disabled, the "Special Items" will only be shuffled within each other's locations.
<br>
<br>The items targeted by this setting are the <b>Rare Frog Coin</b>, <b>Wallet</b>, <b>Cricket Pie</b>, <b>Bambino Bomb</b>, <b>Castle Key 1</b>, <b>Castle Key 2</b>, <b>Alto Card</b>, <b>Tenor Card</b>, <b>Soprano Card</b>, <b>Greaper Flag</b>, <b>Dry Bones Flag</b>, <b>Big Boo Flag</b>, <b>Shed Key</b>, <b>Elder Key</b>, <b>Cricket Jam</b>, <b>Temple Key</b>, <b>Room Key</b>, <b>Seed</b>, <b>Fertilizer</b>, and <b>Bright Card</b>.
<br><br>Certain settings can also add the <b>Extra Shiny Stone</b>, <b>Crystal Shard</b>, <b>Ring</b>, <b>Brooch</b>, <b>Shoes</b>, <b>Crown</b>, <b>Fireworks</b>, <b>Shiny Stone</b>, <b>Carbo Cookie</b>, and <b>Gold Paint</b>.
"""
    _id = "keys_anywhere"
    _requires_all = [(ShuffleItems(), True)]
    # change EVENT_947_jmp_to_event_107" to point to event 949


# ✅
class StarPieceAvailability(BooleanFlag):
    _name = "Star Pieces can appear in the general item pool"
    _description = "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    _id = "stars_anywhere"
    _requires_all = [(ShuffleItems(), True)]
    # change EVENT_947_jmp_to_event_107" to point to event 949


class SpellsAnywhere(BooleanFlag):
    _name = "Spells can appear in the general item pool"
    _description = "If enabled, characters will learn spells by finding them in prize locations instead of by leveling up. Spells are still pre-assigned to characters, so for example if Mallow is supposed to learn Jump, finding the Jump spell will automatically assign it to Mallow."
    _id = "spells_anywhere"
    _requires_all = [(ShuffleItems(), True)]
    # change EVENT_947_jmp_to_event_107" to point to event 949


# ✅
class InvisibleFlagsSetting(BooleanFlag):
    _name = "Move invisible flag checks"
    _description = """Chooses where the invisible items placed by the Three Musty Fears are located. This setting will put your attention to detail and your knowledge of the world of SMRPG to the test!
<br>
<br>If "Default locations" is selected, these checks will remain in their default locations (Mario's Pad bed, Rose Town sign, Yo'ster Isle goalpost).
<br>
<br>If enabled, the three checks will be located somewhere random in the world as an invisible item. The Three Musty Fears will give you hints as to their locations.
<br>
<br>See the "Contribute" tab if you have a great idea for a potential place to move these checks to!"""
    _id = "moveflags"
    _requires_all = [(ShuffleItems(), True)]


# ✅
class Remake(BooleanFlag):
    _name = "Enable Remake content"
    _description = """If enabled, the seven postgame boss fights from the 2023 Switch remake and their rewards will be available in the game and included in all shuffle settings.
<br>
<br>The freestanding Flower Tab checks in Mushroom Way and Land's End will also be added.
<br>
<br>Boss fight locations will be available after you defeat the first iterations of those fights and also find the Stay Voucher. For example, you cannot do the postgame temple fight until after you have defeated the regular campaign temple fight, you can't use the Extra Shiny Stone until you've defeated the boss in the Monstro Town door the first time, etc.
<br>
<br>Defeating all seven bosses that have a postgame re-fight will unlock a check in Mario's Pad that normally contains the Stay Voucher (shuffled as a key item check)."""
    _id = "postgame"
    _remake = False
    _requires_all = [(ShuffleItems(), True)]


# ******** Progression Gating


# ✅
class BanditsWayGating(CategorizationOption):
    """Enumeration for Bandit's Way gating flag option"""

    MALLOW = "Recruit Mallow"
    MUSHROOM_WAY = "Finish Mushroom Way"
    HAMMER_BRO = "Defeat Hammer Bros"
    OPEN = "Always open"


# ✅
class BanditsWayGate(SelectOneFlag[BanditsWayGating]):
    _name = """Bandit's Way access"""
    _description = """<b>Recruit Mallow</b>: Bandit's Way will become available on the world map when Mallow joins the party.
<br>
<br><b>Finish Mushroom Way</b>: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
<br>
<br><b>Defeat Hammer Bros</b>: Bandit's Way will become available on the world map when you have found and defeated the Hammer Bros boss battle.
<br>
<br><b>Always Open</b>: Bandit's Way will be available on the world map from the start of the game."""
    modes = ["open"]
    choices = [o for o in BanditsWayGating]
    _default = BanditsWayGating.MALLOW
    _id = "bw"


# ✅
class KeroSewersGating(CategorizationOption):
    """Enumeration for Bandit's Way gating flag option"""

    MALLOW = "Recruit Mallow"
    MACK = "Defeat Mack"
    KINGDOM = "Liberate Mushroom Kingdom"
    RFC = "Turn in the RareFrogCoin"
    OPEN = "Always open"


# ✅
class KeroSewersGate(SelectOneFlag[KeroSewersGating]):
    _name = """Kero Sewers access"""
    _description = """<b>Recruit Mallow</b>: The entrance to Kero Sewers will open when Mallow joins the party.
<br>
<br><b>Defeat Mack</b>: The entrance to Kero Sewers will open when you have found and defeated the Mack boss battle.
<br>
<br><b>Liberate Mushroom Kingdom</b>: The entrance to Kero Sewers will open when you have defeated the Mushroom Kingdom boss fight.
<br>
<br><b>Turn in the Rare Frog Coin</b>: The entrance to Kero Sewers will open when you turn in the Rare Frog Coin at the Mushroom Kingdom shop.
<br>
<br><b>Always Open</b>: The entrance to Kero Sewers is open from the start of the game.
<br>
<br>This setting does not affect your ability to enter the sewer via Land's End."""
    choices = [o for o in KeroSewersGating]
    _default = KeroSewersGating.OPEN
    _id = "ks"
    # SEWERS_CLOSED - set when game starts, cleared by condition. or just not set if always open


# ✅
class ForestMazeGating(CategorizationOption):
    """Enumeration for Forest Maze gating flag option"""

    PIE = "Exchange Cricket Pie"
    OPEN = "Always open"


# ✅
class ForestMazeGate(SelectOneFlag[ForestMazeGating]):
    _name = """Forest Maze access"""
    _description = """<b>Exchange Cricket Pie</b>: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
<br>
<br><b>Always Open</b>: Forest Maze will be available on the world map from the start of the game."""
    choices = [o for o in ForestMazeGating]
    _default = ForestMazeGating.PIE
    _id = "fm"


# ✅
class PipeVaultGating(CategorizationOption):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    OPEN = "Always open"


# ✅
class PipeVaultGate(SelectOneFlag[PipeVaultGating]):
    _name = """Pipe Vault access"""
    _description = """<b>Recruit Geno</b>: Pipe Vault will be unblocked when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: Pipe Vault will be unblocked when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: Pipe Vault will be unblocked when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Always Open</b>: Pipe Vault will be unblocked from the start of the game."""
    choices = [o for o in PipeVaultGating]
    _default = PipeVaultGating.OPEN
    _id = "pv"


# ✅
class Moleville1Gating(CategorizationOption):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    BOSHI = "Overthrow Boshi"
    OPEN = "Always open"


# ✅
class Moleville1Gate(SelectOneFlag[Moleville1Gating]):
    _name = """Moleville Mines entrance access"""
    _description = """<b>Recruit Geno</b>: The top door inside the Moleville Mines entrance will be accessible when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: The top door inside the Moleville Mines entrance will be accessible when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: The top door inside the Moleville Mines entrance will be accessible when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Defeat Boshi</b>: The top door inside the Moleville Mines entrance will be accessible when you beat Boshi in a one-on-one race.
<br>
<br><b>Always Open</b>: The top door inside the Moleville Mines entrance will be accessible from the start of the game."""
    choices = [o for o in Moleville1Gating]
    _default = Moleville1Gating.OPEN
    _id = "me"


# ✅
class BoosterTowerGating(CategorizationOption):
    """Enumeration for Booster Tower gating flag option"""

    MARIO = "Recruit Mario"
    MALLOW = "Recruit Mallow"
    GENO = "Recruit Geno"
    BOWSER = "Recruit Bowser"
    TOADSTOOL = "Recruit Toadstool"
    MINES = "Finish Moleville Mines"
    PUNCHINELLO = "Defeat Punchinello"
    OPEN = "Always open"


# ✅
class BoosterTowerGate(SelectOneFlag[BoosterTowerGating]):
    _name = """Booster Tower access"""
    _description = """<b>Recruit character</b>: Booster Tower's door can be unlocked when you recruit the selected character.
<br>
<br><b>Finish Moleville</b>: Booster Tower's door will unlock when you defeat the final boss of Moleville.
<br>
<br><b>Defeat Punchinello</b>: Booster Tower's door will unlock when you have found and defeated the Punchinello boss battle.
<br>
<br><b>Always Open</b>: Booster Tower's door will be unlocked from the start of the game."""
    choices = [o for o in BoosterTowerGating]
    _default = BoosterTowerGating.BOWSER
    _id = "bt"


# ✅
class BoosterHillGating(CategorizationOption):
    """Enumeration for Booster Hill gating flag option"""

    TOWER = "Finish Booster Tower"
    KGGG = "Defeat Knife Guy & Grate Guy"
    OPEN = "Always open"


# ✅
class BoosterHillGate(SelectOneFlag[BoosterHillGating]):
    _name = """Booster Hill access"""
    _description = """<b>Finish Booster Tower</b>: The Booster Hill chase sequence will be available when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Defeat Knife Guy & Grate Guy</b>: The Booster Hill chase sequence will be available when you have found and defeated the Knife Guy & Grate Guy boss battle.
<br>
<br><b>Always Open</b>: The Booster Hill chase sequence will be available from the start of the game."""
    choices = [o for o in BoosterHillGating]
    _default = BoosterHillGating.OPEN
    _id = "bh"


# ✅
class MarrymoreGating(CategorizationOption):
    """Enumeration for Marrymore gating flag option"""

    HILL = "Finish Booster Hill"
    TOWER = "Finish Booster Tower"
    KGGG = "Defeat Knife Guy & Grate Guy"
    OPEN = "Always open"


# ✅
class MarrymoreGate(SelectOneFlag[MarrymoreGating]):
    _name = """Marrymore back door access"""
    _description = """<b>Finish Booster Hill</b>: The chapel back door will open when you complete Booster Hill one time.
<br>
<br><b>Finish Booster Tower</b>: The chapel back door will open when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Defeat Knife Guy & Grate Guy</b>: The chapel back door will open when you have found and defeated the Knife Guy & Grate Guy boss battle.
<br>
<br><b>Always Open</b>: The chapel back door will be open from the start of the game."""
    modes = ["open"]
    choices = [o for o in MarrymoreGating]
    _default = MarrymoreGating.HILL
    _id = "mm"


# ✅
class YaridovichGating(CategorizationOption):
    """Enumeration for Seaside boss gating flag option"""

    SHIP = "Finish Sunken Ship"
    JOHNNY = "Defeat Johnny"
    OPEN = "Always available"


# ✅
class YaridovichGate(SelectOneFlag[YaridovichGating]):
    _name = """Seaside boss fight access"""
    _description = """<b>Finish Sunken Ship</b>: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
<br>
<br><b>Defeat Johnny</b>: The Seaside boss fight will become available after you find and defeat the Johnny boss fight.
<br>
<br><b>Always Open</b>: The Seaside boss will be available from the start of the game."""
    choices = [o for o in YaridovichGating]
    _default = YaridovichGating.SHIP
    _id = "seaside"


# ✅
class SeaGating(CategorizationOption):
    """Enumeration for Sea & Sunken Ship gating flag option"""

    TOADSTOOL = "Recruit Toadstool"
    STAR_4 = "Collect 4 Star Pieces"
    BUNDT = "Defeat Bundt"
    MARRYMORE = "Finish Marrymore"
    OPEN = "Always open"


# ✅
class SeaGate(SelectOneFlag[SeaGating]):
    _name = """Sea & Sunken Ship access"""
    _description = """<b>Recruit Toadstool</b>: The Sea will become available on the world map when Toadstool joins the party.
<br>
<br><b>Collect 4 Star Pieces</b>: The Sea will become available on the world map when you collect 4 Star Pieces.
<br>
<br><b>Defeat Bundt</b>: The Sea will become available on the world map when you have found and defeated the Bundt boss battle.
<br>
<br><b>Always Open</b>: The Sea & Sunken Ship will be available on the world map from the start of the game."""
    choices = [o for o in SeaGating]
    _default = SeaGating.STAR_4
    _id = "sea"


# ✅
class LandsEndGating(CategorizationOption):
    """Enumeration for Land's End gating flag option"""

    STAR_5 = "Collect 5 Star Pieces"
    ELDER = "Rescue and talk to the Seaside Town elder"
    YARIDOVICH = "Defeat Yaridovich"
    SEASIDE = "Finish Seaside Town"
    OPEN = "Always open"


# ✅
class LandsEndGate(SelectOneFlag[LandsEndGating]):
    _name = """Land's End access"""
    _description = """<b>Collect 5 Star Pieces</b>: The cannon in Land's End will become usable when you collect 5 Star Pieces.
<br>
<br><b>Rescue and talk to the Seaside Town elder</b>: The cannon in Land's End will become usable on the world map when you rescue the elder in Seaside Town and speak with him. You will need to defeat the Sunken Ship boss and have the Shed Key to release the elder.
<br>
<br><b>Always Open</b>: The cannon in Land's End is usable from the start of the game."""
    choices = [o for o in LandsEndGating]
    _default = LandsEndGating.OPEN
    _id = "land"


# ✅
class BelomeTempleGating(CategorizationOption):
    """Enumeration for Belome Temple gating flag option"""

    KEY = "Use Temple Key"
    OPEN = "Always open"


# ✅
# no KI shuffle + closed monstro + use key = invalid, causes a softlock
class BelomeTempleGate(SelectOneFlag[BelomeTempleGating]):
    _name = """Belome Temple boss access"""
    _description = """<b>Use Temple Key</b>: The temple elevator will never lead to the boss fight until you dispel the Belome statue.
<br>
<br><b>Always Open</b>: The temple elevator works as normal."""
    choices = [o for o in BelomeTempleGating]
    _default = BelomeTempleGating.OPEN
    _id = "tmpl"


# ✅
class MonstroTownGating(CategorizationOption):
    """Enumeration for Monstro Town gating flag option"""

    LANDS_END = "Finish Land's End"
    BELOME_2 = "Defeat Belome 2"
    OPEN = "Always open"


# ✅
class MonstroTownGate(SelectOneFlag[MonstroTownGating]):
    _name = """Monstro Town access"""
    _description = """<b>Finish Land's End</b>: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
<br>
<br><b>Defeat Belome 2</b>: Monstro Town will become available on the World Map when you have found and defeated the Belome 2 boss battle. The pipe in Land's End will be blocked until this happens.
<br>
<br><b>Always Open</b>: Monstro Town will be available on the World Map from the start of the game."""
    choices = [o for o in MonstroTownGating]
    _default = MonstroTownGating.LANDS_END
    _id = "mt"


# ✅
class SkipMustyFearsSequence(BooleanFlag):
    _name = "Skip 3 Musty Fears sequence"
    _description = """This flag affects the Musty Fears checks (normally Mario's Pad bed, Rose Town sign, and Yo'ster Isle goalpost; or whichever three locations are added to the seed when "Move invisible flag checks" is set).
<br>
<br>If disabled, the affected checks will become available after you visit the Musty Fears Inn in Monstro Town.
<br>
<br>If enabled, the affected checks will be available from the start of the seed."""
    _id = "skip_musty"


# ✅
class NimbusGating(CategorizationOption):
    """Enumeration for Nimbus Land gating flag option"""

    VALLEY = "Finish Bean Valley"
    MEGASMILAX = "Defeat Megasmilax"
    PAINT = "Find Gold Paint"
    OPEN = "Always open"


# ✅
class NimbusGate(SelectOneFlag[NimbusGating]):
    _name = """Nimbus Land access"""
    _description = """<b>Finish Bean Valley</b>: The trampoline to Nimbus Land will be enabled once you defeat the boss of Bean Valley.
<br>
<br><b>Defeat Megasmilax</b>: The trampoline to Nimbus Land will be enabled when you have found and defeated the Megasmilax boss battle.
<br>
<br><b>Find Gold Paint</b>: The trampoline to Nimbus Land is enabled by default, but you will need to find an item called "Gold Paint" before Garro will take you into the castle.
<br>
<br><b>Always Open</b>: Nimbus Land and its castle are open from the start of the game."""
    choices = [o for o in NimbusGating]
    _default = NimbusGating.OPEN
    _id = "nl"


# ✅
class BarrelVolcanoGating(CategorizationOption):
    """Enumeration for Barrel Volcano gating flag option"""

    NIMBUS = "Finish Nimbus Land"
    VALENTINA = "Defeat Valentina"
    OPEN = "Always open"


# ✅
class BarrelVolcanoGate(SelectOneFlag[BarrelVolcanoGating]):
    _name = """Barrel Volcano access"""
    _description = """<b>Finish Nimbus Land</b>: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
<br>
<br><b>Defeat Valentina</b>: Barrel Volcano will become available on the World Map when you have found and defeated the Valentina boss battle.
<br>
<br><b>Always Open</b>: Barrel Volcano will be available on the World Map from the start of the game."""
    choices = [o for o in BarrelVolcanoGating]
    _default = BarrelVolcanoGating.NIMBUS
    _id = "bv"


# ✅
class BowsersKeepGating(CategorizationOption):
    """Enumeration for Bowser's Keep gating flag option"""

    STAR_6 = "Collect 6 Star Pieces"
    VOLCANO = "Finish Barrel Volcano"
    AXEM = "Defeat Axem Rangers"
    OPEN = "Always open"


# ✅
class BowsersKeepGate(SelectOneFlag[BowsersKeepGating]):
    _name = """Bowser's Keep access"""
    _description = """<b>Collect 6 Star Pieces</b>: Bowser's Keep will become available on the world map when you collect 6 Star Pieces.
<br>
<br><b>Finish Barrel Volcano</b>: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
<br>
<br><b>Defeat Axem Rangers</b>: Bowser's Keep will become available on the World Map when you have found and defeated the Axem Rangers boss battle.
<br>
<br><b>Always Open</b>: Bowser's Keep will be available on the world map from the start of the game."""
    choices = [o for o in BowsersKeepGating]
    _default = BowsersKeepGating.VOLCANO
    _id = "bk"


# ✅
class FactoryGating(CategorizationOption):
    """Enumeration for Factory gating flag option"""

    OPEN = "Open when Bowser's Keep is opened"
    KEEP = "Finish Bowser's Keep"
    STAR_6 = "Collect 6 Star Pieces"
    EXOR = "Defeat Exor"


# ✅
class FactoryGate(SelectOneFlag[FactoryGating]):
    _name = """Factory access"""
    _description = """<b>Open when Bowser's Keep is opened</b>: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
<br>
<br><b>Finish Bowser's Keep</b>: Factory will become available on the world map when you complete Bowser's Keep for the first time.
<br>
<br><b>Defeat Exor</b>: Factory will become available on the World Map when you have found and defeated the Exor boss battle and Bowser's Keep has been opened.
<br>
<br><b>Collect 6 Star Pieces</b>: Factory will become available on the world map when you collect 6 Star Pieces and Bowser's Keep has been opened."""
    choices = [o for o in FactoryGating]
    _default = FactoryGating.KEEP
    _id = "wf"


# ✅


from ..progression import prizelocations
from ..types.prizelocation import (
    PrizeLocation,
    BossFightLocation,
    StarPieceLocation,
    CharacterRecruitmentLocation,
    StandingLocation,
)
from ..types.prize import CoinPrize, FrogCoinPrize


def _location_class_to_attr_name(cls: type[PrizeLocation]) -> str:
    """Convert a PrizeLocation class to an attribute name for the enum."""
    # Use the class name, converting CamelCase to Snake_Case
    import re

    name = cls.__name__
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name


def _is_freestanding_coin_location(cls: type[PrizeLocation]) -> bool:
    """Check if a location is a freestanding item that originally held coins (not frog coins)."""
    if not issubclass(cls, StandingLocation):
        return False
    originally_held = getattr(cls, "_originally_held", None)
    if originally_held is None:
        return False
    # Check if it's a CoinPrize but not a FrogCoinPrize
    return issubclass(originally_held, CoinPrize) and not issubclass(originally_held, FrogCoinPrize)


# Build enum members dynamically from prizelocations
_item_check_members = {}
_boss_fight_check_members = {}
_star_piece_check_members = {}
for cls in vars(prizelocations).values():
    if isinstance(cls, type) and issubclass(cls, PrizeLocation) and hasattr(cls, "_id"):
        # Skip freestanding coin locations - they always get their original items
        if _is_freestanding_coin_location(cls):
            continue
        attr_name = _location_class_to_attr_name(cls)
        if issubclass(cls, StarPieceLocation) and cls is not StarPieceLocation:
            _star_piece_check_members[attr_name] = cls
        elif issubclass(cls, BossFightLocation) and cls is not BossFightLocation:
            _boss_fight_check_members[attr_name] = cls
        elif cls is not PrizeLocation and not issubclass(
            cls, (BossFightLocation, StarPieceLocation, CharacterRecruitmentLocation)
        ):
            _item_check_members[attr_name] = cls
# Create enums dynamically using functional API
ItemCheckEnum = ClassCategorizationOption("ItemCheckEnum", _item_check_members)
BossFightCheckEnum = ClassCategorizationOption(
    "BossFightCheckEnum", _boss_fight_check_members
)
StarPieceCheckEnum = ClassCategorizationOption(
    "StarPieceCheckEnum", _star_piece_check_members
)


# ✅
class EnabledRegularChecks(CategorizationFlag[ItemCheckEnum]):
    _name = "General item pool checks"
    _description = """If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>This setting only applies if you have "Special Items can appear in the general item pool" or "Star Pieces can appear in the general item pool" enabled.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "chests"
    _default = {o: True for o in ItemCheckEnum.__members__.values()}
    _requires_all = [(ShuffleItems(), True)]
    _requires_any = [(KeyItemsAnywhere(), True), (StarPieceAvailability(), True), (SpellsAnywhere(), True)]


# ✅
class EnabledBossChecks(CategorizationFlag[BossFightCheckEnum]):
    _name = "Boss location star pieces"
    _description = """If a check is highlighted (white text over blue), it is eligible to contain a boss fight that un-gates an area.
<br>
<br>If a check is not highlighted, its contents can still be shuffled, but it will not contain a boss fight that un-gates an area.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "bosses"
    _default = {o: True for o in BossFightCheckEnum.__members__.values()}
    _requires_all = [(ShuffleStarPieces(), True)]


# ✅
class ReplaceItems(BooleanFlag):
    _name = "Replace some chest items with coins"
    _description = "If enabled, the worst items (Wilt Shrooms, etc) will sometimes be replaced with coins in chests."
    _id = "replace"


# ✅
class PoisonMushroom(BooleanFlag):
    _name = "Change Fake Mushroom's Effect"
    _description = (
        "Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give "
        "one status effect per seed, which has a 1/8 chance of being Invincibility."
    )
    _id = "fake"


# ✅
class EXPChallengeOptions(CategorizationOption):
    """Enumeration for exp star quality scaling option"""

    VANILLA = "Default"
    STARS = "Star Pieces"
    BOSSES = "Bosses"
    NONE = "None"


# ✅
class EXPChallenge(SelectOneFlag[EXPChallengeOptions]):
    _name = "EXP Star Behaviour"
    _description = """<b>Default</b>: EXP stars can give you 1 to 11 EXP per hit as normal.
<br>
<br><b>Star Pieces</b>: EXP per star increases with the number of Star Pieces collected.
<br>
<br><b>Bosses</b>: EXP per star increases with the number of bosses you have defeated.
<br>
<br><b>No EXP</b>: EXP stars give you 0 EXP."""
    choices = [o for o in EXPChallengeOptions]
    _default = EXPChallengeOptions.VANILLA
    _id = "xpstar"


# ✅
class GrateGuyPrizeThreshold(RangeFlag):
    _name = 'Required "Look The Other Way" wins'
    _description = "The number of times required to win Grate Guy's casino minigame to receive its ultimate prize (normally the Star Egg after 100 wins)."
    _default = 1
    min_value = 1
    max_value = 255
    _id = "gg"


# ✅
class KnifeGuyPrizeThreshold(RangeFlag):
    _name = "Required Knife Guy wins (normal prize)"
    _description = "The number of wins minus losses required to win Knife Guy's juggling game prize (normally the Bright Card after 12 wins)."
    _default = 1
    min_value = 1
    max_value = 254
    _id = "kg"


# ✅
class SuitePrize1Threshold(RangeFlag):
    _name = "Required Suite prize #1 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the first special gift (normally a Flower Tab after 1 stay)."
    _default = 1
    min_value = 1
    max_value = 249
    _id = "s1"


# ✅
class SuitePrize2Threshold(RangeFlag):
    _name = "Required Suite prize #2 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the second special gift (normally a Flower Jar after 3 stays)."
    _default = 2
    min_value = 2
    max_value = 250
    _id = "s2"


# ✅
class SuitePrize3Threshold(RangeFlag):
    _name = "Required Suite prize #3 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the third special gift (normally a Frog Coin after 5 stays)."
    _default = 3
    min_value = 3
    max_value = 251
    _id = "s3"


# ✅
class SuitePrize4Threshold(RangeFlag):
    _name = "Required Suite prize #4 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the fourth special gift (normally 2 Frog Coins after 10 stays)."
    _default = 4
    min_value = 4
    max_value = 252
    _id = "s4"


# ✅
class SuitePrize5Threshold(RangeFlag):
    _name = "Required Suite prize #5 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the fifth special gift (normally 3 Frog Coins after 15 stays)."
    _default = 5
    min_value = 5
    max_value = 253
    _id = "s5"


# ✅
class SuitePrize6Threshold(RangeFlag):
    _name = "Required Suite prize #6 check-ins"
    _description = "The number of times required to stay (paid check-ins, overstays don't count) in the Marrymore Suite to receive the sixth special gift (normally 20 Frog Coins after 200 stays)."
    _default = 6
    min_value = 6
    max_value = 254
    _id = "s6"


# ✅
class SuperJump1Threshold(RangeFlag):
    _name = "Required Super Jumps for prize #1"
    _description = "The number of consecutive Super Jumps required for the first prize in Monstro Town (normally an Attack Scarf at 30)."
    _default = 30
    min_value = 1
    max_value = 99
    _id = "sj1"


# ✅
class SuperJump2Threshold(RangeFlag):
    _name = "Required Super Jumps for prize #2"
    _description = """The number of consecutive Super Jumps required for the second prize in Monstro Town (normally a Super Suit at 100).
<br>
<br>A Super Suit is more likely to be here if you keep the threshold at 100 and don't lower it."""
    _default = 100
    min_value = 2
    max_value = 100
    _id = "sj2"


# ✅
class FixKnifeGuy(BooleanFlag):
    _name = "Fix Knife Guy max prize glitch"
    _description = """In the original game, Knife Guy runs a dialog that suggests you get a Red Essence at 255 net wins. However, a command to actually add the item to your inventory is missing, so the item you get is just a random mushroom like normal. This flag fixes this and turns it into a check."""
    _id = "fix_kg"


# ✅
class KnifeGuyFixedPrizeThreshold(RangeFlag):
    _name = "Required Knife Guy wins (max prize)"
    _description = "The number of wins minus losses required to win Knife Guy's maxed out game prize (originally intended to be a Red Essence at 255). Must be higher than Knife Guy's other prize check."
    _default = 2
    min_value = 2
    max_value = 255
    _id = "kg2"
    _requires_all = [(FixKnifeGuy(), True)]


class BowserDoorRequirements(RangeFlag):
    _name = "Required Bowser's Keep obstacle doors"
    _description = "The number of doors required to progress through Bowser's Keep."
    _default = 4
    min_value = 1
    max_value = 6
    _id = "doorcount"


# ✅
class StarPiecesRequired(RangeFlag):
    _name = "Star Pieces required to access the final Factory boss"
    _description = "The total number of Star Pieces (0-7) that are required to access the final boss (enables the green button in Inner Factory). Cannot be higher than Total Star Pieces."
    _default = 6
    min_value = 0
    max_value = 7
    _id = "endgame"


# ✅
class CasinoWarp(BooleanFlag):
    _name = "Casino Warp"
    _description = """If enabled, a trampoline warping directly to the final boss fight will become available in Grate Guy's Casino."""
    _id = "cwarp"


# ✅
class BucketWarp(BooleanFlag):
    _name = "Bucket Warp"
    _description = "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss fight."
    _id = "bwarp"


# ✅
class FastTravel(BooleanFlag):
    _name = "Fast travel"
    _description = """If enabled, the following features will be enabled:
<ol>
<li>The Booster Tower balcony (after defeating the boss) will always return you to the ground level.</li>
<li>Inner Factory has a trampoline that exits to the world map.</li>
<li>When you first reach the Inner Factory from the Outer Factory, the Inner Factory will get its own dot on the world map.</li>
</ol>"""
    _id = "fasttravel"


# ✅
class WinConditions(CategorizationOption):
    """Enumeration for win condition options"""

    FACTORY = "Beat the final Factory boss"
    SMITHY = "Beat Smithy"
    STARS = "Collect required Star Pieces"
    SEALED = "Beat Monstro Town sealed door"


# ✅
class WinCondition(SelectOneFlag[WinConditions]):
    _name = "Condition required to beat the game"
    _description = """<b>Beat the Factory</b> (default): When you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
<br>
<br><b>Beat Smithy</b>: The game is over as soon as you find Smithy and defeat him. (If you don't have him shuffled into the boss pool, this is the same thing as "Beat the Factory".)
<br>
<br><b>Collect required Star Pieces</b>: As soon as you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the game is finishe regardless of where you found your final Star Piece.
<br>
<br><b>Beat Monstro Town sealed door</b>: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count."""
    choices = [o for o in WinConditions]
    _default = WinConditions.FACTORY
    _id = "objective"


# ******** Puzzles


# ✅
class BallSolitaireShuffle(BooleanFlag):
    _name = "Randomize Ball Solitaire"
    _description = "The layout for the Ball Solitaire minigame will be randomized."
    _id = "ball"


# ✅
class MagicButtonShuffle(BooleanFlag):
    _name = "Randomize Magic Buttons"
    _description = "The layout for the Magic Buttons minigame will be randomized."
    _id = "button"


# ✅
class QuizShuffle(BooleanFlag):
    _name = "Randomize Dr. Topper Quiz"
    _description = "The question pool for the Dr. Topper quiz will include new questions submitted by players."
    _id = "quiz"


# ✅
class QuizIncludeNonSmrpg(BooleanFlag):
    _name = "Include non-SMRPG questions"
    _description = "The question pool will also include questions that are not related to Super Mario RPG."
    _id = "quizext"
    _requires_all = [(QuizShuffle(), True)]


# ✅
class RandomTadpolePondSong(BooleanFlag):
    _name = "Randomize Tadpole Pond songs"
    _description = """If enabled, the songs required for the three Tadpole Pond songs will be selected from a pool (submitted by players). Hints will be available in their normal locations within Tadpole Pond, Moleville Mines, and Monstro Town."""
    _id = "melody"


# ✅
class RandomSunkenShipPassword(BooleanFlag):
    _name = "Randomize Sunken Ship password"
    _description = """If enabled, the password for the Sunken Ship will be selected from a pool (submitted by players). Hints are available in the 6 ship puzzles, and occasionally on posted notes within the Sunken Ship.
<br/>
<br/><b>Be warned that some of these are very difficult, or may be references to things you aren't familiar with, but they are all solvable.</b> The nearby shop shaman will tell you how many of your letters were correct when you submit an incorrect password."""
    _id = "pwd"


# ✅
class BowserDoorShuffle(BooleanFlag):
    _name = "Randomize Bowser's Keep room sequences"
    _description = """If enabled, the 18 rooms making up the six Bowser's Keep obstacle course doors will be shuffled into six random sequences of three rooms each."""
    _id = "doorshuffle"


# ✅
class SkipMinecart(BooleanFlag):
    _name = "Skip Minecart minigame"
    _description = """If enabled, boarding the minecart for the first time will teleport you back to Moleville. Subsequent visits to the minecart room will play the minigame as normal."""
    _id = "skipcart"


# ✅
class BetterTips(BooleanFlag):
    _name = "Better Event RNG"
    _description = """If enabled, the following changes will take effect:
<br/>
<br/>Some repeatable item grants will give a better, or wider, variety of items. Example of this include Knife Guy's juggling game junk prizes, or tips from working in the Marrymore hotel. This setting has no impact on singular, clearable item checks.
<br/>
<br/>Your odds on Mushroom Boy's prizes and the Mushroom Derby cookie bet races will be improved.
<br/>
<br/>The cloud miniboss in Land's End will have an increased spawn rate. 
<br/>
<br/>Forest Maze mushrooms may be ANY kind of mushroom.
    """
    _id = "rng"


# ******** Shops


# if this is disabled, no options in this category can be changed


# ✅
class ShuffleShops(BooleanFlag):
    _name = "Randomize the contents of shops"
    _description = """If enabled, the contents of all regular shops and Frog Coin shops will be randomized. This includes the Marrymore suite room service menu, the Moleville bomb shop, and the blue toad treasure shop in Moleville."""
    _id = "rshops"


# ✅
class ShopQualities(CategorizationOption):
    """Enumeration for shop shuffle quality option"""

    ORIGINAL = "Original shop pool"
    COMPLETELY_RANDOM = "Completely random items"
    MOSTLY_RANDOM = "Random items, biased toward low-impact items"
    EMPTY = "Completely empty"


# ✅
class ShopQuality(SelectOneFlag[ShopQualities]):
    _name = """Shop contents quality"""
    _description = """Restricts the incidence of certain items in shops.
<br>
<br>"Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops.
<br>
<br>If "Completely empty" is selected, all shops will just sell the Goodie Bag."""
    choices = [o for o in ShopQualities]
    _default = ShopQualities.ORIGINAL
    _id = "shopqual"
    _requires_all = [(ShuffleShops(), True)]


# ✅
class BiasShopShuffle(BooleanFlag):
    _name = "Bias better items to gated shops"
    _description = (
        """If enabled, harder-to-reach shops will generally sell better items."""
    )
    _id = "biasshops"
    _requires_all = [
        (ShuffleShops(), True),
        (ShopQuality(), [o for o in ShopQualities if o != ShopQualities.EMPTY]),
    ]


# ✅
class NoPickMeUps(BooleanFlag):
    _name = "Exclude Pick Me Ups"
    _description = """If enabled, Pick Me Ups will not be sold in any shops."""
    _id = "nolife"
    _requires_all = [(ShuffleShops(), True)]


# ✅
class ShowEquips(BooleanFlag):
    _name = "Always show all permitted characters on equips"
    _description = "Always show who can equip what in stores."
    _id = "showperms"


# ✅
class FreeShops(BooleanFlag):
    _name = "'Free' Shops"
    _description = """If enabled, all shop items will cost 1 coin. You will start with 9999 coins and 999 frog coins."""
    _id = "free"


# ******** Enemies & Bosses


# ✅
class BossShuffle(BooleanFlag):
    _name = "Randomize boss fight locations"
    _description = "If enabled, the positions of bosses (plus Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled."
    _id = "rboss"
    # if false, disable stat scaling and mimics anywhere


# ✅
class BossScaleOptions(CategorizationOption):
    """Enumeration for shuffled boss stat scaling"""

    VANILLA = "Do not scale"
    MATCH = "Match to area"
    RANDOM = "Completely random"


# ✅
class BossShuffleScaleStats(SelectOneFlag[BossScaleOptions]):
    _name = "Scale boss stats"
    _description = """<b>Do not scale</b>: Boss fights retain their relative original stats, regardless of where they are placed. For example, Culex would still have around 4000 HP, even if he's in Mushroom Way.
<br>
<br><b>Match to area</b>: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss. For example, Culex would have about 100 HP if he's in Mushroom Way.
<br>
<br><b>Completely random</b>: A boss fight will inherit the relative stats of a random other location, regardless of position. For example, Culex could be placed in Mushroom Way, but have 1200 HP because he's inherited Belome 2's original stats. Only use this option if you have a reasonable expectation that the seed may not be feasible to complete."""
    choices = [o for o in BossScaleOptions]
    _default = BossScaleOptions.MATCH
    _id = "bossscale"
    _requires_all = [(BossShuffle(), True)]


# ✅
class KeepMinigameSpritesIntact(BooleanFlag):
    _name = "Keep some shuffled NPCs intact"
    _description = """If disabled: All sprites related to an area boss and their corresponding battles will be changed to match the shuffled positions of bosses. Note that sprite replacements will not affect gameplay, i.e. hitboxes stay the same for the Booster Hill henchmen, the Mack Skip NPCs, etc.
<br>
<br>If enabled:
<ul>
<li>Dodo will always peck the statues even if he is not the statue room boss fight.</li>
<li>The snifits on Booster Hill will not be replaced by any henchmen belonging to the first tower boss.</li>
<li>The shy guys in the Mushroom Kingdom throne room will not be swapped out for other sprites.</li>
<li>All Mushroom Kingdom shy guys, Moleville crooks and bob-ombs, Booster Pass apprentice, Booster Tower snifits, Bandana Reds, and inner factory Mad Mallets battles will not be replaced.</li>
</ul>."""
    _id = "allsprites"
    _requires_all = [(BossShuffle(), True)]


# Leaving this out of 9.0.0 because not sure what palettes we have available to us that might be unused in order to expand it to remake bosses.
# Probably a good dedicated project for someone who wants to develop for this.
# class DifferentiateRepeatedBosses(BooleanFlag):
#     _name = "Differentiate similar bosses"
#     _description = """If enabled, Croco, Jinx, Belome, and the four mimics (as well as Punchinello, Johnny, Bundt, Culex, and Booster if remake content is enabled) will look slightly different in the overworld depending on which version of the fight it is.
# <br>
# <br>Croco 2 will have a darker hat.
# <br>
# <br>Jinx 2/3's hair will be black/white respectively.
# <br>
# <br>Belome 2 will be more subdued, and coloured like the golden Belome statue.
# <br>
# <br>Pandorite will be tinted orange, Hidon will be tinted green, and Chester will be tinted purple."""
#     _id = "diff"
#     _requires_all = [(BossShuffle(), True)]
# This is NOT considered a cosmetic because it reveals information that otherwise would only be seen in batte.
# Ideas:
# move chocolate cake palette to postgame bundt
# blue shirt booster (not purple-y)
# blue hat punchinello (not purple-y)
# invert johnny blue and red
# make culex purple lighter
# blue hair jinx
# silver belome
# ^ The above were all suggested based on accessibility for colour-blind players.


# ShuffledBossEnum is created lazily to avoid circular import with prizes module
# Using ShuffledBossEnumType for type checking (defined as Enum in TYPE_CHECKING block)
ShuffledBossEnum: type[ShuffledBossEnumType] | None = None
_shuffled_boss_enum_populated = False


def _ensure_shuffled_boss_enum_populated() -> None:
    """Create ShuffledBossEnum dynamically from ALL_BOSS_FIGHTS on first access."""
    global ShuffledBossEnum, _shuffled_boss_enum_populated
    if _shuffled_boss_enum_populated:
        return
    _shuffled_boss_enum_populated = True

    from ..progression.prizes import ALL_BOSS_FIGHTS

    members = {}
    for boss_class in ALL_BOSS_FIGHTS:
        attr_name = _boss_class_to_attr_name(boss_class)
        members[attr_name] = boss_class

    ShuffledBossEnum = ClassCategorizationOption("ShuffledBossEnum", members)


# Helper function for boss class name conversion
def _boss_class_to_attr_name(boss_class: type) -> str:
    """Convert boss class name to an attribute name.

    Examples:
        Croco1BossFight -> Croco_1
        KnifeGuyGrateGuyBossFight -> Knife_Guy_Grate_Guy
        Culex3DBossFight -> Culex_3D
    """
    import re

    name = boss_class.__name__
    # Remove BossFight/Fight suffix
    name = re.sub(r"(BossFight|Fight|Dight)$", "", name)
    # Add spaces before capital letters and numbers
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", name)
    name = re.sub(r"(\d+)", r" \1", name)
    # Clean up multiple spaces and convert to underscores
    name = re.sub(r"\s+", " ", name).strip()
    return name.replace(" ", "_").replace("-", "_")


# ✅
class ShuffledBosses(CategorizationFlag[ShuffledBossEnumType]):  # type: ignore[type-arg]
    _name = "Shuffled boss fights"
    _description = """Each boss fight location below states the enemy that originally inhabits it.
<br>
<br>If a location is highlighted (white text over blue), there will instead be a random different boss inhabiting that location.
<br>
<br>If a boss is not highlighted, the location's original boss fight will stay there.
<br>
<br>Selecting a remake-specific boss will do nothing if the remake flag is not enabled."""
    _id = "pool"
    _requires_all = [(BossShuffle(), True)]

    @property
    def default(self) -> dict:
        """Lazy default that ensures ShuffledBossEnum is populated first."""
        _ensure_shuffled_boss_enum_populated()
        return {o: True for o in ShuffledBossEnum.__members__.values()}  # type: ignore[union-attr]

    def __init__(self) -> None:
        _ensure_shuffled_boss_enum_populated()
        self._default = {o: True for o in ShuffledBossEnum.__members__.values()}  # type: ignore[union-attr]
        super().__init__()


# ✅
class EnemyStatsShuffleOptions(CategorizationOption):
    """Enumeration for enemy stat randomization option"""

    DISABLED = "Original stats"
    NUMBERS_ONLY = "Stat values only"
    FULL_RANDOM = "Everything"


# ✅
class EnemyStats(SelectOneFlag[EnemyStatsShuffleOptions]):
    _name = "Randomize enemy stats"
    _description = """Choose what should be randomized about enemy stats (includes normal mobs and bosses).
<br>
<br><b>Stat values only</b>: Attack, defense, speed, and HP values are randomized. Elemental weaknesses/resistances and status immunities remain unchanged.
<br>
<br><b>Everything</b>: Attack, defense, speed, and HP values are randomized. Elemental weaknesses/resistances and status immunities are also randomized.
<br>
<br><b>Original stats</b>: Enemy stats remain unchanged."""
    _id = "enemystats"
    choices = [o for o in EnemyStatsShuffleOptions]
    _default = EnemyStatsShuffleOptions.DISABLED


# ✅
class EnemyDrops(BooleanFlag):
    _name = "Randomize enemy drops"
    _description = "If enabled, the EXP and in-battle items received from battles will be randomized."
    _id = "drops"


# ✅
class EnemyFormations(BooleanFlag):
    _name = "Randomize formations"
    _description = """If enabled, enemy encounters may contain random unexpected additional enemies and be laid out erratically. Boss formations are not affected."""
    _id = "formations"


# ✅
class EnemyAttacks(BooleanFlag):
    _name = "Randomize attack stats and effects"
    _description = "If enabled, enemy spells and attacks will have their power randomized. Attacks which cast statuses will have the status effects randomized, and attacks which normally don't inflict statuses may inflict unexpected statuses."
    _id = "attacks"


# ✅
class EnemySpells(BooleanFlag):
    _name = "Randomize enemy spell assignments"
    _description = "If enabled, enemies can cast random spells (excluding remake spells). I.E. Mack could cast Blast instead of Flame."
    _id = "enemyspells"


# ✅
class ExperienceNoRegular(BooleanFlag):
    _name = "Remove EXP from regular enemy encounters"
    _description = "If enabled, regular enemy encounters will not give any EXP when defeated. Boss fights are not affected by this flag."
    _id = "noregexp"


# ✅
class ExperienceNoBosses(BooleanFlag):
    _name = "Remove EXP from boss encounters"
    _description = "If enabled, boss encounters will not give any EXP when defeated. Regular enemy encounters are not affected by this flag."
    _id = "nobossexp"


# ✅
class SkipBossFights(BooleanFlag):
    _name = "Allow alternate boss fight win conditions"
    _description = """If set, the following actions will allow you to skip a boss fight and still proceed as normal:
<ul>
<li> Mack Skip</li>
<li> Booster Tower curtain game</li>
<li> Nimbus Castle statue game</li>
</ul>
<br/>If unset, you must still fight the associated boss to receive Star Pieces and other rewards."""
    _id = "skips"


# ✅
class NoGenoWhirlExor(BooleanFlag):
    _name = "No Geno Whirl on Exor"
    _description = (
        "If enabled, stunning Exor's eyes will not make him vulnerable to Geno Whirl."
    )
    _id = "nowhirl"


# ✅
class FixMagikoopa(BooleanFlag):
    _name = "Fix Magikoopa"
    _description = (
        "If enabled, King Bomb's Big Bang will not disable Magikoopa's attacks."
    )
    _id = "nobigbang"


# ✅
class NoOHKO(BooleanFlag):
    _name = "No instant KOs on boss allies"
    _description = (
        "You will not be able to use Geno Whirl, Pure Water, or Lamb's Lure/Sheep Attack to OHKO any allies to a boss (Mallow Clone, "
        "Bandana Blue, Fautso, etc)."
    )
    _id = "noko"


# ******** Cosmetics and Accessibility
# aka stuff that doesn't affect the seed


class MarioPaletteOptions(CategorizationOption):
    """Enumeration for Mario Palette Name options"""

    RANDOM = "Random"
    DEFAULT = "Default"
    JUMPMAN = "Jumpman"
    FIREMARIO = "Fire Mario"
    LUIGI = "Luigi"
    FIRELUIGI = "Fire Luigi"
    WARIO = "Wario"
    WALUIGI = "Waluigi"
    BUILDER = "Builder"
    MEGAMAN = "Mega Man"
    GREY = "Grey"
    ZOMBIE = "Zombio"
    SPONGE = "Sponge"
    PRETZEL = "Pretzel"
    MARLON = "Marlon"
    GRANDDAD = "Grand Dad"
    BLUE2 = "Blue2"



class MarioPaletteChoice(SelectOneFlag[MarioPaletteOptions]):
    _name = "Mario Palette"
    _description = "Choose Mario's Palette"
    choices = [
        MarioPaletteOptions.DEFAULT,
        MarioPaletteOptions.RANDOM,
        *sorted(o for o in MarioPaletteOptions if o not in [MarioPaletteOptions.RANDOM, MarioPaletteOptions.DEFAULT]),
    ]

    _default = MarioPaletteOptions.DEFAULT
    _id = "mariopalette"



class MallowPaletteOptions(CategorizationOption):
    """Enumeration for Mallow Palette Name options"""

    RANDOM = "Random"
    DEFAULT = "Default"
    MOKURA = "Mokura"
    FROG = "Frog"
    PALOM = "Palom"
    POROM = "Porom"
    CLOUD = "Cloud"
    STORMY = "Stormy"
    LIGHT = "Light"
    WATER = "Water"
    RED = "Red"
    MINT = "Mint"
    DEMON = "Demon"
    RAINCLOUD = "Rain Cloud"



class MallowPaletteChoice(SelectOneFlag[MallowPaletteOptions]):
    _name = "Mallow Palette"
    _description = "Choose Mallow's Palette"
    choices = [
        MallowPaletteOptions.DEFAULT,
        MallowPaletteOptions.RANDOM,
        *sorted(o for o in MallowPaletteOptions if o not in [MallowPaletteOptions.RANDOM, MallowPaletteOptions.DEFAULT]),
    ]
    _default = MallowPaletteOptions.DEFAULT
    _id = "mallowpalette"



class GenoPaletteOptions(CategorizationOption):
    """Enumeration for Geno Palette Name options"""

    RANDOM = "Random"
    DEFAULT = "Default"
    PINK = "Millnium"
    MAGIKOOPA = "Magikoopa"
    MAGIKOOPARED = "Magikoopa Red"
    LINK = "Zelda"
    VLADOR = "Vlador"
    LIGHT = "Light"
    PURPLE = "Purple"
    GREY = "Grey"
    GREEN = "Green"
    DARK = "Dark"



class GenoPaletteChoice(SelectOneFlag[GenoPaletteOptions]):
    _name = "Geno Palette"
    _description = "Choose Geno's Palette"
    choices = [
        GenoPaletteOptions.DEFAULT,
        GenoPaletteOptions.RANDOM,
        *sorted(o for o in GenoPaletteOptions if o not in [GenoPaletteOptions.RANDOM, GenoPaletteOptions.DEFAULT]),
    ]
    _default = GenoPaletteOptions.DEFAULT
    _id = "genopalette"



class BowserPaletteOptions(CategorizationOption):
    """Enumeration for Bowser Palette Name options"""

    RANDOM = "Random"
    DEFAULT = "Default"
    DRYBONE = "Dry Bone"
    CULEX = "Culex"
    WABOWSER = "Wabowser"
    RED = "Red"
    DARK = "Dark"
    KRONK = "Korush"
    ZECCET = "Zeccet"
    BLUE = "Melee Blue"
    SKING = "S.King"



class BowserPaletteChoice(SelectOneFlag[BowserPaletteOptions]):
    _name = "Bowser Palette"
    _description = "Choose Bowser's Palette"
    choices = [
        BowserPaletteOptions.DEFAULT,
        BowserPaletteOptions.RANDOM,
        *sorted(o for o in BowserPaletteOptions if o not in [BowserPaletteOptions.RANDOM, BowserPaletteOptions.DEFAULT]),
    ]
    _default = BowserPaletteOptions.DEFAULT
    _id = "bowserpalette"



class ToadstoolPaletteOptions(CategorizationOption):
    """Enumeration for Toadstool Palette Name options"""

    RANDOM = "Random"
    DEFAULT = "Default"
    DAISY = "Daisy"
    PAULINE = "Pauline"
    ROSALINA = "Rosalina"
    PALUTENA = "Palutena"
    KUMATORA = "Kumatora"
    TIA = "Tia"
    KAIRI = "Kairi"
    LEENA = "Leena"
    EMERALDA = "Emeralda"
    MIKU = "Miku"
    JASMINE = "Jasmine"
    KOTORI = "Kotori"
    ZOMBIE = "Zombie"
    BLOOD = "Blood Peach"
    DEMON = "Demon"
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    BLACK = "Black"
    INDIGO = "Indigo"
    SHADOWQ = "Shadow Q."



class ToadstoolPaletteChoice(SelectOneFlag[ToadstoolPaletteOptions]):
    _name = "Toadstool Palette"
    _description = "Choose Toadstool's Palette"
    choices = [
        ToadstoolPaletteOptions.DEFAULT,
        ToadstoolPaletteOptions.RANDOM,
        *sorted(o for o in ToadstoolPaletteOptions if o not in [ToadstoolPaletteOptions.RANDOM, ToadstoolPaletteOptions.DEFAULT]),
    ]
    _default = ToadstoolPaletteOptions.DEFAULT
    _id = "toadstoolpalette"

# ✅
class ChangeNames(BooleanFlag):
    _name = "Change character names"
    _description = """Some palette swaps are references to other media. If this flag is enabled, the character's name will be changed to match the palette."""
    _id = "names"


# ✅
class RemakeNames(BooleanFlag):
    _name = "Use Remake Names"
    _description = "Spells, enemies, items, and attacks will use their names from the 2023 Switch remake (where space limits allow)."
    _id = "remake"


# ✅
class CanonNames(BooleanFlag):
    _name = "Use Canon Names"
    _description = "Magikoopa is renamed 'Kamek' and Birdo is renamed 'Birdetta'."
    _id = "canon"


# ✅
class Peach(BooleanFlag):
    _name = "Rename Peach"
    _description = (
        "Toadstool is renamed 'Peach' (overridden by palette name swaps, if enabled)."
    )
    _id = "peach"


# ✅
class JapaneseABXY(BooleanFlag):
    _name = "Japanese ABXY buttons"
    _description = "If this flag is enabled, ABXY buttons will have the Super Famicom colours from the Japanese version of the game instead of the SNES purple."
    _id = "abxy"


# ✅
class BossShuffleMusic(BooleanFlag):
    _name = "Randomize battle music"
    _description = "All battle music will be randomized."
    _id = "music"


# ✅
from randomizer.data.variables.music_tracks import MusicTrack


# ✅
# Default music IDs: 0x06, 0x03, 0x19, 0x44, 0x23, 0x26, 0x3E, 0x3B
_DEFAULT_MUSIC_IDS = {6, 3, 25, 68, 35, 38, 62, 59}


# ✅
class ShuffledMusic(CategorizationFlag[MusicTrack]):
    _name = "Battle music pool"
    _description = """Eight tunes will be chosen at random for boss battles. Deselect any tracks you don't want to include in the pool.
<br><br>This setting does nothing if "Randomize boss music" is turned off."""
    _id = "avail_music"
    _default = {o: o.music_id in _DEFAULT_MUSIC_IDS for o in MusicTrack}
    _requires_all = [(BossShuffleMusic(), True)]


# ✅
class RemoveFlashes(BooleanFlag):
    _name = "Remove flashes"
    _description = """Removes some flashing animations (from spells, attacks, etc). 
<br>
<br>Disclaimer: While this feature is intended to promote accessibility, SMRPG Randomizer's developers are not accessibility experts and we may have missed some things. Players and viewers with photosensitivity should continue to engage with this randomizer at their own risk. If you would like to suggest an animation that should have flashes removed by this feature, please go to "Resources -> Report an Issue" in the randomizer website's menu."""
    _id = "noflash"


# ✅
class HoldB(BooleanFlag):
    _name = "Hold B to auto-advance text"
    _description = "Holding the B button will advance text boxes."
    _id = "holdb"


#############


class FlagCategory:
    """Base class for a collection of settings."""

    _id: str = ""
    _name: str = ""
    _subcategories: "list[type[FlagCategory]]" = []
    _flags: list[type[Flag]] = []
    _size: int = 3

    @property
    def id(self) -> str:
        """An identifier for this collection to use internally."""
        return self._id

    @property
    def name(self) -> str:
        """An identifier for this collection to appear in the frontend."""
        return self._name

    @property
    def subcategories(self) -> "list[type[FlagCategory]]":
        """Subcategories for this collection."""
        return self._subcategories

    @property
    def flags(self) -> list[type[Flag]]:
        """Individual settings that belong in this collection."""
        return self._flags

    @property
    def size(self) -> int:
        """Something to do with the frontend that I don't remember"""
        return self._size


class CharacterRecruitmentSubcategory(FlagCategory):
    """Collection of settings related to character recruitment."""

    _name: str = "Character Recruitment"
    _flags: list[type[Flag]] = [
        ShuffleCharacters,
        MaxCharacters,
        AvailableCharacters,
        StartingCharacters,
    ]
    _size: int = 4
    _id: str = "P"


class CharacterEquipmentSubcategory(FlagCategory):
    """Collection of settings related to equipment properties."""

    _name: str = "Character Equipment"
    _flags: list[type[Flag]] = [
        EquipmentCharacters,
        EquipmentProperties,
        IgnoreNamesakeProperties,
        StarPieceHints,
    ]
    _size: int = 4
    _id: str = "Q"


class CharacterStatsSpellsSubcategory(FlagCategory):
    """Collection of settings related to learnable spells."""

    _name: str = "Character Stats & Spells"
    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        InfuseSpellElements,
        CharacterSpellElements,
        UncapSuperJumps,
        AvailableSpells,
    ]
    _size: int = 4
    _id = "C"


class PartyCategory(FlagCategory):
    """Pan-collection of settings related to party members and equips."""

    _name: str = "Party & Equipment"
    _subcategories: list[type[FlagCategory]] = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory,
    ]
    _id: str = "PartyCategory"


class StarPiecesCategory(FlagCategory):
    """Collection of settings related to star piece distribution."""

    _flags: list[type[Flag]] = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
        ProgressionLogicDifficulty,
        DisperseStarPieces,
    ]
    _size: int = 3
    _id: str = "X"


class ItemShuffleSubcategory(FlagCategory):
    """Collection of settings related to item distribution."""

    _name: str = "Item Shuffle"
    _flags: list[type[Flag]] = [
        ShuffleItems,
        ItemQuality,
        AnnoyingChests,
        BiasItemShuffle,
        NoStarEgg,
        RestrictSpecialEquips,
        EXPStarsAnywhere,
        ShuffleHillFlowers,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        FireworksSetting,
    ]
    _id: str = "T"


class ItemLocationSubcategory(FlagCategory):
    """Collection of settings related to item availability."""

    _name: str = "Item Locations"
    _flags: list[type[Flag]] = [
        KeyItemsAnywhere,
        StarPieceAvailability,
        SpellsAnywhere,
        InvisibleFlagsSetting,
        Remake,
        EnabledRegularChecks,
    ]
    _id: str = "L"


class BehaviourSubcategory(FlagCategory):
    """Collection of settings related to item and minigame behaviour."""

    _name: str = "Behaviour & Minigames"
    _flags: list[type[Flag]] = [
        ReplaceItems,
        PoisonMushroom,
        EXPChallenge,
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        FixKnifeGuy,
        KnifeGuyFixedPrizeThreshold,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
        SuperJump1Threshold,
        SuperJump2Threshold,
    ]
    _id: str = "I"


class ItemsCategory(FlagCategory):
    """Pan-collection of settings related to items."""

    _name: str = "Items & Star Pieces"
    _subcategories: list[type[FlagCategory]] = [
        StarPiecesCategory,
        ItemShuffleSubcategory,
        ItemLocationSubcategory,
        BehaviourSubcategory,
    ]
    _id: str = "ItemsCategory"


class AreaAccessSubcategory(FlagCategory):
    """Collection of settings related to area gating logic."""

    _name: str = "Area Access"
    _flags: list[type[Flag]] = [
        BanditsWayGate,
        KeroSewersGate,
        ForestMazeGate,
        PipeVaultGate,
        Moleville1Gate,
        BoosterTowerGate,
        BoosterHillGate,
        MarrymoreGate,
        SeaGate,
        LandsEndGate,
        BelomeTempleGate,
        MonstroTownGate,
        NimbusGate,
        BarrelVolcanoGate,
        BowsersKeepGate,
        FactoryGate,
    ]
    _size: int = 3
    _id: str = "A"


class OtherAccessSubcategory(FlagCategory):
    """Collection of settings related to event gating logic."""

    _name: str = "Other Access & Win Condition"
    _flags: list[type[Flag]] = [
        YaridovichGate,
        SkipMustyFearsSequence,
        BowserDoorRequirements,
        StarPiecesRequired,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        WinCondition,
    ]
    _size: int = 3
    _id: str = "O"


class PuzzleCategory(FlagCategory):
    """Collection of settings related to puzzles."""

    _name: str = "Puzzles & Minigames"
    _flags: list[type[Flag]] = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
        QuizIncludeNonSmrpg,
        RandomTadpolePondSong,
        RandomSunkenShipPassword,
        BowserDoorShuffle,
        SkipMinecart,
        BetterTips,
    ]
    _size: int = 3
    _id: str = "G"


class ShopsCategory(FlagCategory):
    """Collection of settings related to shops."""

    _name: str = "Shops"
    _flags: list[type[Flag]] = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        NoPickMeUps,
        ShowEquips,
        FreeShops,
    ]
    _size: int = 3
    _id: str = "S"


class AccessCategory(FlagCategory):
    """Pan-collection of settings related to logical access and puzzles."""

    _name: str = "Progression & Shops"
    _subcategories: list[type[FlagCategory]] = [
        AreaAccessSubcategory,
        OtherAccessSubcategory,
        PuzzleCategory,
        ShopsCategory,
    ]
    _id: str = "AccessCategory"


class BossPositionSubcategory(FlagCategory):
    """Collection of settings related to boss placement."""

    _name: str = "Boss Position"
    _flags: list[type[Flag]] = [
        BossShuffle,
        BossShuffleScaleStats,
        KeepMinigameSpritesIntact,
        # DifferentiateRepeatedBosses,
        ShuffledBosses,
    ]
    _size: int = 4
    _id: str = "B"


class BossStatSubcategory(FlagCategory):
    """Collection of settings related to enemy stats."""

    _name: str = "Enemy Stats"
    _flags: list[type[Flag]] = [
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemySpells,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]
    _size: int = 4
    _id: str = "E"


class BossCheeseSubcategory(FlagCategory):
    """Collection of settings related to boss exploits."""

    _name: str = "Boss Exploits"
    _flags: list[type[Flag]] = [
        SkipBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    _size: int = 4
    _id: str = "F"


class BossCategory(FlagCategory):
    """Pan-collection of settings related to bosses."""

    _name: str = "Enemies & Boss Fights"
    _subcategories: list[type[FlagCategory]] = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory,
    ]
    _id: str = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    """Collection of settings related to accessibility."""

    _name: str = "Accessibility"
    _flags: list[type[Flag]] = [RemoveFlashes, HoldB]
    _size: int = 3
    _id: str = "R"


class MusicSubcategory(FlagCategory):
    """Collection of settings related to music cosmetics."""

    _name: str = "Music"
    _flags: list[type[Flag]] = [BossShuffleMusic, ShuffledMusic]
    _size: int = 3
    _id: str = "R"


class PaletteSubcategory(FlagCategory):
    """Collection of settings related to visual cosmetics."""

    _name: str = "Visual Cosmetics"
    _flags: list[type[Flag]] = [
        JapaneseABXY,
        MarioPaletteChoice,
        MallowPaletteChoice,
        GenoPaletteChoice,
        BowserPaletteChoice,
        ToadstoolPaletteChoice,
    ]
    _size: int = 3
    _id: str = "R"


class NamesCategory(FlagCategory):

    _name: str = "Names"
    _flags: list[type[Flag]] = [PlayAsStarter, ChangeNames, RemakeNames, CanonNames, Peach]
    _size: int = 3
    _id: str = "R"


class CosmeticCategory(FlagCategory):
    """Pan-collection of settings related to things that don't affect logic."""

    _name: str = "Player Experience"
    _subcategories: list[type[FlagCategory]] = [
        AccessibilitySubcategory,
        MusicSubcategory,
        PaletteSubcategory,
        NamesCategory,
    ]


FlagCategoryT = TypeVar(
    "FlagCategoryT",
    CharacterRecruitmentSubcategory,
    CharacterEquipmentSubcategory,
    CharacterStatsSpellsSubcategory,
    PartyCategory,
    StarPiecesCategory,
    ItemShuffleSubcategory,
    ItemLocationSubcategory,
    BehaviourSubcategory,
    ItemsCategory,
    AreaAccessSubcategory,
    OtherAccessSubcategory,
    PuzzleCategory,
    ShopsCategory,
    AccessCategory,
    BossPositionSubcategory,
    BossStatSubcategory,
    BossCheeseSubcategory,
    BossCategory,
    AccessibilitySubcategory,
    MusicSubcategory,
    PaletteSubcategory,
    NamesCategory,
    CosmeticCategory,
    FlagCategory,
)

CATEGORIES = (
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
    CosmeticCategory,
)

#############

"""Base classes for settings presets."""


class Preset:
    """A pre-created settings string"""

    _name: str = ""
    _description: str = ""
    _flags: str = ""

    @property
    def name(self) -> str:
        """The name of this preset as it appears on the site"""
        return self._name

    @property
    def description(self) -> str:
        """A brief description of who this preset is meant for and what it does"""
        return self._description

    @property
    def flags(self) -> str:
        """The string that corresponds to the desired settings"""
        return self._flags

    @classmethod
    def id(cls):
        """An identifier for this preset to use internally."""
        return cls.__name__


class TestPreset(Preset):
    """test preset"""

    _name: str = "test preset"
    _description: str = "test"
    _flags: str = "P(random|max:5)"


PRESETS = [TestPreset]
