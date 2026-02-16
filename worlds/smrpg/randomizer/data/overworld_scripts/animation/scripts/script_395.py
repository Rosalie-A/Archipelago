#A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY
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
	A_SetAllSpeeds(NORMAL, identifier="ACTION_395_set_animation_speed_0"),
	A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SequencePlaybackOn(),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_FloatingOn(),
	A_FixedFCoordOff(),
	A_ShadowOff(),
	A_ResetProperties(),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
