# E2225_KEEP_2ND_BOSS
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
	JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["EVENT_2225_ret_20"]),
	JmpIfBitSet(KEEP_BOSS_2_DEFEATED, ["EVENT_2225_jmp_to_event_19"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(1),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(11)
	]),
	Pause(60),
	Pause(15),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=12, y=46, z=0, direction=EAST),
		A_Pause(1),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xe0\xfd\x00\xff')),
		A_UnknownCommand(bytearray(b'%\x00\r\x80\xff')),
		A_Pause(44),
		A_BPL262728(),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunEventAsSubroutine(E0943_KEEP_SECOND_BOSS_ANIMATION_SUBROUTINE),
	FadeOutMusicToVolume(duration=0, volume=0),
	SetVarToConst(PRIMARY_TEMP_7000, 521),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_2225_restore_all_hp_14"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2225_restore_all_hp_14"),
	RestoreAllFP(),
	SetBit(KEEP_BOSS_2_DEFEATED),
	SetVarToConst(PRIMARY_TEMP_7000, 521),
	RunEventAsSubroutine(E1237_KEEP_CHANDELIER_BOSS_UNLOCKS),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	JmpToEvent(E2226_KEEP_3RD_BOSS, identifier="EVENT_2225_jmp_to_event_19"),
	Return(identifier="EVENT_2225_ret_20")
])
