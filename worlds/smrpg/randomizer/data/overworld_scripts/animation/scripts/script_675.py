#A0675_ROSE_TOWN_LIBERATED_WATER_KID
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
	A_Pause(32),
	A_JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	A_Walk1StepSouthwest(),
	A_FaceNorthwest(),
	A_Pause(160),
	A_Walk1StepNortheast(),
	A_JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	A_ReturnQueue()
])
