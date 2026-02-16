#A0433_ROSE_WAY_TRANSPORT_PLATFORM_SUBROUTINE
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
	A_SetPriority(3, identifier="ACTION_433_set_priority_0"),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_IncPaletteRowBy(1),
	A_SetWalkingSpeed(FAST),
	A_ReturnQueue(),
	A_IncPaletteRowBy(15, 15, identifier="ACTION_433_inc_palette_row_by_6"),
	A_ClearBit(TEMP_7043_0),
	A_Pause(1, identifier="ACTION_433_pause_8"),
	A_Set700CToPressedButton(),
	A_Compare700CToVar(TEMP_7034),
	A_JmpIfLoadedMemoryIsNot0(["ACTION_433_pause_8"]),
	A_IncPaletteRowBy(1),
	A_SetBit(TEMP_7043_0),
	A_ReturnQueue()
])
