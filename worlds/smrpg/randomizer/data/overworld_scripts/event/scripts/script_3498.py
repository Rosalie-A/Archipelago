# E3498_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_BACKGROUND
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
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["EVENT_3498_action_queue_3"]),
	SetSyncActionScript(NPC_4, A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
	Jmp(["EVENT_3498_action_queue_5"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	], identifier="EVENT_3498_action_queue_3"),
	SetSyncActionScript(NPC_0, A0045_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_PATH),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(128),
		A_Walk1StepSouthwest(),
		A_Pause(12),
		A_FloatingOff()
	], identifier="EVENT_3498_action_queue_5"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FixedFCoordOn(),
		A_SetAllSpeeds(NORMAL),
		A_JumpToHeight(64),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(4),
		A_WalkWestPixels(8),
		A_WalkEastPixels(8),
		A_WalkWestPixels(8),
		A_WalkEastPixels(8),
		A_WalkWestPixels(4),
		A_FaceSoutheast()
	]),
	SetVarToConst(PRIMARY_TEMP_700C, 0),
	StartLoopNTimes(7),
	CreatePacketAtObjectCoords(packet=P017_SMALL_MINIGAME_COIN, target_npc=NPC_1, destinations=["EVENT_3498_pause_11"]),
	Pause(1, identifier="EVENT_3498_pause_11"),
	Inc(PRIMARY_TEMP_700C),
	EndLoop(),
	Pause(30),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3498_action_queue_18"]),
	SetBit(TEMP_7043_1),
	Jmp(["EVENT_3498_action_queue_5"]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(9),
		A_FaceSoutheast()
	], identifier="EVENT_3498_action_queue_18"),
	Pause(180),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_JumpToHeight(0),
		A_Pause(13),
		A_FloatingOff()
	], identifier="EVENT_3498_action_queue_20"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_BounceToXYWithHeight(x=5, y=90, height=9)
	]),
	SetVarToConst(PRIMARY_TEMP_700C, 0),
	StartLoopNTimes(7),
	CreatePacketAtObjectCoords(packet=P017_SMALL_MINIGAME_COIN, target_npc=NPC_3, destinations=["EVENT_3498_pause_26"]),
	Pause(1, identifier="EVENT_3498_pause_26"),
	Inc(PRIMARY_TEMP_700C),
	EndLoop(),
	Pause(20),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3498_ret_37"]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkWestSteps(2)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=3, y=90, z=8, direction=EAST),
		A_JumpToHeight(0)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(7),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(88),
		A_WalkEastSteps(2),
		A_PlaySound(sound=SO065_THWOMP_STOMP, channel=4),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ShiftZDownPixels(8)
	]),
	SetBit(TEMP_7043_2),
	Jmp(["EVENT_3498_action_queue_20"]),
	Return(identifier="EVENT_3498_ret_37")
])
