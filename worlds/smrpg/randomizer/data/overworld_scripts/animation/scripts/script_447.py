#A0447_LOOPING_SINGLE_SPARKLE
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
	A_ObjectMemorySetBit(arg_1=0x3C, bits=[6]),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_FloatingOff(),
	A_TransferToObjectXY(MARIO),
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	A_JmpIfRandom1of2(["ACTION_447_shift_xy_pixels_9"]),
	A_ShiftXYPixels(x=4, y=4),
	A_Jmp(["ACTION_447_sequence_looping_on_10"]),
	A_ShiftXYPixels(x=252, y=252, identifier="ACTION_447_shift_xy_pixels_9"),
	A_SequenceLoopingOn(identifier="ACTION_447_sequence_looping_on_10"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_StartLoopNTimes(23),
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOff(identifier="ACTION_447_visibility_off_17"),
	A_ReturnQueue()
])
