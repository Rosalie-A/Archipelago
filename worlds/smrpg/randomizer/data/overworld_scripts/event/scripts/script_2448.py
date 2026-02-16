# E2448_FOREST_BOSS_FIGHT
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
	JmpIfBitSet(FOREST_LIBERATED, ["EVENT_2448_ret_77"]),
	ClearBit(DIRECTIONAL_7045_0),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	ClearBit(DIRECTIONAL_7045_5),
	ClearBit(DIRECTIONAL_7045_6),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	ClearBit(DIRECTIONAL_7046_1),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNorthwestSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthwestSteps(10)
	]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, ["EVENT_2448_pause_28"]),
	SetSyncActionScript(NPC_0, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_20"),
	SetSyncActionScript(NPC_5, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_25"),
	SetSyncActionScript(NPC_1, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_21"),
	SetSyncActionScript(NPC_6, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_26"),
	SetSyncActionScript(NPC_2, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_22"),
	SetSyncActionScript(NPC_7, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_27"),
	SetSyncActionScript(NPC_3, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_23"),
	SetSyncActionScript(NPC_8, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_28"),
	SetSyncActionScript(NPC_4, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_24"),
	SetSyncActionScript(NPC_9, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP, identifier="forest_henchman_29"),
	RunBackgroundEvent(event_id=E2446_FOREST_BOSS_HENCHMEN_BOUNCE, return_on_level_exit=True, identifier="forest_henchmen_bounce_30"),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetPriority(3),
		A_SetSequenceSpeed(FASTER)
	]),
	Pause(180, identifier="EVENT_2448_pause_28"),
	SetBit(TEMP_7043_0),
	StopAllBackgroundEvents(),
	Pause(16),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FaceSoutheast(),
		A_Pause(16),
		A_SequenceLoopingOff()
	]),
	Pause(112),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=10, y=29, z=0, direction=SOUTHEAST),
		A_VisibilityOn(),
		A_SequencePlaybackOff(),
		A_FloatingOn(),
		A_JumpToHeight(height=1, silent=True),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True, identifier="forest_character_animation_13"),
		A_Pause(1, identifier="EVENT_2448_action_queue_35_SUBSCRIPT_pause_6"),
		A_JmpIfObjectInAir(NPC_10, ["EVENT_2448_action_queue_35_SUBSCRIPT_pause_6"]),
		A_PlaySound(sound=SO058_INSERT, channel=6),
		A_Pause(8),
		A_SequencePlaybackOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=17, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="forest_character_animation_11")
	], identifier="forest_character_animation_14"),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(FASTER),
		A_SequenceLoopingOn()
	]),
    Pause(90),
	RunEventAsSubroutine(E1226_FOREST_MAZE_CHARACTER),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2448_set_bit_43"]),
	ResetAndChooseGame(),
	SetBit(FOREST_LIBERATED, identifier="EVENT_2448_set_bit_43"),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_11),
	RemoveObjectFromSpecificLevel(NPC_0, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_1, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_2, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_3, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_4, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_5, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_6, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_7, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_8, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_9, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_10, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_11, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_11, R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09),
	RemoveObjectFromSpecificLevel(NPC_1, R228_FOREST_MAZE_AREA_04),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_TransferToObjectXYZ(NPC_10)
	]),
	FadeInFromBlack(sync=False),
	RestoreAllHP(),
	RestoreAllFP(),
	PlayMusicAtDefaultVolume(M0026_FORESTMAZE),
	UnfreezeCamera(),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsLesser(["EVENT_2448_j_24"]),
	SetBit(SWITCH_MENU_UNLOCKED),
    RunEventAsSubroutine(E1198_FOREST_MAZE_BOSS_UNLOCKS, identifier="EVENT_2448_j_24"),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2448_ret_77")
])
