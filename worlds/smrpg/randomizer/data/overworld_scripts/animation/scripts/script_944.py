#A0944_CRANE_FOR_FINAL_FACTORY_BOSS
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
	A_SetWalkingSpeed(NORMAL),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b'\xc8\x87')),
	A_SetVarToConst(Z_COORD_2, 13),
	A_UnknownCommand(bytearray(b'\x98')),
	A_WalkToXYCoords(x=3, y=82),
	A_SetBit(TEMP_7044_3),
	A_WalkToXYCoords(x=6, y=81),
	A_SetBit(TEMP_7044_4),
	A_WalkToXYCoords(x=7, y=82),
	A_ReturnQueue()
])
