# E1368_CURTAIN_GAME_SUCCESS_2
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
	StopMusicFDA2(identifier="EVENT_1368_stop_music_FDA2_0"),
	EnableControlsUntilReturn([]),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(10),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(10),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(10),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(8),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(13),
		A_Pause(15),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, identifier="tower_henchman_curtain_39"),
		A_Pause(7),
		A_SetSpriteSequence(index=15, is_sequence=True, looping=True, identifier="tower_henchman_curtain_40")
	], identifier="tower_henchman_curtain_aqueue_39"),
	PlayMusicAtDefaultVolume(M0032_ANDMYNAME_SBOOSTER),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=41),
	Pause(3),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=42),
	Pause(3),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	Pause(5),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(25),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SequenceLoopingOn(),
		A_FixedFCoordOn(),
		A_JumpToHeight(112),
		A_WalkSoutheastSteps(3),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(5),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestPixels(8),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(5),
		A_WalkNortheastSteps(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	Pause(20),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(80),
		A_Pause(20)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(80),
		A_Pause(20)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_JumpToHeight(80),
		A_Pause(20)
	]),
	Pause(1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_BounceToXYWithHeight(x=3, y=20, height=0),
		A_FaceNorth(),
		A_Pause(80),
		A_FaceEast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestPixels(6),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW),
		A_Pause(25),
		A_SequenceLoopingOff(),
		A_Pause(10),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_Pause(30),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="tower_boss_laughing_seq_2"),
		A_Pause(30),
		A_ResetProperties()
	], identifier="tower_boss_laughing_aqueue_2"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkNortheastPixels(6),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest()
	]),
	Pause(1),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True, mirror_sprite=True, identifier="tower_boss_crying_1")
	], identifier="tower_boss_crying_aq_1"),
	SetSyncActionScript(NPC_1, A0579_CURTAIN_GAME_HENCHMAN_SPIN),
	SetSyncActionScript(NPC_2, A0580_CURTAIN_GAME_HENCHMAN_SPIN),
	SetSyncActionScript(NPC_3, A0578_CURTAIN_GAME_HENCHMAN_SPIN),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_BounceToXYWithHeight(x=3, y=16, height=0),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast()
	]),
	Pause(1),
	Set7000ToTappedButton(identifier="EVENT_1368_set_7000_to_tapped_button_49"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1368_action_queue_54"]),
	Jmp(["EVENT_1368_set_7000_to_tapped_button_49"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(112),
		A_Pause(60),
		A_SetSequenceSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetPriority(2)
	], identifier="EVENT_1368_action_queue_54"),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(8),
		A_SetWalkingSpeed(FAST),
		A_FloatingOn(),
		A_ShadowOff(),
		A_JumpToHeight(height=64, silent=True),
		A_WalkSoutheastSteps(3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(8),
		A_SetWalkingSpeed(FAST),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=6),
		A_WalkNorthPixels(7),
		A_WalkSouthPixels(7),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(4)
	]),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(60),
		A_JumpToHeight(64),
		A_Pause(30)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=6),
		A_WalkNorthwestSteps(3)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_Pause(12),
		A_SetWalkingSpeed(VERY_FAST),
		A_JumpToHeight(32),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_WalkSouthwestSteps(2)
	]),
	Pause(20),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Pause(45),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(3),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestSteps(6)
	]),
	Pause(20),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestSteps(3)
	]),
	Pause(45),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(20),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(10),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_Pause(45)
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=1),
	SetBit(CURTAIN_MINIGAME_COMPLETED),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	JmpIfBitClear(ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_1368_summon_to_level_94"]),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	SetBit(TOWER_BOSS_1_STAR_PIECE),
	RunEventAsSubroutine(E1201_TOWER_CURTAIN_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(),
	SummonObjectToSpecificLevel(NPC_7, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, identifier="EVENT_1368_summon_to_level_94"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOn(),
		A_FaceNorthwest(),
		A_ShiftToXYCoords(x=5, y=29)
	]),
	Return()
])
