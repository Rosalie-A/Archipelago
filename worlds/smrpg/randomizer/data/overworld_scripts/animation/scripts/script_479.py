#A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT
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
	A_VisibilityOff(),
	A_TransferToObjectXY(MEM_70A9),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00,\x00\x01\x00\x00\x80\x00\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00 \x00\x01\x00\x00\x80\x00\x80")),
	A_CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
	A_UnknownCommand(bytearray(b'\xfd%')),
	A_Pause(1, identifier="ACTION_479_pause_8"),
	A_Jmp(["ACTION_479_pause_8"])
])
