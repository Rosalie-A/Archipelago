# E3375_KEEP_SET_DOOR_ORDER
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 4),
	SetVarToConst(KEEP_DOORS_EXIT_TYPE_1, 0),
	SetVarToConst(KEEP_DOORS_EXIT_TYPE_2, 0),
	SetVarToConst(UNKNOWN_70E7, 0),
	SetVarToConst(UNKNOWN_70E8, 0),
	SetVarToConst(UNKNOWN_70E9, 0),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	SetVarToConst(ROSE_WAY_703C, 1),
	SetVarToRandom(PRIMARY_TEMP_7000, 6, identifier="EVENT_3375_set_var_to_random_13"),
	AddConstToVar(PRIMARY_TEMP_7000, 24),
	JmpIfMem704XAt7000BitSet(["EVENT_3375_set_var_to_random_13"]),
	SetMem704XAt7000Bit(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_3375_copy_var_to_var_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 26, ["EVENT_3375_copy_var_to_var_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_3375_copy_var_to_var_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_3375_copy_var_to_var_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 29, ["EVENT_3375_copy_var_to_var_50"]),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	VarShiftLeft(ROSE_WAY_703E, 252),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
	Jmp(["EVENT_3375_inc_54"]),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3375_copy_var_to_var_28"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
	Jmp(["EVENT_3375_inc_54"]),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3375_copy_var_to_var_33"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	VarShiftLeft(ROSE_WAY_703E, 252),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
	Jmp(["EVENT_3375_inc_54"]),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3375_copy_var_to_var_39"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
	Jmp(["EVENT_3375_inc_54"]),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3375_copy_var_to_var_44"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	VarShiftLeft(ROSE_WAY_703E, 252),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
	Jmp(["EVENT_3375_inc_54"]),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3375_copy_var_to_var_50"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
	Inc(ROSE_WAY_703C, identifier="EVENT_3375_inc_54"),
	CompareVarToConst(ROSE_WAY_703C, 7),
	JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3375_set_var_to_random_13"]),
	Return()
])
