# E2316_GARDENER_EXTERIOR_LOADER
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
		A_SetPriority(3),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_WalkEastPixels(5),
		A_WalkSouthPixels(3),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	JmpIfBitSet(TEMP_GARDENER_EXTERIOR_1, ["EVENT_2316_freeze_camera_24"]),
	JmpIfBitSet(TEMP_GARDENER_EXTERIOR_2, ["EVENT_2316_freeze_camera_6"]),
	FadeInFromBlack(sync=False),
	Return(),
	FreezeCamera(identifier="EVENT_2316_freeze_camera_6"),
	ClearBit(TEMP_GARDENER_EXTERIOR_2),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_WalkWestPixels(4),
		A_ShiftZUpSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$ \x00\x00\x00')),
		A_ShiftZUpSteps(8),
		A_BPL262728()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(32),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthSteps(5)
	]),
	FadeInFromBlack(sync=False),
	Pause(112),
	FadeOutToBlack(sync=False, duration=32),
	EnterArea(room_id=R419_LAZY_SHELL_CLOUD, face_direction=SOUTH, x=4, y=109, z=10, run_entrance_event=True),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=76),
		A_WalkNorthPixels(8),
		A_WalkEastPixels(17)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShiftToXYCoords(x=4, y=111),
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(8),
		A_WalkWestPixels(12),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkWestPixels(5),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	SetBit(TEMP_GARDENER_EXTERIOR_1),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$\x1c\x00\x00\x00')),
		A_ShiftZUpSteps(6),
		A_BPL262728(),
		A_SetSpriteSequence(index=14, sprite_offset=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_FaceNortheast(),
		A_JumpToHeight(160),
		A_WalkNortheastSteps(2),
		A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastPixels(8)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return(),
	FreezeCamera(identifier="EVENT_2316_freeze_camera_24"),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferToXYZF(x=9, y=88, z=24, direction=EAST)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=4, y=67)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$\xe3\xff\x00\x00')),
		A_ShiftZDownSteps(7),
		A_BPL262728(),
		A_SetSpriteSequence(index=14, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$@\x000\x01')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(37),
		A_BPL262728()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(2)
	]),
	UnfreezeCamera(),
	ClearBit(TEMP_GARDENER_EXTERIOR_1),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
