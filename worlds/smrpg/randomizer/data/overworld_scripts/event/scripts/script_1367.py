# E1367_CURTAIN_GAME_SUCCESS_1
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
	PauseActionScript(NPC_1, identifier="EVENT_1367_pause_action_script_0"),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_WalkNorthwestSteps(1),
		A_Pause(15)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_21")
	], identifier="tower_henchman_curtain_aqueue_21"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_22")
	], identifier="tower_henchman_curtain_aqueue_22"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_23")
	], identifier="tower_henchman_curtain_aqueue_23"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	StartLoopNTimes(49),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	Pause(3),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_24")
	], identifier="tower_henchman_curtain_aqueue_24"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_25")
	], identifier="tower_henchman_curtain_aqueue_25"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_26")
	], identifier="tower_henchman_curtain_aqueue_26"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	StartLoopNTimes(39),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	Pause(3),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest(),
		A_Pause(20)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_27")
	], identifier="tower_henchman_curtain_aqueue_27"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_28")
	], identifier="tower_henchman_curtain_aqueue_28"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_29")
	], identifier="tower_henchman_curtain_aqueue_29"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	StartLoopNTimes(29),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	Pause(3),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_2, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest(),
		A_Pause(20)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_30")
	], identifier="tower_henchman_curtain_aqueue_30"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_31")
	], identifier="tower_henchman_curtain_aqueue_31"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_32")
	], identifier="tower_henchman_curtain_aqueue_32"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	StartLoopNTimes(29),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	Pause(3),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest(),
		A_Pause(20)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_WalkNortheastSteps(2),
		A_Pause(5),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_33")
	], identifier="tower_henchman_curtain_aqueue_33"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_Pause(5),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_34")
	], identifier="tower_henchman_curtain_aqueue_34"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_Pause(5),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_35")
	], identifier="tower_henchman_curtain_aqueue_35"),
	Pause(20),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	StartLoopNTimes(9),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	StartLoopNTimes(9),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	StartLoopNTimes(29),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	Pause(3),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ck')),
		A_ResetProperties(),
		A_Pause(40),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(4),
		A_WalkNorthwestSteps(1),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_36")
	], identifier="tower_henchman_curtain_aqueue_36"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Pause(40),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSouthwestSteps(4),
		A_WalkNortheastSteps(4),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(1),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(1),
		A_FaceNorthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_37")
	], identifier="tower_henchman_curtain_aqueue_37"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_Pause(40),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(3),
		A_JumpToHeight(112),
		A_WalkSouthwestSteps(6),
		A_WalkNorthwestSteps(3),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="tower_henchman_curtain_38")
	], identifier="tower_henchman_curtain_aqueue_38"),
	Pause(20),
	SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
	PlaySound(sound=SO090_CURTAIN, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=45),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=34),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35),
	StartLoopNTimes(39),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
	Pause(1),
	EndLoop(),
	EnableControlsUntilReturn([]),
	Jmp(["EVENT_1368_stop_music_FDA2_0"]),
	StopMusicFDA2(identifier="EVENT_1367_stop_music_FDA2_273"),
	MoveScriptToMainThread(),
	EnableControlsUntilReturn([]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(10),
		A_JumpToHeight(50)
	]),
	Jmp(["EVENT_1370_play_sound_1"])
])
