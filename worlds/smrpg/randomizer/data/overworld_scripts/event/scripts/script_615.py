# E0615_MARRYMORE_LAMP
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
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_256_ret_0"]),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_615_run_dialog_49"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=16, silent=True),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=6)
	], identifier="EVENT_615_action_queue_5"),
	PaletteSet(palette_set=89, row=7, bit_0=True),
	Pause(60),
	FadeOutMusicToVolume(duration=2, volume=0),
	CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
	Pause(10),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
	PauseScriptUntilEffectDone(),
	SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	EnterArea(room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=SOUTH, x=8, y=13, z=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0),
	RestoreAllHP(),
	RestoreAllFP(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Pause(80),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(46),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(23),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(60),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	StopSound(),
	Pause(30),
	FadeOutMusicToVolume(duration=2, volume=96),
	CircleMaskShrinkToObject(target=MARIO, width=255, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	FadeOutMusicToVolume(duration=2, volume=96),
	PlaySound(sound=SO047_SNOOZE, channel=6),
	Pause(60),
	StopSound(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True)
	]),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	ApplyTileModToLevel(use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0),
	PauseActionScript(MARIO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_JumpToHeight(108),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_615_action_queue_45_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_615_action_queue_45_SUBSCRIPT_pause_3"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP, identifier="EVENT_615_clear_bit_46"),
	SetBit(TEMP_7042_5),
	Return(),
	RunDialog(dialog_id=DI0990_STAY_LONGER_IN_SUITE_INTRO, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_615_run_dialog_49"),
	RunDialog(dialog_id=DI0991_STAY_LONGER_IN_SUITE_PROMPT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_615_clear_bit_46"]),
	SetBit(TEMP_7042_6),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_615_set_bit_58"]),
	Inc(TEMP_70AC),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Jmp(["EVENT_615_action_queue_5"]),
	SetBit(MARRYMORE_UNKNOWN_709F_6, identifier="EVENT_615_set_bit_58"),
	SetVarToConst(TEMP_70AC, 199),
	Jmp(["EVENT_615_action_queue_5"])
])
