#A0302_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE_BASE
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
	A_Pause(10, identifier="ACTION_302_pause_0"),
	A_SetSolidityBits(cant_walk_through=True),
	A_SetSolidityBits(bit_4=True),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False, identifier="microbomb_spark"),
	A_PlaySound(sound=SO089_LIT_FUSE, channel=4),
	A_Pause(16),
	A_StopSound(),
	A_SetBit(TEMP_7043_0),
	A_Pause(1),
	A_ClearBit(TEMP_7043_0),
	A_Pause(3),
	A_VisibilityOff(),
	A_ClearBit(TEMP_7043_1),
	A_Pause(12),
	A_ClearSolidityBits(cant_walk_through=True),
	A_ClearSolidityBits(bit_4=True),
	A_TransferToXYZF(x=4, y=55, z=0, direction=EAST),
	A_ReturnQueue()
])
