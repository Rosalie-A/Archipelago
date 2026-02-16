#A0661_PIPE_VAULT_JUMPING_CHOMPWEED
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
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_661_set_animation_speed_1"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=2, destinations=["ACTION_661_set_animation_speed_5"]),
	A_Pause(1),
	A_Jmp(["ACTION_661_set_animation_speed_1"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_661_set_animation_speed_5"),
	A_JumpToHeight(height=64, silent=True),
	A_Pause(1, identifier="ACTION_661_pause_7"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_661_pause_7"]),
	A_Jmp(["ACTION_661_set_animation_speed_1"])
])
