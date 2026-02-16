#A0470_COLLECT_MIDAS_COIN
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
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_PlaySound(sound=SO013_COIN, channel=4),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_SetSpriteSequence(index=2, looping=False),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_FAST),
	A_AddZCoord1Step(),
	A_Pause(26),
	A_VisibilityOff(),
	A_ReturnQueue()
])
