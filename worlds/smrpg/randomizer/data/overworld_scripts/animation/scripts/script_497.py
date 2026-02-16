#A0497_MUSHROOM_DERBY_UNKNOWN
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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_FloatingOn(),
	A_CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_SequencePlaybackOn(),
	A_ResetProperties(),
	A_ShadowOff(),
	A_SetWalkingSpeed(NORMAL),
	A_JumpToHeight(108),
	A_WalkFDirectionPixels(12),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_WalkFDirectionPixels(12),
	A_Pause(1, identifier="ACTION_497_pause_12"),
	A_JmpIfMarioInAir(["ACTION_497_pause_12"]),
	A_ClearBit(TEMP_7044_4),
	A_FixedFCoordOff(),
	A_ReturnQueue()
])
