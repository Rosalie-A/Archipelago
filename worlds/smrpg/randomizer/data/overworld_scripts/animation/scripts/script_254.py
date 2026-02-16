#A0254_ENDING_CUTSCENE_EFFECT
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
	A_FloatingOff(),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\xb4\x00 \x00\x01\x00\x00\x80\xfe\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00v\x00\x1a\x00\x01\x00\x00\x80\xfe\x80")),
	A_Pause(248),
	A_SetVarToConst(PRIMARY_TEMP_700C, 65120),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(240),
	A_SetVarToConst(PRIMARY_TEMP_700C, 64800),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(120),
	A_SetVarToConst(PRIMARY_TEMP_700C, 64512),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(90),
	A_SetVarToConst(PRIMARY_TEMP_700C, 64000),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(60),
	A_SetVarToConst(PRIMARY_TEMP_700C, 63744),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(30),
	A_SetVarToConst(PRIMARY_TEMP_700C, 63488),
	A_UnknownCommand(bytearray(b'5\x00\x06')),
	A_UnknownCommand(bytearray(b'5\x01\x06')),
	A_Pause(230),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(FAST),
	A_AddZCoord1Step(),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpSteps(2),
	A_SetBit(TEMP_7043_4),
	A_ShiftZUpSteps(2),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpSteps(8),
	A_BPL262728(),
	A_ReturnQueue()
])
