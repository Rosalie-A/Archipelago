# E2077_DOJO_BOSS_4
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
	JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2077_run_dialog_40"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=16),
		A_FaceNortheast()
	]),
	Pause(30),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkSouthwestSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(15),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(30)
	]),
	RunEventAsSubroutine(E0866_DOJO_4TH_BOSS_CHALLENGE_SUBROUTINE),
	SetVarToConst(PRIMARY_TEMP_7000, 517),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(1),
	StopMusicFDA2(),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	Pause(1),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(1),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	Pause(30),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2077_ret_41"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2077_ret_41"]),
	Pause(3),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(4),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(1),
		A_VisibilityOff(),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_Pause(1),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_Pause(1),
		A_PlaySound(sound=SO058_INSERT, channel=6),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(1),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(1),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_VisibilityOn(),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(1),
		A_WalkToXYCoords(x=6, y=16),
		A_StopSound(),
		A_FaceSouthwest()
	]),
	Pause(1),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOn(),
		A_ShadowOn(),
		A_StopSound(),
		A_StopSound(),
		A_ShadowOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=14),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(1),
	Pause(1),
	SetSyncActionScript(NPC_3, A1006_DOJO_PERMA_JUMP),
	SetSyncActionScript(NPC_1, A1006_DOJO_PERMA_JUMP),
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=32),
	SetBit(DOJO_BOSS_4_DEFEATED),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunEventAsSubroutine(E1216_DOJO_4_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 517),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	Return(),
	RunDialog(dialog_id=DI3353_DOJO_BOSS_2_FULLY_DEFEATED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2077_run_dialog_40"),
	Return(identifier="EVENT_2077_ret_41")
])
