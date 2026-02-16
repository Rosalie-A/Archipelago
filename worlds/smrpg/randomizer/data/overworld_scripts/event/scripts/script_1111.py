# E1111_FROGFUCIUS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
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

script = EventScript([
	StoreItemAmountTo7000(CricketPieItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1111_remove_one_from_inventory_6"]),
	StoreItemAmountTo7000(CricketJamItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1111_jmp_if_bit_clear_12"]),
	JmpToEvent(E0947_FROGFUCIUS_HINT_MAIN_CHECKS, identifier="EVENT_1111_jmp_to_event_4"),
	Return(),
	RemoveOneOfItemFromInventory(CricketPieItem, identifier="EVENT_1111_remove_one_from_inventory_6"),
	SetBit(CRICKET_PIE_EXCHANGED),
	RunEventAsSubroutine(E1255_UNLOCK_FOREST_BY_PIE),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	StoreItemAmountTo7000(CricketJamItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1111_ret_15"]),
	JmpIfBitClear(CRICKET_PIE_EXCHANGED, ["EVENT_1111_run_dialog_16"], identifier="EVENT_1111_jmp_if_bit_clear_12"),
	RemoveOneOfItemFromInventory(CricketJamItem),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
    SetBit(CRICKET_JAM_EXCHANGED),
	Return(identifier="EVENT_1111_ret_15"),
	RunDialog(dialog_id=DI2759_FROGFUCIUS_CRICKET_JAM_WITHOUT_PIE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_16"),
	Jmp(["EVENT_1111_jmp_to_event_4"])
])
