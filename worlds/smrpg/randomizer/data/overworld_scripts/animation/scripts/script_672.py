#A0672_ROSE_TOWN_LIBERATED_WATER_KID
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
	A_JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	A_WalkSouthwestSteps(1),
	A_WalkNorthwestSteps(1),
	A_FaceSoutheast(),
	A_SequenceLoopingOff(),
	A_Pause(160),
	A_WalkSoutheastSteps(1),
	A_WalkNortheastSteps(1),
	A_JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	A_ReturnQueue(),
	A_VisibilityOff(identifier="ACTION_672_visibility_off_10"),
	A_TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	A_FaceSoutheast(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_VisibilityOn(),
	A_Walk1StepSoutheast(),
	A_SetSolidityBits(cant_walk_through=True),
	A_WalkSoutheastSteps(4),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkSouthwestSteps(2),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_WalkSouthwestSteps(2),
	A_ReturnQueue(),
	A_WalkNortheastSteps(2, identifier="ACTION_672_shift_northeast_steps_26"),
	A_WalkNortheastPixels(8),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_WalkNortheastSteps(1),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_WalkNortheastPixels(8),
	A_WalkNorthwestSteps(4),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_Walk1StepNorthwest(),
	A_VisibilityOff(),
	A_TransferToXYZF(x=16, y=85, z=0, direction=EAST),
	A_ReturnQueue()
])
