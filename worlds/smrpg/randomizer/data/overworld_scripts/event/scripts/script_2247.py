# E2247_DOJO_BOSS_5 
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
	ActionQueueSync(target=NPC_4, subscript=[
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
    RunEventAsSubroutine(E0867_DOJO_5TH_BOSS_CHALLENGE_SUBROUTINE),
	SetVarToConst(PRIMARY_TEMP_7000, 525),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(1),
	StopMusicFDA2(),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	Pause(1),
    RunEventAsSubroutine(E0868_DOJO_5TH_BOSS_CHALLENGE_DEESCALATE),
    FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_4, subscript=[
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
	JmpIfBitSet(RUN_AWAY, ["EVENT_2247_fade_in_from_black_async_26"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2247_fade_in_from_black_async_26"]),
    SetBit(DOJO_POSTGAME_COMPLETED),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	FadeOutToBlack(sync=False, identifier="EVENT_167_ret_87_dojo_postgame"),
    RemoveObjectFromCurrentLevel(NPC_4),
    SummonObjectToCurrentLevel(NPC_3),
    EnterArea(R255_MONSTRO_TOWN_JINXS_DOJO, face_direction=NORTHEAST, x=5, y=16, z=0, run_entrance_event=True),
	RunEventAsSubroutine(E1217_DOJO_5_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 525),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Pause(30, identifier="EVENT_2247_fade_in_from_black_async_26"),
	Return()
])
