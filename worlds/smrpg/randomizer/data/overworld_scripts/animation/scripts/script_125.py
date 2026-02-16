#A0125_MK_BRANCH_HALLWAY_HENCHMAN
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
	A_SetBit(TEMP_7043_5, identifier="ACTION_125_set_bit_0"),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 2),
	A_Inc(PRIMARY_TEMP_700C),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_JmpToSubroutine(["ACTION_103_clear_solidity_bits_0"]),
	A_EndLoop(),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	A_FaceSouthwest(),
	A_Jmp(["ACTION_125_set_bit_0"])
])
