#A0548_KEEP_CROSSING_TERRA_COTTAS
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
	A_SetWalkingSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_WalkNorthwestPixels(37, identifier="ACTION_548_shift_northwest_pixels_7"),
	A_JmpIfRandom1of2(["ACTION_548_shift_northwest_pixels_30"]),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_JmpIfVarEqualsConst(GAME_OVER_COUNTER_MAYBE, 0, ["ACTION_548_pause_16"]),
	A_StartLoopNTimes(4),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=128, tiles=3, destinations=["ACTION_549_dec_0"]),
	A_Pause(16),
	A_EndLoop(),
	A_Jmp(["ACTION_548_reset_properties_17"]),
	A_Pause(80, identifier="ACTION_548_pause_16"),
	A_ResetProperties(identifier="ACTION_548_reset_properties_17"),
	A_JmpIfRandom1of2(["ACTION_548_shift_northwest_pixels_30"]),
	A_FaceNortheast(),
	A_Pause(8),
	A_FaceSoutheast(),
	A_Pause(8),
	A_WalkSoutheastPixels(37),
	A_Pause(8),
	A_FaceSouthwest(),
	A_Pause(8),
	A_FaceNorthwest(),
	A_Pause(16),
	A_Jmp(["ACTION_548_shift_northwest_pixels_7"]),
	A_WalkNorthwestPixels(37, identifier="ACTION_548_shift_northwest_pixels_30"),
	A_Pause(8),
	A_FaceNortheast(),
	A_Pause(8),
	A_FaceSoutheast(),
	A_Pause(16),
	A_Jmp(["ACTION_547_shift_southeast_pixels_7"])
])
