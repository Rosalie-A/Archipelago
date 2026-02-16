#A0452_FACTORY_FOUR_SCREW_ROOM_AMEBOID
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
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_JmpIfBitClear(DIRECTIONAL_7045_7, ["ACTION_452_pause_3"]),
	A_Pause(176),
	A_Pause(1, identifier="ACTION_452_pause_3"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=2, destinations=["ACTION_452_sequence_looping_on_6"]),
	A_Jmp(["ACTION_452_pause_3"]),
	A_SequenceLoopingOn(identifier="ACTION_452_sequence_looping_on_6"),
	A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
	A_Pause(48),
	A_WalkNorthwestSteps(2, identifier="ACTION_452_shift_northwest_steps_9"),
	A_Pause(8),
	A_FaceNortheast(),
	A_Pause(8),
	A_WalkSoutheastSteps(2),
	A_Pause(8),
	A_FaceSouthwest(),
	A_Pause(8),
	A_Jmp(["ACTION_452_shift_northwest_steps_9"])
])
