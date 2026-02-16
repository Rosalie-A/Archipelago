# E1754_LANDS_END_FINAL_WHIRLPOOL_2
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
	SetVarToConst(TEMP_70AC, 0),
	ClearBit(BELOME_HEAD_1),
	ClearBit(BELOME_HEAD_2),
	ClearBit(BELOME_HEAD_3),
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1754_jmp_if_object_in_level_6"]),
	SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
	JmpIfObjectInSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06, ["EVENT_1754_copy_var_to_var_17"], identifier="EVENT_1754_jmp_if_object_in_level_6"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_1753_run_event_as_subroutine_3"]),
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL, identifier="EVENT_1754_run_event_as_subroutine_9"),
	EnterArea(room_id=R263_LANDS_END_UNDERGROUND_AREA_01, face_direction=SOUTH, x=5, y=91, z=15, run_entrance_event=True),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	JmpIfBitClear(LANDS_END_CHEST_2_REQUESTED, ["EVENT_1754_ret_16"]),
	SummonObjectToSpecificLevel(NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	Return(identifier="EVENT_1754_ret_16"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1754_copy_var_to_var_17"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_1753_jmp_if_bit_set_11"]),
	Jmp(["EVENT_1753_run_event_as_subroutine_3"]),
	Jmp(["EVENT_1753_run_event_as_subroutine_3"])
])
