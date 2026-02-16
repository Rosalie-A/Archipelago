#A0932_STUMPET
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
	A_TransferXYZFPixels(x=0, y=0, z=0, direction=EAST, identifier="ACTION_932_transfer_xyzf_pixels_0"),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2, identifier="ACTION_932_pause_2"),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_932_pause_2"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(60),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(8),
	A_Jmp(["ACTION_932_transfer_xyzf_pixels_0"])
])
