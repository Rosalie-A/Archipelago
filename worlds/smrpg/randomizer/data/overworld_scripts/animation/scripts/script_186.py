#A0186_CHEST_SLOT_MACHINE_ROLLER
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
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SetPriority(3),
	A_SetVarToConst(FACTORY_FALL_3, 0, identifier="ACTION_186_set_var_to_const_2"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetVarToConst(FACTORY_FALL_3, 2),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetVarToConst(FACTORY_FALL_3, 1),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(4),
	A_Jmp(["ACTION_186_set_var_to_const_2"])
])
