#A0677_MUSHROOM_DERBY_UNKNOWN
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
	A_JmpIfRandom2of3(['ACTION_677_pause_2', 'ACTION_677_pause_3'], identifier="ACTION_677_jmp_if_random_above_66_0"),
	A_Pause(30),
	A_Pause(30, identifier="ACTION_677_pause_2"),
	A_Pause(30, identifier="ACTION_677_pause_3"),
	A_JumpToHeight(height=64, silent=True),
	A_Pause(1, identifier="ACTION_677_pause_5"),
	A_JmpIfBitSet(TEMP_7044_7, ["ACTION_677_pause_9"]),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_5"]),
	A_Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
	A_Pause(1, identifier="ACTION_677_pause_9"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_9"]),
	A_FaceNortheast(),
	A_ReturnQueue()
])
