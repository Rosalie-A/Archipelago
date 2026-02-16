# E1147_SEASIDE_INITIATE_BOSS_FIGHT_ANIMATION
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
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_PlaySound(sound=SO089_LIT_FUSE, channel=6),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	PlaySound(sound=SO148_SURGING_ELECTRICITY, channel=6),
	FadeOutMusicToVolume(duration=8, volume=0),
	PaletteSetMorphs(palette_type=NOTHING, duration=2, palette_set=214, row=11),
	Pause(60),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_1"),
	Pause(20),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_2"),
	Pause(10),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_3"),
	Pause(10),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_4"),
	Pause(10),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_5"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=26, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_7, A0527_SEASIDE_BOSS_TRANSFORM),
	Pause(7),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_6"),
	Pause(7),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_7"),
	SetSyncActionScript(NPC_6, A0527_SEASIDE_BOSS_TRANSFORM),
	Pause(10),
	StartLoopNTimes(6),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_8"),
	Pause(5),
	EndLoop(),
	RemoveObjectFromCurrentLevel(NPC_6),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOn(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False, mirror_sprite=True, identifier="seaside_boss_reveal_sequence_1"),
	], identifier="seaside_boss_reveal_sequence"),
	PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=6),
	Pause(8),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_9"),
	Pause(10),
	ScreenFlashesWithColour(WHITE, identifier="screenflash_10"),
	Pause(45),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_1147_play_music_default_volume_42"]),
	ResetAndChooseGame(),
	PlayMusicAtDefaultVolume(M0005_SEASIDETOWN, identifier="EVENT_1147_play_music_default_volume_42"),
	EnterArea(room_id=R316_SEASIDE_TOWN_BEACH, face_direction=NORTHWEST, x=8, y=30, z=0),
	SetBit(SEASIDE_LIBERATED),
	RemoveObjectFromSpecificLevel(NPC_0, R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP),
	RemoveObjectFromSpecificLevel(NPC_1, R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=8)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=4, y=22)
	]),
	RunEventAsSubroutine(E1163_SEASIDE_LIBERATED_BEACH),
	PauseScriptUntilEffectDone(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E1206_SEASIDE_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
