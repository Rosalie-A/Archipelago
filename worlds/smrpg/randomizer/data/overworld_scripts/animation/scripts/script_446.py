#A0446_SUMMON_EXTRA_SPARKLES
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
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
	A_JmpIfRandom1of2(["ACTION_446_shift_xy_pixels_9"]),
	A_ShiftXYPixels(x=252, y=4),
	A_Jmp(["ACTION_446_sequence_looping_on_10"]),
	A_ShiftXYPixels(x=4, y=252, identifier="ACTION_446_shift_xy_pixels_9"),
	A_SequenceLoopingOn(identifier="ACTION_446_sequence_looping_on_10"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
	A_StartLoopNTimes(5),
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
	A_Pause(1),
	A_EndLoop(),
	A_JmpIfBitClear(TEMP_7076_0, ["ACTION_446_start_loop_n_times_19"]),
	A_CreatePacketAtObjectCoords(packet=P023_LOOPING_SINGLE_SPARKLE, target_npc=MARIO, destinations=["ACTION_446_start_loop_n_times_19"]),
	A_StartLoopNTimes(5, identifier="ACTION_446_start_loop_n_times_19"),
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
	A_Pause(1),
	A_EndLoop(),
	A_JmpIfBitClear(TEMP_7076_0, ["ACTION_446_start_loop_n_times_26"]),
	A_CreatePacketAtObjectCoords(packet=P022_RECURSIVE_SPARKLES, target_npc=MARIO, destinations=["ACTION_446_start_loop_n_times_26"]),
	A_StartLoopNTimes(11, identifier="ACTION_446_start_loop_n_times_26"),
	A_JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
	A_JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOff(identifier="ACTION_446_visibility_off_31"),
	A_ReturnQueue()
])
