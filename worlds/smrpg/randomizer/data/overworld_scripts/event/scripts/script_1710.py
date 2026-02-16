# E1710_BANDITS_WAY_5_LOADER_BACKGROUND_BOSS_FIGHT
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
	JmpToSubroutine(["EVENT_1709_enable_controls_until_return_35"]),
	SetSyncActionScript(NPC_1, A0467_BANDITS_WAY_5_TROOPA_CHASE),
	SetSyncActionScript(NPC_2, A0467_BANDITS_WAY_5_TROOPA_CHASE),
	SetSyncActionScript(NPC_3, A0467_BANDITS_WAY_5_TROOPA_CHASE),
	SetSyncActionScript(NPC_4, A0467_BANDITS_WAY_5_TROOPA_CHASE),
	JmpToSubroutine(["EVENT_1709_action_queue_47"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNorthwest(),
		A_Pause(4),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(1),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_StartLoopNTimes(3),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(5),
		A_FaceSoutheast(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(5),
		A_FaceNorthwest(),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="bway_distracted_5")
	], identifier="bway_aqueue_5"),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_SetPriority(3),
		A_JumpToHeight(108),
		A_Walk1StepNortheast()
	]),
	Pause(23),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R206_BANDITS_WAY_AREA_05),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
    RunEventAsSubroutine(E1195_BANDITS_WAY_BOSS_UNLOCKS),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=6, y=88)
	]),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(30),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetPriority(3),
		A_VisibilityOn(),
		A_ShadowOff(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_1710_action_queue_34_SUBSCRIPT_pause_4"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_1710_action_queue_34_SUBSCRIPT_pause_4"]),
		A_ShadowOn(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(5),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_Pause(55)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_UnknownCommand(bytearray(b'\xc8\x80')),
		A_AddConstToVar(X_COORD_2, 65532),
		A_AddConstToVar(Y_COORD_2, 65520),
		A_WalkTo70167018(),
		A_SetWalkingSpeed(NORMAL),
		A_Jmp(["EVENT_1710_set_bit_38"]),
		A_WalkSouthSteps(6),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetBit(MUSHROOM_KINGDOM_OCCUPIED, identifier="EVENT_1710_set_bit_38"),
	SetBit(BANDITS_WAY_LIBERATED),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
