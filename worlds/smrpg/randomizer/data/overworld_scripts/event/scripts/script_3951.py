# E3951_STAR_PIECE_CREDITS_INIT
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
	EnterArea(room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, face_direction=NORTHWEST, x=4, y=48, z=0),
	RunStarPieceSequence(8),
	PaletteSet(palette_set=163, row=1, bit_3=True),
	PaletteSet(palette_set=164, row=1, bit_0=True, bit_3=True),
	PaletteSet(palette_set=166, row=1, bit_1=True, bit_3=True),
	PaletteSet(palette_set=167, row=1, bit_0=True, bit_1=True, bit_3=True),
	PaletteSet(palette_set=165, row=1, bit_0=True, bit_2=True, bit_3=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(16),
		A_Walk1StepNorth()
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepWest(),
		A_WalkNorthwestSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=5, y=90, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_SetPriority(3),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=16, y=4, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
		A_SetPriority(3),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=4, y=208, z=0, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	Pause(30),
	FadeInFromColour(duration=60, colour=WHITE),
	PauseScriptUntilEffectDone(),
	Pause(170),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(6),
		A_WalkSouthPixels(12),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(4),
		A_WalkSouthSteps(11)
	]),
	Pause(328),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSoutheast()
	]),
	Pause(2),
	SetSyncActionScript(MARIO, A0229_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_0, A0229_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_1, A0229_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_2, A0229_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_4, A0229_ENDING_CUTSCENE_EFFECT),
	RememberLastObject(),
	ApplyTileModToLevel(use_alternate=True, room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, mod_id=1),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, mod_id=0),
	Pause(180),
	UnknownCommand(bytearray(b'_')),
	Pause(404),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=161, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=162, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=84, row=8),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=85, row=10),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=86, row=11),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=141, row=9),
	PaletteSetMorphs(palette_type=FADE_TO, duration=12, palette_set=140, row=13),
	PauseScriptUntilEffectDone(),
	Pause(216),
	ApplyTileModToLevel(use_alternate=True, room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, mod_id=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, mod_id=2),
	FadeOutToBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60, identifier="EVENT_3951_pause_49"),
	PlayMusicAtDefaultVolume(M0071_ENDINGPART2),
	Pause(130),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=0),
	Pause(8),
	EnterArea(room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, face_direction=SOUTHWEST, x=17, y=40, z=2),
	JmpToEvent(E3804_ENDING_CREDITS_CORONATION_NPCS)
])
