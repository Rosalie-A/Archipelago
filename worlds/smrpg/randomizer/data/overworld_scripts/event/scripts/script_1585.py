# E1585_MIDAS_RIVER_BARREL_SUBROUTINE
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
	Pause(1, identifier="EVENT_1585_pause_0"),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1585_pause_0"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1585_set_var_to_const_7"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1585_set_var_to_const_22"]),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1585_set_var_to_const_37"]),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_1585_set_var_to_const_52"]),
	Jmp(["EVENT_1585_pause_0"]),
	SetVarToConst(TEMP_70AB, 23, identifier="EVENT_1585_set_var_to_const_7"),
	SetVarToConst(X_COORD_2, 1820),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1312),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1570),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1062),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 554),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 46),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	ClearBit(TEMP_7043_0),
	Jmp(["EVENT_1585_pause_0"]),
	SetVarToConst(TEMP_70AB, 23, identifier="EVENT_1585_set_var_to_const_22"),
	SetVarToConst(X_COORD_2, 6202),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 6460),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 5952),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 5444),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 4678),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 4936),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	ClearBit(TEMP_7043_4),
	Jmp(["EVENT_1585_pause_0"]),
	SetVarToConst(TEMP_70AB, 23, identifier="EVENT_1585_set_var_to_const_37"),
	SetVarToConst(X_COORD_2, 2646),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 2904),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 2396),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1630),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1888),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 1380),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	ClearBit(TEMP_7043_5),
	Jmp(["EVENT_1585_pause_0"]),
	SetVarToConst(TEMP_70AB, 23, identifier="EVENT_1585_set_var_to_const_52"),
	SetVarToConst(X_COORD_2, 7028),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 7286),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 6520),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 6778),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 6012),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	SetVarToConst(X_COORD_2, 5504),
	JmpToSubroutine(["EVENT_1585_copy_var_to_var_67"]),
	ClearBit(TEMP_7043_6),
	Jmp(["EVENT_1585_pause_0"]),
	CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2, identifier="EVENT_1585_copy_var_to_var_67"),
	VarShiftLeft(X_COORD_2, 8),
	SetVarToConst(Z_COORD_2, 10),
	ActionQueueAsync(target=MEM_70AB, subscript=[
		A_UnknownCommand(bytearray(b'\x9a')),
		A_VisibilityOn(),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	SetSyncActionScript(MEM_70AB, A0163_MIDAS_SMALL_COIN),
	Inc(TEMP_70AB),
	Pause(2),
	Return()
])
