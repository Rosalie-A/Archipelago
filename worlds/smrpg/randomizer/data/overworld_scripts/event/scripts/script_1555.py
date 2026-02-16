# E1555_FOREST_FIRST_WIGGLER_ROOM_LOADER_CONTD
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
	Set7016701BToObjectXYZ(target=NPC_0),
	CopyVarToVar(from_var=X_COORD_2, to_var=TEMP_7026),
	CopyVarToVar(from_var=Y_COORD_2, to_var=TEMP_7028),
	Pause(3, identifier="EVENT_1555_pause_3"),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1555_pause_3"]),
	JmpIfObjectActionScriptIsRunning(NPC_3, ["EVENT_1555_pause_3"]),
	JmpIfVarNotEqualsConst(TEMP_702E, 20, ["EVENT_1555_clear_bit_8"]),
	SetVarToConst(TEMP_70AF, 0),
	ClearBit(TEMP_7043_7, identifier="EVENT_1555_clear_bit_8"),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	SetVarToRandom(PRIMARY_TEMP_7000, 4096),
	CompareVarToConst(PRIMARY_TEMP_7000, 2048),
	JmpIfComparisonResultIsLesser(["EVENT_1555_mem_7000_and_const_15"]),
	SetBit(TEMP_7043_7),
	Mem7000AndConst(0x07FF, identifier="EVENT_1555_mem_7000_and_const_15"),
	CompareVarToConst(PRIMARY_TEMP_7000, 1024),
	JmpIfComparisonResultIsLesser(["EVENT_1555_mem_7000_and_const_19"]),
	SetBit(TEMP_7044_0),
	Mem7000AndConst(0x03FF, identifier="EVENT_1555_mem_7000_and_const_19"),
	CompareVarToConst(PRIMARY_TEMP_7000, 512),
	JmpIfComparisonResultIsLesser(["EVENT_1555_mem_7000_and_const_23"]),
	SetBit(TEMP_7044_1),
	Mem7000AndConst(0x0007, identifier="EVENT_1555_mem_7000_and_const_23"),
	Inc(PRIMARY_TEMP_7000),
	SetObjectMemoryToVar(UNKNOWN_7006),
	Pause(4),
	EndLoop(),
	CopyVarToVar(from_var=TEMP_7026, to_var=X_COORD_1),
	CopyVarToVar(from_var=TEMP_7028, to_var=Y_COORD_1),
	SetVarToConst(Z_COORD_1, 256),
	SetVarToConst(PRIMARY_TEMP_7000, 20),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	StartLoopNTimes(3),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Move70107015To7016701B(),
		A_UnknownCommand(bytearray(b'\x99')),
		A_SetWalkingSpeed(NORMAL)
	]),
	Inc(TEMP_70A9),
	EndLoop(),
	JmpToSubroutine(["EVENT_1555_jmp_if_bit_set_39"]),
	Jmp(["EVENT_1555_pause_3"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1555_set_action_script_45"], identifier="EVENT_1555_jmp_if_bit_set_39"),
	SetSyncActionScript(NPC_0, A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP),
	SetSyncActionScript(NPC_1, A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP),
	SetSyncActionScript(NPC_2, A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP),
	SetSyncActionScript(NPC_3, A0032_FIRST_WIGGLER_IN_FRONT_OF_STUMP),
	Jmp(["EVENT_1555_ret_49"]),
	SetSyncActionScript(NPC_0, A0033_FIRST_WIGGLER_BEHIND_STUMP, identifier="EVENT_1555_set_action_script_45"),
	SetSyncActionScript(NPC_1, A0033_FIRST_WIGGLER_BEHIND_STUMP),
	SetSyncActionScript(NPC_2, A0033_FIRST_WIGGLER_BEHIND_STUMP),
	SetSyncActionScript(NPC_3, A0033_FIRST_WIGGLER_BEHIND_STUMP),
	Return(identifier="EVENT_1555_ret_49")
])
