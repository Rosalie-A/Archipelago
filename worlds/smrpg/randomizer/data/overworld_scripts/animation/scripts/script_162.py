#A0162_BOSS_IN_BANDITS_WAY_3
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
	A_JmpIfBitSet(UNKNOWN_7078_1, ["ACTION_162_set_animation_speed_57"]),
	A_JmpIfBitSet(UNKNOWN_7078_0, ["ACTION_162_set_animation_speed_38"]),
	A_JmpIfBitSet(UNKNOWN_7077_7, ["ACTION_162_set_animation_speed_18"]),
	A_VisibilityOn(),
	A_SetBit(UNKNOWN_7077_7),
	A_SequenceLoopingOn(),
	A_SetAllSpeeds(FASTER),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_JumpToHeight(128),
	A_WalkToXYCoords(x=20, y=108),
	A_WalkNorthSteps(7),
	A_StartLoopNTimes(1),
	A_WalkNortheastSteps(3),
	A_SetAllSpeeds(FAST),
	A_WalkNortheastSteps(2),
	A_SetAllSpeeds(FASTER),
	A_EndLoop(),
	A_WalkNorthwestSteps(2),
	A_SetAllSpeeds(FASTER, identifier="ACTION_162_set_animation_speed_18"),
	A_TransferToXYZF(x=24, y=82, z=0, direction=EAST),
	A_VisibilityOn(),
	A_FaceSouthwest(),
	A_Pause(1, identifier="ACTION_162_pause_22"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_162_set_bit_25"]),
	A_Jmp(["ACTION_162_pause_22"]),
	A_SetBit(UNKNOWN_7078_0, identifier="ACTION_162_set_bit_25"),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_JumpToHeight(128),
	A_SetPriority(3),
	A_WalkToXYCoords(x=29, y=72),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_SetAllSpeeds(VERY_FAST),
	A_WalkNorthwestSteps(9),
	A_SetAllSpeeds(FASTER),
	A_WalkNorthSteps(5),
	A_WalkNorthwestSteps(2),
	A_WalkNorthSteps(3),
	A_WalkNortheastSteps(2),
	A_SetAllSpeeds(FAST, identifier="ACTION_162_set_animation_speed_38"),
	A_TransferToXYZF(x=24, y=43, z=0, direction=EAST),
	A_VisibilityOn(),
	A_FaceSouthwest(),
	A_Pause(1, identifier="ACTION_162_pause_42"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_162_set_bit_45"]),
	A_Jmp(["ACTION_162_pause_42"]),
	A_SetBit(UNKNOWN_7078_1, identifier="ACTION_162_set_bit_45"),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_JumpToHeight(128),
	A_WalkToXYCoords(x=25, y=36),
	A_SetAllSpeeds(FASTER),
	A_WalkNorthwestSteps(4),
	A_SetAllSpeeds(FAST),
	A_WalkNorthwestSteps(4),
	A_SetAllSpeeds(FASTER),
	A_WalkNorthSteps(5),
	A_SetAllSpeeds(FAST),
	A_WalkNorthwestSteps(2),
	A_SetAllSpeeds(FAST, identifier="ACTION_162_set_animation_speed_57"),
	A_TransferToXYZF(x=20, y=16, z=0, direction=EAST),
	A_VisibilityOn(),
	A_FaceSoutheast(),
	A_Pause(1, identifier="ACTION_162_pause_61"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=4, destinations=["ACTION_162_set_bit_64"]),
	A_Jmp(["ACTION_162_pause_61"]),
	A_SetBit(BANDITS_WAY_CUTSCENE_3_VIEWED, identifier="ACTION_162_set_bit_64"),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_JumpToHeight(144),
	A_WalkNortheastSteps(5),
	A_VisibilityOff(),
	A_ReturnQueue()
])
