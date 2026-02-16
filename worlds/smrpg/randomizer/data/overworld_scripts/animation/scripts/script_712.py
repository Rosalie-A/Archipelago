#A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL
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
	A_Set700CToPressedButton(identifier="ACTION_712_set_700C_to_pressed_button_0"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_712_pause_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 29, ["ACTION_712_db_7"]),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\x00\x00\x00\x02\x80")),
	A_ReturnQueue(),
	A_UnknownCommand(bytearray(b' \x03'), identifier="ACTION_712_db_7"),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00 \x00\x01\x00\x00\x80\x01\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x80\x01\x80")),
	A_ReturnQueue(),
	A_Pause(2, identifier="ACTION_712_pause_11"),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80")),
	A_ReturnQueue()
])
