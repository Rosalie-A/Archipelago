# E1777_LANDS_END_CLIFF_LOADER
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
	SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
	SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
	SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_1777_ret_32"]),
	PlaySound(sound=SO123_CHAIN_RUMBLING_NOISE, channel=6),
	Pause(1),
	FadeOutSoundToVolume(duration=8, volume=0),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(4),
		A_WalkNorthSteps(22)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FASTER),
		A_TransferToXYZF(x=24, y=113, z=24, direction=SOUTHEAST),
		A_BounceToXYWithHeight(x=24, y=113, height=44),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(2),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=21, y=107, z=14, direction=EAST),
		A_BounceToXYWithHeight(x=21, y=107, height=14),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(4),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=23, y=110, z=18, direction=EAST),
		A_BounceToXYWithHeight(x=23, y=110, height=18),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(6),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=26, y=116, z=20, direction=EAST),
		A_BounceToXYWithHeight(x=26, y=116, height=20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(8),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=24, y=113, z=24, direction=EAST),
		A_BounceToXYWithHeight(x=24, y=113, height=24),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(10),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=22, y=108, z=24, direction=EAST),
		A_BounceToXYWithHeight(x=22, y=108, height=24),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(12),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=20, y=105, z=28, direction=EAST),
		A_BounceToXYWithHeight(x=20, y=105, height=28),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(14),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=21, y=107, z=31, direction=EAST),
		A_BounceToXYWithHeight(x=21, y=107, height=36),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(14),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=23, y=111, z=30, direction=EAST),
		A_BounceToXYWithHeight(x=23, y=111, height=30),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	SetVarToConst(TEMP_70AB, 21),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	SetBit(SKY_BRIDGE_PAN),
	SetVarToConst(TEMP_70AB, 29),
	StartLoopNTimes(7),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ActionQueueAsync(target=MEM_70AB, subscript=[
		A_SetVarToConst(TEMP_7034, 65535),
		A_UnknownCommand(bytearray(b'\xc7\x13')),
		A_AddConstToVar(X_COORD_1, 80),
		A_AddConstToVar(Z_COORD_1, 128),
		A_Pause(1, identifier="EVENT_1777_action_queue_26_SUBSCRIPT_pause_4"),
		A_CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1777_action_queue_26_SUBSCRIPT_pause_4"]),
		A_PlaySound(sound=SO134_SWIPE, channel=4),
		A_Pause(1),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetAllSpeeds(NORMAL),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_FixedFCoordOff()
	]),
	Dec(TEMP_70AB),
	EndLoop(),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(SKY_BRIDGE_PAN),
	Return(identifier="EVENT_1777_ret_32")
])
