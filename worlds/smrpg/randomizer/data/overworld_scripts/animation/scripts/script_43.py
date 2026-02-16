#A0043_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH
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
	A_Pause(4),
	A_SetVarToConst(X_COORD_2, 15488),
	A_SetVarToConst(Y_COORD_2, 3584),
	A_SetVarToConst(Z_COORD_2, 864),
	A_UnknownCommand(bytearray(b'\x99')),
	A_SetPriority(3),
	A_ShadowOff(),
	A_SetVRAMPriority(PRIORITY_3),
	A_VisibilityOn(),
	A_JmpToSubroutine(["ACTION_15_ret_0"]),
	A_Pause(14),
	A_SequenceLoopingOn(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_SetAllSpeeds(FAST),
	A_FloatingOn(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%`\x03\xe0\xff')),
	A_WalkToXYCoords(x=26, y=26),
	A_BPL262728(),
	A_SetAllSpeeds(NORMAL),
	A_JumpToHeight(108),
	A_WalkEastSteps(2),
	A_StartLoopNTimes(4),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ClearBit(TEMP_7043_4),
	A_Pause(1, identifier="ACTION_43_pause_29"),
	A_JmpIfBitClear(TEMP_7043_4, ["ACTION_43_pause_29"]),
	A_Pause(4),
	A_SetVarToConst(X_COORD_2, 11904),
	A_SetVarToConst(Y_COORD_2, 2304),
	A_SetVarToConst(Z_COORD_2, 864),
	A_UnknownCommand(bytearray(b'\x99')),
	A_VisibilityOn(),
	A_Pause(14),
	A_SequenceLoopingOn(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_SetAllSpeeds(FAST),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%`\x03\xe0\xff')),
	A_WalkToXYCoords(x=19, y=18),
	A_BPL262728(),
	A_PlaySound(sound=SO065_THWOMP_STOMP, channel=4),
	A_JumpToHeight(108),
	A_JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["ACTION_43_shift_west_steps_50"]),
	A_WalkEastSteps(2),
	A_Jmp(["ACTION_298_clear_solidity_bits_0"]),
	A_WalkWestSteps(2, identifier="ACTION_43_shift_west_steps_50"),
	A_StartLoopNTimes(4),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_ReturnQueue()
])
