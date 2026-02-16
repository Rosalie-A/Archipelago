# E1702_BANDITS_WAY_2_LOADER
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
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkWestPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkWestPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(24),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetSyncActionScript(NPC_7, A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC),
	SetVarToConst(SECONDARY_TEMP_7024, 128),
	SetVarToConst(ROSE_WAY_703E, 26),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_2_VIEWED, ["EVENT_1702_set_bit_14"]),
	RunEventAsSubroutine(E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	SetBit(BANDITS_WAY_CUTSCENE_2_VIEWED, identifier="EVENT_1702_set_bit_14"),
	RunEventAsSubroutine(E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=NPC_8, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="bway_distracted_2")
	], identifier="bway_aqueue_2"),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest()
	]),
	FreezeAllNPCsUntilReturn(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetSolidityBits(bit_7=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(2),
		A_Walk1StepSoutheast(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(13),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(144),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(16),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_Pause(10),
		A_WalkEastPixels(50),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(80),
		A_WalkEastPixels(40),
		A_Pause(1, identifier="EVENT_1702_action_queue_22_SUBSCRIPT_pause_20"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_1702_action_queue_22_SUBSCRIPT_pause_20"]),
		A_SetAllSpeeds(FAST),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(128),
		A_WalkEastSteps(4),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(140),
		A_ClearSolidityBits(cant_jump_through=True),
		A_PlaySound(sound=SO013_COIN, channel=4),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_Pause(28),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(5),
		A_Pause(20),
		A_WalkEastSteps(4),
		A_Pause(80),
		A_WalkWestSteps(4),
		A_WalkSouthwestSteps(5),
		A_SetWalkingSpeed(VERY_FAST)
	]),
	UnfreezeAllNPCs(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ClearSolidityBits(bit_7=True)
	]),
	Return()
])
