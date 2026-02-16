#A0485_PLAYER_SHOCKED_WHEN_WIGGLER_WAKES_UP
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ShiftToXYCoords(x=3, y=74),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSoutheastPixels(4),
	A_WalkNorthPixels(8),
	A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_485_set_sprite_sequence_6"),
	A_Pause(10),
	A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(10),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_485_pause_12"]),
	A_Jmp(["ACTION_485_set_sprite_sequence_6"]),
	A_Pause(3, identifier="ACTION_485_pause_12"),
	A_WalkSoutheastPixels(4),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x0f\x80\xff')),
	A_Pause(48),
	A_BPL262728(),
	A_ReturnQueue()
])
