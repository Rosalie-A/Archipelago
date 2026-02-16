#A0984_DREAM_CUSHION_CHEF
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
	A_SetSequenceSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_Pause(1, identifier="ACTION_984_pause_2"),
	A_JmpIfBitSet(TEMP_7043_1, ["ACTION_984_face_southwest_5"]),
	A_Jmp(["ACTION_984_pause_2"]),
	A_FaceSouthwest(identifier="ACTION_984_face_southwest_5"),
	A_Pause(30),
	A_FaceSoutheast(),
	A_Pause(30),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(40),
	A_SetSequenceSpeed(SLOW),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Jmp(["ACTION_984_pause_2"])
])
