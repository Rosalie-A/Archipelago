#A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP
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
	A_Set700CToPressedButton(identifier="ACTION_487_set_700C_to_pressed_button_0"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65516),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_JumpToHeight(64, identifier="ACTION_487_jump_to_height_5"),
	A_Pause(1),
	A_JmpIfMarioInAir(["ACTION_487_jump_to_height_5"]),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_487_set_700C_to_pressed_button_0"]),
	A_ReturnQueue()
])
