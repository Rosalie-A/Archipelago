# E1650_MOLEVILLE_LIBERATED_EXTERIOR_LOADER_CONTD
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
	StopMusic(),
	Pause(1),
	EnterArea(room_id=R338_MOLEVILLE_DYNA_AND_MITES_HOUSE, face_direction=SOUTHWEST, x=4, y=41, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_TransferXYZFSteps(x=0, y=0, z=20, direction=EAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=3, y=38, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=2, y=38, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(SLOW)
	]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(NPC_1, A0650_BLUE_CLOUD_MOVEMENT),
	FadeOutSoundToVolume(duration=0, volume=64),
	PlaySoundBalance(sound=SO019_LONG_FALL, balance=32),
	Pause(60),
	FadeOutSoundToVolume(duration=0, volume=127),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_StartLoopNTimes(5),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_EndLoop(),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthPixels(3),
		A_StartLoopNTimes(8),
		A_WalkNorthPixels(6),
		A_WalkSouthPixels(6),
		A_EndLoop(),
		A_WalkNorthPixels(3),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthPixels(2),
		A_StartLoopNTimes(10),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(4),
		A_EndLoop(),
		A_WalkNorthPixels(2)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=41, z=20, direction=EAST),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_ShadowOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1650_action_queue_15_SUBSCRIPT_pause_6"),
		A_JmpIfObjectInAir(NPC_3, ["EVENT_1650_action_queue_15_SUBSCRIPT_pause_6"]),
		A_JumpToHeight(104),
		A_SetAllSpeeds(NORMAL),
		A_WalkSouthwestSteps(5),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_ShadowOff(),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_1650_action_queue_16_SUBSCRIPT_pause_5"),
		A_JmpIfMarioInAir(["EVENT_1650_action_queue_16_SUBSCRIPT_pause_5"]),
		A_JumpToHeight(height=104, silent=True),
		A_Walk1StepNorth(),
		A_Pause(1, identifier="EVENT_1650_action_queue_16_SUBSCRIPT_pause_9"),
		A_JmpIfMarioInAir(["EVENT_1650_action_queue_16_SUBSCRIPT_pause_9"]),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(12),
		A_TransferToXYZF(x=5, y=40, z=20, direction=EAST),
		A_VisibilityOn(),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Walk1StepNortheast(),
		A_SetAllSpeeds(NORMAL),
		A_Pause(1, identifier="EVENT_1650_action_queue_17_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_2, ["EVENT_1650_action_queue_17_SUBSCRIPT_pause_8"]),
		A_JumpToHeight(133),
		A_Walk1StepNortheast(),
		A_Pause(1, identifier="EVENT_1650_action_queue_17_SUBSCRIPT_pause_12"),
		A_JmpIfObjectInAir(NPC_2, ["EVENT_1650_action_queue_17_SUBSCRIPT_pause_12"]),
		A_JumpToHeight(125),
		A_WalkSoutheastSteps(2),
		A_Pause(1, identifier="EVENT_1650_action_queue_17_SUBSCRIPT_pause_16"),
		A_JmpIfObjectInAir(NPC_2, ["EVENT_1650_action_queue_17_SUBSCRIPT_pause_16"]),
		A_JumpToHeight(116),
		A_WalkSouthwestSteps(2),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Pause(20),
	SetVarToConst(TEMP_7034, 2),
	SetVarToConst(X_COORD_1, 2304),
	SetVarToConst(Y_COORD_1, 5376),
	SetVarToConst(Z_COORD_1, 256),
	StartLoopNTimes(23),
	Pause(1, identifier="EVENT_1650_pause_24"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1650_pause_24"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	AddConstToVar(Z_COORD_1, 112),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceEast(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(3),
		A_FaceNortheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FAST),
		A_WalkEastSteps(2),
		A_FixedFCoordOff(),
		A_Walk1StepSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetAsyncActionScript(NPC_2, A0650_BLUE_CLOUD_MOVEMENT),
	PauseScriptUntilEffectDone(),
	SetBit(OPTIONAL_MINECART_CLEARED),
	SetBit(TEMP_7042_1),
	SetSyncActionScript(NPC_0, A0160_SEQUENCE_LOOPING_ON),
	SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
	SetSyncActionScript(NPC_2, A0160_SEQUENCE_LOOPING_ON),
	Return()
])
