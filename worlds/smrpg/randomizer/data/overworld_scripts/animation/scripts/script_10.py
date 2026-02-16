#A0010_FALL_ON_TRAMPOLINE
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
	A_ShadowOn(),
	A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True),
	A_FaceSouth(),
	A_FixedFCoordOn(),
	A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
	A_AddZCoord1Step(),
	A_SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	A_ResetProperties(),
	A_FixedFCoordOff(),
	A_ShadowOff(),
	A_FloatingOn(),
	A_ClearBit(TEMP_707C_0),
	A_ReturnQueue()
])
