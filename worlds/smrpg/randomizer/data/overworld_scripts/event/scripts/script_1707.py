# E1707_BANDITS_WAY_5_LOADER_BACKGROUND
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
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_6),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	ResetCoords(NPC_5),
	ResetCoords(NPC_6),
	ResetCoords(NPC_7),
	ResetCoords(NPC_8),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_VisibilityOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JmpIfBitClear(TEMP_7043_7, ["EVENT_1707_clear_bit_9"]),
		A_Walk1StepSouth(),
		A_Walk1StepSoutheast(),
		A_Walk1StepEast(),
		A_WalkNortheastSteps(3)
	]),
	ClearBit(TEMP_7044_6, identifier="EVENT_1707_clear_bit_9"),
	SetVarToRandom(PRIMARY_TEMP_7000, 32768),
	JmpIf7000AllBitsClear(bits=[0], destinations=["EVENT_1707_clear_bit_13"]),
	SetBit(TEMP_7044_6),
	ClearBit(TEMP_7044_7, identifier="EVENT_1707_clear_bit_13"),
	CompareVarToConst(PRIMARY_TEMP_7000, 16384),
	JmpIfComparisonResultIsLesser(["EVENT_1707_mem_7000_and_const_17"]),
	SetBit(TEMP_7044_7),
	Mem7000AndConst(0x3FFF, identifier="EVENT_1707_mem_7000_and_const_17"),
	CompareVarToConst(PRIMARY_TEMP_7000, 8192),
	JmpIfComparisonResultIsLesser(["EVENT_1707_jmp_if_bit_set_22"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1707_set_var_to_const_77"]),
	Jmp(["EVENT_1707_set_var_to_const_59"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1707_set_var_to_const_41"], identifier="EVENT_1707_jmp_if_bit_set_22"),
	SetVarToConst(PRIMARY_TEMP_7000, 12288),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1707_clear_bit_13"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1707_action_queue_32"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1707_action_queue_30"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1707_action_queue_28"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkNortheastSteps(8)
	], identifier="EVENT_1707_action_queue_28"),
	Jmp(["EVENT_1707_action_queue_34"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorth(),
		A_Walk1StepNorthwest(),
		A_WalkNorthSteps(8)
	], identifier="EVENT_1707_action_queue_30"),
	Jmp(["EVENT_1707_action_queue_34"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorth(),
		A_WalkNorthwestSteps(9)
	], identifier="EVENT_1707_action_queue_32"),
	Jmp(["EVENT_1707_action_queue_34"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_BounceToXYWithHeight(x=11, y=95, height=0)
	], identifier="EVENT_1707_action_queue_34"),
	SetVarToConst(TEMP_70A9, 25),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7044_0),
	Jmp(["EVENT_1707_action_queue_97"]),
	SetVarToConst(PRIMARY_TEMP_7000, 28672, identifier="EVENT_1707_set_var_to_const_41"),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1707_clear_bit_13"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1707_action_queue_50"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1707_action_queue_48"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1707_action_queue_46"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSoutheastSteps(7),
		A_WalkEastSteps(3),
		A_WalkNortheastSteps(3)
	], identifier="EVENT_1707_action_queue_46"),
	Jmp(["EVENT_1707_action_queue_52"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkNortheastSteps(8)
	], identifier="EVENT_1707_action_queue_48"),
	Jmp(["EVENT_1707_action_queue_52"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSoutheastSteps(9),
		A_Walk1StepSouth(),
		A_Walk1StepSouthwest()
	], identifier="EVENT_1707_action_queue_50"),
	Jmp(["EVENT_1707_action_queue_52"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_BounceToXYWithHeight(x=15, y=107, height=0)
	], identifier="EVENT_1707_action_queue_52"),
	SetVarToConst(TEMP_70A9, 25),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7044_1),
	Jmp(["EVENT_1707_action_queue_100"]),
	SetVarToConst(PRIMARY_TEMP_7000, 4096, identifier="EVENT_1707_set_var_to_const_59"),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1707_clear_bit_13"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1707_action_queue_68"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1707_action_queue_66"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1707_action_queue_64"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSoutheastSteps(9),
		A_Walk1StepSouth(),
		A_Walk1StepSouthwest()
	], identifier="EVENT_1707_action_queue_64"),
	Jmp(["EVENT_1707_action_queue_70"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSouthwestSteps(8)
	], identifier="EVENT_1707_action_queue_66"),
	Jmp(["EVENT_1707_action_queue_70"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSouthSteps(8),
		A_Walk1StepSoutheast(),
		A_Walk1StepSouth(),
		A_Walk1StepSouthwest()
	], identifier="EVENT_1707_action_queue_68"),
	Jmp(["EVENT_1707_action_queue_70"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_BounceToXYWithHeight(x=11, y=115, height=0)
	], identifier="EVENT_1707_action_queue_70"),
	SetVarToConst(TEMP_70A9, 25),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7044_2),
	Jmp(["EVENT_1707_action_queue_103"]),
	SetVarToConst(PRIMARY_TEMP_7000, 20480, identifier="EVENT_1707_set_var_to_const_77"),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1707_clear_bit_13"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1707_action_queue_86"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1707_action_queue_84"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1707_action_queue_82"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorth(),
		A_WalkNorthwestSteps(9)
	], identifier="EVENT_1707_action_queue_82"),
	Jmp(["EVENT_1707_action_queue_88"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSouthwestSteps(3),
		A_WalkWestSteps(3),
		A_WalkNorthwestSteps(7)
	], identifier="EVENT_1707_action_queue_84"),
	Jmp(["EVENT_1707_action_queue_88"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSouthwestSteps(8)
	], identifier="EVENT_1707_action_queue_86"),
	Jmp(["EVENT_1707_action_queue_88"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_BounceToXYWithHeight(x=7, y=103, height=0)
	], identifier="EVENT_1707_action_queue_88"),
	SetVarToConst(TEMP_70A9, 25),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2),
	SetBit(TEMP_7044_3),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x12')),
		A_TransferToXYZF(x=10, y=90, z=0, direction=EAST)
	], identifier="EVENT_1707_action_queue_94"),
	Inc(TEMP_70A9),
	JmpIfVarEqualsConst(TEMP_70A9, 28, ["EVENT_1707_clear_bit_107"]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x12')),
		A_TransferToXYZF(x=14, y=102, z=0, direction=EAST)
	], identifier="EVENT_1707_action_queue_97"),
	Inc(TEMP_70A9),
	JmpIfVarEqualsConst(TEMP_70A9, 28, ["EVENT_1707_clear_bit_107"]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x12')),
		A_TransferToXYZF(x=10, y=110, z=0, direction=EAST)
	], identifier="EVENT_1707_action_queue_100"),
	Inc(TEMP_70A9),
	JmpIfVarEqualsConst(TEMP_70A9, 28, ["EVENT_1707_clear_bit_107"]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x12')),
		A_TransferToXYZF(x=6, y=98, z=0, direction=EAST)
	], identifier="EVENT_1707_action_queue_103"),
	Inc(TEMP_70A9),
	JmpIfVarEqualsConst(TEMP_70A9, 28, ["EVENT_1707_clear_bit_107"]),
	Jmp(["EVENT_1707_action_queue_94"]),
	ClearBit(TEMP_7043_7, identifier="EVENT_1707_clear_bit_107"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNortheast(),
		A_JmpIfBitClear(TEMP_7044_6, ["EVENT_1707_set_action_script_109"]),
		A_SetAllSpeeds(FASTEST),
		A_SetBit(TEMP_7043_7),
		A_WalkSouthwestSteps(3),
		A_Walk1StepWest(),
		A_Walk1StepNorthwest(),
		A_Walk1StepNorth(),
		A_FaceNorthwest()
	]),
	SetSyncActionScript(NPC_5, A0472_BANDITS_WAY_5_GOOMBA, identifier="EVENT_1707_set_action_script_109"),
	SetSyncActionScript(NPC_6, A0472_BANDITS_WAY_5_GOOMBA),
	SetSyncActionScript(NPC_7, A0472_BANDITS_WAY_5_GOOMBA),
	SetSyncActionScript(NPC_8, A0469_BANDITS_WAY_5_LOADER_BOSS),
	Return()
])
