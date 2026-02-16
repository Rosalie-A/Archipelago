#A0617_MINES_LEFT_CROOK
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
	A_JmpIfBitSet(MINES_HENCHMAN_LEFT_DEFEATED, ["ACTION_617_visibility_off_3"]),
	A_ReturnQueue(),
	A_VisibilityOff(identifier="ACTION_617_visibility_off_3"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SequencePlaybackOff(),
	A_ReturnQueue()
])
