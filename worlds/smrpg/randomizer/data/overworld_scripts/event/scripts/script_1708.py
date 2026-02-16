# E1708_BANDITS_WAY_5_LOADER
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
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1708_jmp_if_bit_clear_3"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_1708_jmp_if_bit_clear_3"]),
	SetVarToConst(TIMER_7022, 30),
	JmpIfBitClear(BANDITS_WAY_LIBERATED, ["EVENT_1708_jmp_if_bit_clear_9"], identifier="EVENT_1708_jmp_if_bit_clear_3"),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	ActionQueueSync(target=NPC_9, subscript=[
		A_VisibilityOn(),
		A_JumpToHeight(0),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_1708_jmp_if_bit_clear_16"], identifier="EVENT_1708_jmp_if_bit_clear_9"),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_5_VIEWED, ["EVENT_1708_set_bit_22"], identifier="EVENT_1708_jmp_if_bit_clear_16"),
	RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	JmpToSubroutine(["EVENT_1708_action_queue_34"]),
	RunBackgroundEvent(event_id=E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2, return_on_level_exit=True),
	Return(),
	SetBit(BANDITS_WAY_CUTSCENE_5_VIEWED, identifier="EVENT_1708_set_bit_22"),
	RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
	ActionQueueSync(target=NPC_8, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="bway_distracted_4")
	], identifier="bway_aqueue_4"),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(20),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(3),
		A_WalkSouthSteps(11),
		A_WalkSoutheastSteps(4),
		A_SetAllSpeeds(FASTEST),
		A_StartLoopNTimes(1),
		A_WalkSoutheastSteps(4),
		A_WalkSouthSteps(2),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(8),
		A_WalkNorthwestSteps(8),
		A_WalkNorthSteps(2),
		A_WalkNortheastSteps(8),
		A_EndLoop()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepEast(),
		A_WalkSouthSteps(7),
		A_WalkSoutheastSteps(8),
		A_WalkSouthSteps(6),
		A_Pause(80),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(13),
		A_WalkNorthwestSteps(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	StopEmbeddedActionScript(NPC_8),
	JmpToSubroutine(["EVENT_1708_action_queue_34"]),
	RunBackgroundEvent(event_id=E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2, return_on_level_exit=True),
	Return(),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=10, y=90, z=0, direction=EAST),
		A_FaceNortheast()
	], identifier="EVENT_1708_action_queue_34"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=14, y=102, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	SetBit(TEMP_7044_2),
	ClearBit(TEMP_7043_7),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=11, y=115, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=98, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_5, A0472_BANDITS_WAY_5_GOOMBA),
	SetSyncActionScript(NPC_6, A0472_BANDITS_WAY_5_GOOMBA),
	SetSyncActionScript(NPC_7, A0472_BANDITS_WAY_5_GOOMBA),
	SetSyncActionScript(NPC_8, A0469_BANDITS_WAY_5_LOADER_BOSS),
	Return()
])
