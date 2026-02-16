# E3490_MIDAS_SMALL_MARIO_COORD_CALC
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
	Pause(2, identifier="EVENT_3490_pause_0"),
	Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_Y, pixel=True),
	Mem7000AndConst(0xFF00),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1792, ["EVENT_3490_jmp_if_bit_set_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5120, ["EVENT_3490_jmp_if_bit_set_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8704, ["EVENT_3490_jmp_if_bit_set_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12288, ["EVENT_3490_jmp_if_bit_set_93"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15616, ["EVENT_3490_set_bit_140"]),
	Jmp(["EVENT_3490_pause_0"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3490_pause_0"], identifier="EVENT_3490_jmp_if_bit_set_9"),
	SetBit(TEMP_7043_1),
	SetVarToConst(TEMP_70AB, 23),
	SetVarToConst(X_COORD_2, 3848),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4361),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4107),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_4, ["EVENT_3490_set_var_to_const_24"]),
	SetVarToConst(TEMP_70AB, 22),
	SetVarToConst(X_COORD_2, 4620),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(TEMP_70AB, 27),
	Jmp(["EVENT_3490_set_var_to_const_26"]),
	SetVarToConst(X_COORD_2, 4620, identifier="EVENT_3490_set_var_to_const_24"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4110, identifier="EVENT_3490_set_var_to_const_26"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4112),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4625),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3858),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4627),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	Jmp(["EVENT_3490_pause_0"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3490_pause_0"], identifier="EVENT_3490_jmp_if_bit_set_37"),
	SetBit(TEMP_7043_2),
	SetVarToConst(TEMP_70AB, 23),
	SetVarToConst(X_COORD_2, 3861),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4631),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3352),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_5, ["EVENT_3490_set_var_to_const_52"]),
	SetVarToConst(TEMP_70AB, 22),
	SetVarToConst(X_COORD_2, 3098),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(TEMP_70AB, 27),
	Jmp(["EVENT_3490_set_var_to_const_54"]),
	SetVarToConst(X_COORD_2, 3098, identifier="EVENT_3490_set_var_to_const_52"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4889, identifier="EVENT_3490_set_var_to_const_54"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3356),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2846),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3359),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2593),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	Jmp(["EVENT_3490_pause_0"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_3490_pause_0"], identifier="EVENT_3490_jmp_if_bit_set_65"),
	SetBit(TEMP_7043_3),
	SetVarToConst(TEMP_70AB, 23),
	SetVarToConst(X_COORD_2, 3362),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2083),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2596),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_6, ["EVENT_3490_set_var_to_const_80"]),
	SetVarToConst(TEMP_70AB, 22),
	SetVarToConst(X_COORD_2, 2086),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(TEMP_70AB, 27),
	Jmp(["EVENT_3490_set_var_to_const_82"]),
	SetVarToConst(X_COORD_2, 2086, identifier="EVENT_3490_set_var_to_const_80"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2344, identifier="EVENT_3490_set_var_to_const_82"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2090),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2349),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 1838),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 1327),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	Jmp(["EVENT_3490_pause_0"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3490_pause_0"], identifier="EVENT_3490_jmp_if_bit_set_93"),
	SetBit(TEMP_7043_4),
	SetVarToConst(TEMP_70AB, 23),
	SetVarToConst(X_COORD_2, 1329),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 1074),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3122),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_7, ["EVENT_3490_set_var_to_const_108"]),
	SetVarToConst(TEMP_70AB, 22),
	SetVarToConst(X_COORD_2, 3125),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(TEMP_70AB, 27),
	Jmp(["EVENT_3490_set_var_to_const_110"]),
	SetVarToConst(X_COORD_2, 3125, identifier="EVENT_3490_set_var_to_const_108"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 4150, identifier="EVENT_3490_set_var_to_const_110"),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3383),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 3128),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 2873),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	SetVarToConst(X_COORD_2, 5180),
	JmpToSubroutine(["EVENT_3490_copy_var_to_var_121"]),
	Jmp(["EVENT_3490_pause_0"]),
	CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2, identifier="EVENT_3490_copy_var_to_var_121"),
	CopyVarToVar(from_var=X_COORD_2, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0xFF00),
	Mem7000OrConst(0x0080),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_2),
	VarShiftLeft(Y_COORD_2, 248),
	CopyVarToVar(from_var=Y_COORD_2, to_var=PRIMARY_TEMP_7000),
	Mem7000OrConst(0x00E0),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2),
	SetVarToConst(Z_COORD_2, 0),
	JmpIfObjectNotInSpecificLevel(MEM_70AB, R069_MIDAS_RIVER_WATERFALL, ["EVENT_3490_pause_133"]),
	ActionQueueAsync(target=MEM_70AB, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop()
	]),
	Pause(1, identifier="EVENT_3490_pause_133"),
	JmpIfObjectActionScriptIsRunning(MEM_70AB, ["EVENT_3490_pause_133"]),
	SetSyncActionScript(MEM_70AB, A0173_MIDAS_RIVER_WATERFALL_INTERACTION),
	SummonObjectToSpecificLevel(MEM_70AB, R069_MIDAS_RIVER_WATERFALL),
	Inc(TEMP_70AB),
	Pause(1),
	Return(),
	SetBit(TEMP_7043_0, identifier="EVENT_3490_set_bit_140"),
	Return()
])
