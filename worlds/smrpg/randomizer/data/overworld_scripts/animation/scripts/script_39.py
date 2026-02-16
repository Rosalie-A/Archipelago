#A0039_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_TINY_FISH
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
	A_ShadowOff(),
	A_StartLoopNTimes(2),
	A_Pause(1, identifier="ACTION_39_pause_2"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_39_pause_2"]),
	A_TransferToXYZF(x=29, y=29, z=0, direction=EAST),
	A_SetPriority(3),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_VisibilityOn(),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(96),
	A_WalkSoutheastSteps(3),
	A_VisibilityOff(),
	A_ClearBit(TEMP_7043_1),
	A_EndLoop(),
	A_Pause(1, identifier="ACTION_39_pause_15"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_39_pause_15"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b'\x97\x17'), identifier="ACTION_39_db_20"),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_39_db_20"]),
	A_JumpToHeight(120),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNorthwest(),
	A_WalkNorthwestPixels(4),
	A_FloatingOff(),
	A_ReturnQueue()
])
