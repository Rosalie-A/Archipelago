#A0489_FOREST_MAZE_AREA_DECOY_MUSHROOM
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
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_489_set_animation_speed_4"], identifier="ACTION_489_jmp_if_object_within_range_1"),
	A_Pause(1),
	A_Jmp(["ACTION_489_jmp_if_object_within_range_1"]),
	A_SetSequenceSpeed(SLOW, identifier="ACTION_489_set_animation_speed_4"),
	A_SetSpriteSequence(index=7, looping=False),
	A_Pause(48),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(NORMAL),
	A_Jmp(["ACTION_405_sequence_looping_on_0"])
])
