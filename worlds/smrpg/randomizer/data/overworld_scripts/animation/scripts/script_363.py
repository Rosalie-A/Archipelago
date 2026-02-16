#A0363_SKY_BRIDGE_HIT_BY_BULLET_BILL
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
	A_ClearSolidityBits(bit_7=True),
	A_SetWalkingSpeed(FAST),
	A_WalkSoutheastPixels(2, identifier="ACTION_363_shift_southeast_pixels_2"),
	A_JmpIfMarioInAir(["ACTION_363_clear_bit_5"]),
	A_Jmp(["ACTION_363_shift_southeast_pixels_2"]),
	A_ClearBit(TEMP_7044_7, identifier="ACTION_363_clear_bit_5"),
	A_ResetProperties(),
	A_FaceNorthwest(),
	A_SetAllSpeeds(NORMAL),
	A_ShiftZDownPixels(1),
	A_SetSolidityBits(bit_7=True),
	A_ReturnQueue()
])
