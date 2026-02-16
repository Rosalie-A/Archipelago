#A0379_MARRYMORE_LIBERATED_EXTERIOR_PHOTO_KID
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
	A_FaceSouthwest(identifier="ACTION_379_face_southwest_0"),
	A_JumpToHeight(height=64, silent=True),
	A_Pause(1, identifier="ACTION_379_pause_2"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_379_pause_2"]),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_379_face_southeast_6"]),
	A_Jmp(["ACTION_379_face_southwest_0"]),
	A_FaceSoutheast(identifier="ACTION_379_face_southeast_6"),
	A_Pause(1, identifier="ACTION_379_pause_7"),
	A_JmpIfBitClear(TEMP_7043_1, ["ACTION_379_face_southwest_0"]),
	A_Jmp(["ACTION_379_pause_7"])
])
