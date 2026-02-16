# E1553_FOREST_TREE_TRUNK_AREA_LOADER_CONTD
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
	SetVarToConst(TEMP_7026, 35),
	SetVarToConst(TEMP_7028, 36),
	ClearBit(TEMP_7044_2),
	SetBit(TEMP_7044_3),
	SetBit(TEMP_7044_4),
	Pause(3, identifier="EVENT_1553_pause_5"),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1553_pause_15"]),
	JmpIfObjectActionScriptIsRunning(NPC_3, ["EVENT_1553_pause_15"]),
	JmpIfVarNotEqualsConst(TEMP_702E, 20, ["EVENT_1553_set_var_to_const_10"]),
	SetVarToConst(TEMP_70AF, 0),
	SetVarToConst(TEMP_702A, 20, identifier="EVENT_1553_set_var_to_const_10"),
	CopyVarToVar(from_var=TEMP_7026, to_var=TEMP_702C),
	SetBit(TEMP_7044_7),
	JmpToSubroutine(["EVENT_1553_clear_bit_26"]),
	CopyVarToVar(from_var=TEMP_702C, to_var=TEMP_7026),
	Pause(3, identifier="EVENT_1553_pause_15"),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_1553_pause_5"]),
	JmpIfObjectActionScriptIsRunning(NPC_7, ["EVENT_1553_pause_5"]),
	JmpIfVarNotEqualsConst(TEMP_702E, 24, ["EVENT_1553_set_var_to_const_20"]),
	SetVarToConst(TEMP_70AF, 0),
	SetVarToConst(TEMP_702A, 24, identifier="EVENT_1553_set_var_to_const_20"),
	CopyVarToVar(from_var=TEMP_7028, to_var=TEMP_702C),
	ClearBit(TEMP_7044_7),
	JmpToSubroutine(["EVENT_1553_clear_bit_26"]),
	CopyVarToVar(from_var=TEMP_702C, to_var=TEMP_7028),
	Jmp(["EVENT_1553_pause_5"]),
	ClearBit(TEMP_7044_1, identifier="EVENT_1553_clear_bit_26"),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_6),
	SetVarToRandom(PRIMARY_TEMP_7000, 4096),
	CompareVarToConst(PRIMARY_TEMP_7000, 2048),
	JmpIfComparisonResultIsLesser(["EVENT_1553_mem_7000_and_const_33"]),
	SetBit(TEMP_7044_5),
	Mem7000AndConst(0x07FF, identifier="EVENT_1553_mem_7000_and_const_33"),
	CompareVarToConst(PRIMARY_TEMP_7000, 1024),
	JmpIfComparisonResultIsLesser(["EVENT_1553_jmp_if_7000_all_bits_clear_37"]),
	SetBit(TEMP_7044_6),
	JmpIf7000AllBitsClear(bits=[0], destinations=["EVENT_1553_jmp_if_bit_clear_39"], identifier="EVENT_1553_jmp_if_7000_all_bits_clear_37"),
	SetBit(TEMP_7044_1),
	JmpIfBitClear(TEMP_7044_4, ["EVENT_1553_copy_var_to_var_51"], identifier="EVENT_1553_jmp_if_bit_clear_39"),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1553_copy_var_to_var_46"]),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
	SetVarToConst(TEMP_702C, 34),
	SetVarToConst(X_COORD_2, 8192),
	SetVarToConst(Y_COORD_2, 11776),
	Jmp(["EVENT_1553_clear_mem_704x_at_7000_bit_55"]),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1553_copy_var_to_var_46"),
	SetVarToConst(TEMP_702C, 35),
	SetVarToConst(X_COORD_2, 6144),
	SetVarToConst(Y_COORD_2, 11008),
	Jmp(["EVENT_1553_clear_mem_704x_at_7000_bit_55"]),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1553_copy_var_to_var_51"),
	SetVarToConst(TEMP_702C, 36),
	SetVarToConst(X_COORD_2, 4608),
	SetVarToConst(Y_COORD_2, 9984),
	ClearMem704XAt7000Bit(identifier="EVENT_1553_clear_mem_704x_at_7000_bit_55"), # 7044.2-4
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
	SetMem704XAt7000Bit(),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	StartLoopNTimes(3),
	SetVarToConst(Z_COORD_2, 256),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_UnknownCommand(bytearray(b'\x99')),
		A_SetWalkingSpeed(NORMAL),
		A_JmpIfBitSet(TEMP_7044_1, ["EVENT_1553_inc_63"]),
		A_ShiftXYPixels(x=160, y=48)
	]),
	Inc(TEMP_70A9, identifier="EVENT_1553_inc_63"),
	EndLoop(),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_1553_copy_var_to_var_74"]),
	JmpIfRandom1of2(["EVENT_1553_copy_var_to_var_74"]),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_0),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_1553_jmp_if_bit_clear_71"]),
	SetBit(TEMP_7043_7),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_1553_jmp_73"], identifier="EVENT_1553_jmp_if_bit_clear_71"),
	SetBit(TEMP_7044_0),
	Jmp(["EVENT_1555_jmp_if_bit_set_39"], identifier="EVENT_1553_jmp_73"),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1553_copy_var_to_var_74"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	StartLoopNTimes(3),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1553_set_action_script_80"]),
	SetSyncActionScript(MEM_70A9, A0035_INNER_FORST_WIGGLER_NORTHEAST),
	Jmp(["EVENT_1553_inc_81"]),
	SetSyncActionScript(MEM_70A9, A0034_INNER_FORST_WIGGLER_SOUTHWEST, identifier="EVENT_1553_set_action_script_80"),
	Inc(TEMP_70A9, identifier="EVENT_1553_inc_81"),
	EndLoop(),
	Return()
])
