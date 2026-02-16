#A0946_WIGGLER_ASLEEP
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
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_946_set_sprite_sequence_0"),
	A_Pause(128, identifier="ACTION_946_pause_1"),
	A_JmpIfRandom1of2(["ACTION_946_start_loop_n_times_9"]),
	A_StartLoopNTimes(2),
	A_WalkNortheastPixels(1),
	A_WalkSouthwestPixels(1),
	A_EndLoop(),
	A_Pause(128),
	A_Jmp(["ACTION_946_set_sprite_sequence_0"]),
	A_StartLoopNTimes(2, identifier="ACTION_946_start_loop_n_times_9"),
	A_WalkSoutheastPixels(1),
	A_WalkNorthwestPixels(1),
	A_EndLoop(),
	A_Pause(128),
	A_Jmp(["ACTION_946_pause_1"])
])
