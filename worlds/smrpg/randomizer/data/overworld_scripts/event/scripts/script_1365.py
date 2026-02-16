# E1365_CURTAIN_GAME_BUSINESS_LOGIC_1
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
	PlayMusicAtDefaultVolume(M0047_GRATEGUY_SCASINO, identifier="EVENT_1365_play_music_default_volume_0"),
	Pause(30),
	PlaySound(sound=SO107_DRUM_ROLL, channel=4),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_WalkNorthwestSteps(1),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_1")
	], identifier="tower_henchman_curtain_aqueue_1"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	StartLoopNTimes(89),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1365_move_script_to_main_thread_112"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	Pause(3),
	PauseActionScript(NPC_1),
	PlaySound(sound=SO107_DRUM_ROLL, channel=4),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_FaceNortheast(),
		A_Pause(25),
		A_WalkNortheastSteps(2),
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_2")
	], identifier="tower_henchman_curtain_aqueue_2"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	StartLoopNTimes(89),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1365_move_script_to_main_thread_112"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	Pause(3),
	PauseActionScript(NPC_1),
	PlaySound(sound=SO107_DRUM_ROLL, channel=4),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(4),
		A_FaceNorthwest(),
		A_Pause(25),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_3")
	], identifier="tower_henchman_curtain_aqueue_3"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	StartLoopNTimes(59),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1365_move_script_to_main_thread_112"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	Pause(3),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_4")
	], identifier="tower_henchman_curtain_aqueue_4"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35),
	StartLoopNTimes(29),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1365_move_script_to_main_thread_112"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=32),
	Pause(3),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_Pause(10),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(6),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_5")
	], identifier="tower_henchman_curtain_aqueue_5"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	StartLoopNTimes(39),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1365_move_script_to_main_thread_112"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	Pause(3),
	Pause(45),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	Jmp(["EVENT_1366_pause_action_script_0"]),
	MoveScriptToMainThread(identifier="EVENT_1365_move_script_to_main_thread_112"),
	EnableControlsUntilReturn([]),
	StopMusicFDA2(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(10),
		A_JumpToHeight(50)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(10),
		A_JumpToHeight(50)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(10),
		A_JumpToHeight(50)
	]),
	Jmp(["EVENT_1370_play_sound_1"]),
	Return()
])
