# E2616_FACTORY_4TH_ROOM_GREEN_BUTTON
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
	DisableObjectTrigger(NPC_14),
	SetBit(UNUSED_7091_4),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=7, y=82),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthPixels(6)
	]),
	SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=0, y=61)
	]),
	Pause(1, identifier="EVENT_2616_pause_6"),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_2616_pause_6"]),
	SetBit(TEMP_7044_2),
	SetSyncActionScript(NPC_13, A0944_CRANE_FOR_FINAL_FACTORY_BOSS),
	Pause(1, identifier="EVENT_2616_pause_10"),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_2616_pause_10"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=3, y=66)
	]),
	Pause(1, identifier="EVENT_2616_pause_13"),
	JmpIfBitClear(TEMP_7044_4, ["EVENT_2616_pause_13"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=13, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=14, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(32),
	ActionQueueSync(target=NPC_13, subscript=[
		A_DecZCoord1Step(),
		A_ShiftZDownPixels(6),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(11),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(56),
		A_WalkWestPixels(1),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(2),
		A_FaceNortheast(),
		A_JumpToHeight(108),
		A_Pause(16),
		A_FloatingOff(),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(24),
	UnfreezeCamera(),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ShiftZUpSteps(5),
		A_Pause(16),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(3),
		A_Pause(16),
		A_WalkNorthwestSteps(9)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_ShiftZUpSteps(5),
		A_Pause(16),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(3),
		A_Pause(16),
		A_WalkNorthwestSteps(6),
		A_ShadowOn(),
		A_WalkNorthwestSteps(3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(3)
	]),
	FreezeCamera(),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=6, is_sequence=True, looping=True),
		A_Pause(16)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xd0\xfd\xb0\x01')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\xa0\xff')),
		A_Pause(27),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_UnknownCommand(bytearray(b'$@\x00\x00\x00')),
		A_Pause(16),
		A_UnknownCommand(bytearray(b'$\x00\x00\x00\x00')),
		A_Pause(1),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_Pause(1),
		A_SetPriority(1),
		A_Pause(6),
		A_BPL262728()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(37),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x00\xd0\xff')),
		A_Pause(59)
	]),
	Pause(88),
	FadeOutToBlack(sync=False, duration=8),
	Pause(48),
	JmpToEvent(E3791_OPEN_FACTORY_FINAL_BOSS_ROOM),
	Return()
])
