# E0023_MUSHROOM_SELECTION
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 100),
        CompareVarToConst(PRIMARY_TEMP_7000, 20),
        JmpIfComparisonResultIsLesser(["mushroom_0"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 40),
        JmpIfComparisonResultIsLesser(["mushroom_1"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 60),
        JmpIfComparisonResultIsLesser(["mushroom_2"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 65),
        JmpIfComparisonResultIsLesser(["mushroom_3"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 70),
        JmpIfComparisonResultIsLesser(["mushroom_4"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 75),
        JmpIfComparisonResultIsLesser(["mushroom_5"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 85),
        JmpIfComparisonResultIsLesser(["mushroom_6"]),
        SetVarToConst(ITEM_ID, BadMushroomItem),
        Return(),
        SetVarToConst(ITEM_ID, MushroomItem, identifier="mushroom_0"),
        Return(),
        SetVarToConst(ITEM_ID, MidMushroomItem, identifier="mushroom_1"),
        Return(),
        SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="mushroom_2"),
        Return(),
        SetVarToConst(ITEM_ID, WiltShroomItem, identifier="mushroom_3"),
        Return(),
        SetVarToConst(ITEM_ID, RottenMushItem, identifier="mushroom_4"),
        Return(),
        SetVarToConst(ITEM_ID, MoldyMushItem, identifier="mushroom_5"),
        Return(),
        SetVarToConst(ITEM_ID, MushroomItem2, identifier="mushroom_6"),
        Return(),
    ]
)
