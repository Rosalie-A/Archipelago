# E1395_MARIOS_HOUSE_LAMP
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
	MoveScriptToMainThread(),
	SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceNortheast(),
		A_Pause(5),
		A_FaceNorth(),
		A_JumpToHeight(height=35, silent=True),
		A_Pause(10),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4)
	]),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=112, green=104, blue=16, speed=0),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB]),
	FadeOutMusicToVolume(duration=4, volume=0),
	RemoveObjectFromCurrentLevel(NPC_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(15),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(32),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(120),
		A_WalkNorthwestPixels(32)
	]),
	SummonObjectToCurrentLevel(NPC_0),
	Pause(5),
	CircleMaskShrinkToObject(target=NPC_2, width=0, speed=3, static=True),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(110),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=0, green=0, blue=0, speed=0),
	ResetPrioritySet(),
	ApplyTileModToLevel(use_alternate=True, room_id=R189_MARIOS_PIPEHOUSE, mod_id=32),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(30),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(16),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	CircleMaskShrinkToObject(target=NPC_2, width=35, speed=3, static=True),
	Pause(30),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(10),
	PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL)
	]),
	FadeOutMusicToVolume(duration=6, volume=100),
	Set7000ToTappedButton(identifier="EVENT_1395_set_7000_to_tapped_button_31"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1395_apply_tile_mod_36"]),
	Jmp(["EVENT_1395_set_7000_to_tapped_button_31"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R189_MARIOS_PIPEHOUSE, mod_id=32, identifier="EVENT_1395_apply_tile_mod_36"),
	CircleMaskShrinkToObject(target=MARIO, width=153, speed=5, static=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(120),
		A_WalkSouthPixels(32),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(1),
	PlaySound(sound=SO058_INSERT, channel=6),
	ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	Return()
])
