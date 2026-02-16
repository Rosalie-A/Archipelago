# E2563_REVEAL_BEAN_VALLEY_BEANSTALK
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
	JmpIfBitSet(TEMP_708C_4, ["EVENT_2563_freeze_camera_28"]),
	SetBit(TEMP_708C_4),
	SetBit(UNKNOWN_BEANSTALK_707F_1),
	PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
	FreezeCamera(),
	Pause(32),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=26, y=29),
		A_FaceNortheast()
	]),
	Pause(80),
	PlaySound(sound=SO127_LIGHT_RATTLE, channel=6),
	SummonObjectToCurrentLevel(NPC_0),
	SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
	PlaySound(sound=SO128_FLOATING_HOVERING, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(64),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(6)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(40),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(64),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(8),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Pause(48),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthSteps(7)
	]),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(56),
		A_ResetProperties()
	]),
	StopEmbeddedActionScript(MARIO),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Jmp(["EVENT_2563_ret_37"]),
	FreezeCamera(identifier="EVENT_2563_freeze_camera_28"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_WalkToXYCoords(x=26, y=30),
		A_FaceNortheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_Pause(24),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_ShadowOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x80\x01\x80\x01')),
		A_UnknownCommand(bytearray(b'%\x00\x0c\x80\xff')),
		A_Pause(31),
		A_BPL262728(),
		A_ShadowOn(),
		A_SetSpriteSequence(index=13, sprite_offset=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(24)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$ \x00\x00\x00')),
		A_WalkNorthSteps(10),
		A_BPL262728()
	]),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3615_CLIMB_UP_VALLEY_BEANSTALK_INTO_VINE_CLOUDS),
	Return(identifier="EVENT_2563_ret_37")
])
