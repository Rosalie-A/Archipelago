# E1712_BANDITS_WAY_2_DOG
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
	StopAllBackgroundEvents(),
	SetVarToConst(BATTLE_PACK_ID, 9),
	StartBattleWithPackAt700E(),
	ClearBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(3),
		A_JumpToHeight(height=0, silent=True)
	]),
	SetVarToConst(TEMP_70AB, 20),
	StartLoopNTimes(1),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1712_inc_16"]),
	JmpIfObjectNotInSpecificLevel(MEM_70AB, R207_BANDITS_WAY_AREA_02, ["EVENT_1712_action_queue_13"]),
	Jmp(["EVENT_1712_inc_16"]),
	ActionQueueAsync(target=MEM_70AB, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_UnknownCommand(bytearray(b'\xfd\x12')),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
		A_CompareVarToConst(PRIMARY_TEMP_700C, 14),
		A_JmpIfComparisonResultIsLesser(["EVENT_1712_action_queue_13_SUBSCRIPT_transfer_to_xyzf_9"]),
		A_TransferToXYZF(x=8, y=74, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNortheast(),
		A_Jmp(["EVENT_1712_action_queue_13_SUBSCRIPT_set_solidity_bits_12"]),
		A_TransferToXYZF(x=18, y=73, z=0, direction=EAST, identifier="EVENT_1712_action_queue_13_SUBSCRIPT_transfer_to_xyzf_9"),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True, identifier="EVENT_1712_action_queue_13_SUBSCRIPT_set_solidity_bits_12"),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	], identifier="EVENT_1712_action_queue_13"),
	SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	SummonObjectToSpecificLevel(MEM_70AB, R207_BANDITS_WAY_AREA_02),
	Inc(TEMP_70AB, identifier="EVENT_1712_inc_16"),
	EndLoop(),
	RunBackgroundEvent(event_id=E1705_BANDITS_WAY_2_DOGS_BACKGROUND, return_on_level_exit=True),
	Return()
])
