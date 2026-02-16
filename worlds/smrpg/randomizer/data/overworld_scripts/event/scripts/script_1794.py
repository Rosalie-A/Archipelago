# E1794_LANDS_END_BUY_CHEST
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitSet(TEMP_7076_0, ["EVENT_1794_action_queue_71"]),
	JmpIfBitSet(LANDS_END_CHEST_1_USED, ["EVENT_1794_jmp_if_bit_set_22"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 400),
	JmpIfComparisonResultIsLesser(["EVENT_1794_run_dialog_66"]),
	RunDialog(dialog_id=DI1223_SHAMAN_SALESMAN_400_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1794_pause_19"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_SLOW)
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 400),
	Dec7000FromCoins(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	SetVarToConst(TEMP_70AA, 38),
	JmpToSubroutine(["EVENT_1794_action_queue_51"]),
	SetBit(LANDS_END_CHEST_1_PAID),
	Return(),
	Pause(10, identifier="EVENT_1794_pause_19"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(),
	JmpIfBitSet(LANDS_END_CHEST_2_REQUESTED, ["EVENT_1794_store_coin_amount_7000_32"], identifier="EVENT_1794_jmp_if_bit_set_22"),
	RunDialog(dialog_id=DI1224_SHAMAN_SALESMAN_2ND_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1794_pause_19"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1226_SHAMAN_SALESMAN_LEAVES, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(LANDS_END_CHEST_2_REQUESTED),
	JmpToSubroutine(["EVENT_1794_set_var_to_const_68"]),
	RemoveObjectFromSpecificLevel(NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	Return(),
	StoreCoinCountTo7000(identifier="EVENT_1794_store_coin_amount_7000_32"),
	CompareVarToConst(PRIMARY_TEMP_7000, 800),
	JmpIfComparisonResultIsLesser(["EVENT_1794_run_dialog_66"]),
	RunDialog(dialog_id=DI1227_SHAMAN_SALESMAN_800_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1794_clear_bit_49"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_SLOW)
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 800),
	Dec7000FromCoins(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	SetVarToConst(TEMP_70AA, 39),
	JmpToSubroutine(["EVENT_1794_action_queue_51"]),
	SetBit(LANDS_END_CHEST_2_PAID),
	ClearBit(LANDS_END_CHEST_2_REQUESTED),
	RemoveObjectFromSpecificLevel(NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	Return(),
	ClearBit(LANDS_END_CHEST_2_REQUESTED, identifier="EVENT_1794_clear_bit_49"),
	Jmp(["EVENT_1794_pause_19"]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(112),
		A_StartLoopNTimes(11),
		A_TurnClockwise45DegreesNTimes(6),
		A_Pause(1),
		A_EndLoop()
	], identifier="EVENT_1794_action_queue_51"),
	Pause(20),
	SetVarToConst(TEMP_7034, 6),
	Set70107015ToObjectXYZ(target=MEM_70AA),
	PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=6),
	StartLoopNTimes(8),
	Pause(1, identifier="EVENT_1794_pause_57"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1794_pause_57"]),
	Pause(5),
	AddConstToVar(TEMP_7034, 3),
	AddConstToVar(Z_COORD_1, 64),
	EndLoop(),
	ActionQueueAsync(target=MEM_70AA, subscript=[
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(8),
		A_EndLoop()
	]),
	SetSyncActionScript(MEM_70AA, A0014_FLOATING_CHEST),
	Jmp(["EVENT_1794_set_var_to_const_68"]),
	RunDialog(dialog_id=DI1222_SHAMAN_SALESMAN_NOT_ENOUGH_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1794_run_dialog_66"),
	Return(),
	SetVarToConst(TEMP_70AA, 36, identifier="EVENT_1794_set_var_to_const_68"),
	ActionQueueAsync(target=MEM_70AA, subscript=[
		A_PlaySound(sound=SO059_HOVERING_FROGFUCIUS, channel=4),
		A_SequencePlaybackOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(SLOW),
		A_ShiftZUpSteps(2),
		A_StartLoopNTimes(3),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(6),
		A_VisibilityOff(),
		A_EndLoop(),
		A_Pause(1, identifier="EVENT_1794_action_queue_69_SUBSCRIPT_pause_11"),
		A_SetVarToConst(TEMP_7034, 65535),
		A_CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=MEM_70AA, destinations=["EVENT_1794_action_queue_69_SUBSCRIPT_pause_11"]),
		A_PlaySound(sound=SO161_GHOST, channel=4)
	], identifier="EVENT_1794_action_queue_69"),
	Return(),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_JumpToHeight(128),
		A_StartLoopNTimes(11),
		A_Pause(4),
		A_TurnClockwise45DegreesNTimes(2),
		A_EndLoop(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True)
	], identifier="EVENT_1794_action_queue_71"),
	Return()
])
