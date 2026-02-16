#A0923_SHIP_STAIRCASE_ZEOSTARS
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
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_ShadowOn(),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0003),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_923_db_10"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_923_pause_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_923_pause_8"]),
	A_Pause(15),
	A_Pause(15, identifier="ACTION_923_pause_8"),
	A_Pause(15, identifier="ACTION_923_pause_9"),
	A_UnknownCommand(bytearray(b' \x05'), identifier="ACTION_923_db_10"),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x01\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x02\x00\x01\x00\x00\x00\x02\x80')),
	A_Pause(1, identifier="ACTION_923_pause_13"),
	A_Jmp(["ACTION_923_pause_13"])
])
