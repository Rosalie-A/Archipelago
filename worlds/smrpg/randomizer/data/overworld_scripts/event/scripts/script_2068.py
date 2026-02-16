# E2068_DOJO_BOSS_2
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
	ActionQueueSync(target=NPC_0, subscript=[
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
	RunEventAsSubroutine(E0862_DOJO_2ND_BOSS_CHALLENGE_SUBROUTINE),
	SetVarToConst(PRIMARY_TEMP_7000, 515),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(1),
	StopMusicFDA2(),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	Pause(1),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2068_fade_in_from_black_async_26"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2068_fade_in_from_black_async_26"]),
	SetBit(DOJO_BOSS_2_DEFEATED),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromSpecificLevel(NPC_0, R255_MONSTRO_TOWN_JINXS_DOJO),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToSpecificLevel(NPC_2, R255_MONSTRO_TOWN_JINXS_DOJO),
	RunEventAsSubroutine(E0863_DOJO_2ND_BOSS_CHALLENGE_DEESCALATE),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(1)
	]),
	Jmp(["EVENT_2068_action_queue_28"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2068_fade_in_from_black_async_26"),
	ActionQueueSync(target=NPC_0, subscript=[
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
	], identifier="EVENT_2068_action_queue_28"),
	UnfreezeCamera(),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2068_pause_34"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2068_pause_34"]),
	SetVarToConst(PRIMARY_TEMP_7000, 515),
	RunEventAsSubroutine(E1214_DOJO_2_BOSS_UNLOCKS),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Pause(30, identifier="EVENT_2068_pause_34"),
	Return()
])
