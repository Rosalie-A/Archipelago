# E2209_KEEP_1ST_BOSS_FIGHT
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
	Pause(30, identifier="EVENT_2209_pause_0"),
	FadeOutMusicToVolume(duration=7, volume=0),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkNortheastSteps(4)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=25, y=101),
		A_FaceSouthwest(),
		A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop(),
		A_VisibilityOn()
	]),
	Pause(15),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=False, identifier="keep_boss_1_animation")
	], identifier="keep_boss_1_animation_aq"),
	Pause(80, identifier="keep_boss_1_animation_pause"),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2209_fade_in_from_black_async_10"]),
	ResetAndChooseGame(),
	FadeInFromBlack(sync=False, identifier="EVENT_2209_fade_in_from_black_async_10"),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=138, row=11, identifier="kamek_palette"),
	RunEventAsSubroutine(E0942_KEEP_FIRST_BOSS_SUMMON_CHEST),
	PaletteSet(palette_set=139, row=1, bit_0=True, bit_3=True, identifier="infinite_coin_chest_palette"),
	SetSyncActionScript(NPC_0, A0014_FLOATING_CHEST),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6, identifier="infinite_coin_chest_sfx"),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop(),
		A_VisibilityOn()
	], identifier="infinite_coin_chest_aq"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(3),
		A_FaceSoutheast(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn()
	]),
	SetBit(KEEP_BOSS_1_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E1236_KEEP_1_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
