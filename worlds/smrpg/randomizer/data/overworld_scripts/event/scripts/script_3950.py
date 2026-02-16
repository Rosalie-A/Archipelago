# E3950_POST_FINAL_BOSS_INIT
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
	EnterArea(room_id=R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, face_direction=SOUTHWEST, x=4, y=51, z=0),
	FreezeCamera(),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=3, y=50, z=0, direction=EAST),
		A_TransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=57, z=0, direction=EAST),
		A_TransferXYZFPixels(x=240, y=0, z=0, direction=EAST),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=3, y=56, z=0, direction=EAST),
		A_TransferXYZFPixels(x=240, y=0, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=53, z=0, direction=EAST),
		A_TransferXYZFPixels(x=242, y=252, z=0, direction=EAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=6, y=50, z=0, direction=EAST),
		A_TransferXYZFPixels(x=240, y=254, z=0, direction=EAST)
	]),
	FadeInFromColour(duration=40, colour=WHITE),
	PauseScriptUntilEffectDone(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(12),
		A_SetSpriteSequence(index=12, sprite_offset=6, is_sequence=True, looping=True)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(6),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(120),
	ActionQueueSync(target=NPC_6, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=56, z=0, direction=EAST),
		A_TransferXYZFPixels(x=2, y=220, z=0, direction=EAST),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(1),
		A_Pause(60),
		A_ShiftZUpPixels(12),
		A_ShiftZDownPixels(12),
		A_EndLoop(),
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(56),
		A_VisibilityOff(),
		A_SetPriority(0),
		A_TransferXYZFPixels(x=0, y=216, z=0, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(90),
		A_ResetProperties(),
		A_Pause(150),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(120),
		A_ResetProperties(),
		A_Pause(90),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(90),
		A_ResetProperties(),
		A_Pause(120),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(90),
		A_ResetProperties(),
		A_Pause(120),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	Pause(90),
	PauseActionScript(NPC_6),
	StartAsyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_BPL262728(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'%\x00\x07\x80\xff')),
		A_UnknownCommand(bytearray(b'$\x98\xff\xc8\xff')),
		A_Pause(30),
		A_BPL262728()
	]),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	PauseActionScript(NPC_6),
	StartAsyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'%\x80\x06\xa0\xff')),
		A_UnknownCommand(bytearray(b'$\x90\xff\x00\x01')),
		A_Pause(30)
	]),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(60),
	PauseActionScript(NPC_6),
	StartAsyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x88\xff')),
		A_UnknownCommand(bytearray(b'$x\x01\x00\x00')),
		A_Pause(28)
	]),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(1, identifier="EVENT_3950_action_queue_43_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_3950_action_queue_43_SUBSCRIPT_pause_2"]),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(60),
	PauseActionScript(NPC_6),
	StartAsyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'%\x80\x06\x90\xff')),
		A_UnknownCommand(bytearray(b'$ \x000\xff')),
		A_Pause(30)
	]),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=4, y=52, z=0, direction=EAST),
		A_TransferXYZFPixels(x=242, y=252, z=0, direction=EAST)
	]),
	SetSyncActionScript(NPC_5, A0228_ENDING_CUTSCENE_EFFECT),
	Pause(2),
	PauseActionScript(NPC_6),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_BPL262728(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	Pause(230),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthSteps(3),
		A_WalkNorthPixels(8),
		A_Pause(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(6)
	]),
	Pause(240),
	JmpToEvent(E3951_STAR_PIECE_CREDITS_INIT)
])
