#A0957_FACTORY_CONVEYOR_PAINT
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
	A_SetPriority(3),
	A_WalkWestPixels(8),
	A_VisibilityOff(identifier="ACTION_957_visibility_off_2"),
	A_Pause(1),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_957_visibility_off_2"]),
	A_ClearBit(TEMP_7043_0),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=0, looping=False),
	A_PlaySound(sound=SO146_MACHINE_TRANSFORM, channel=4),
	A_Pause(36),
	A_Jmp(["ACTION_957_visibility_off_2"])
])
