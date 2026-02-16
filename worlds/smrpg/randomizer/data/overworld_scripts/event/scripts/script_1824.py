# E1824_KEEP_SET_PLATFORM_PROPERTIES
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	FreezeAllNPCsUntilReturn(),
	Pause(1),
	SetVarToConst(TEMP_70A9, 22),
	SetVarToConst(PRIMARY_TEMP_700C, 2),
	StartLoopNTimes(5),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FaceNortheast(),
		A_WalkFDirection16Pixels(),
		A_SetWalkingSpeed(SLOW)
	]),
	Inc(TEMP_70A9),
	AddConstToVar(PRIMARY_TEMP_700C, 2),
	EndLoop(),
	UnfreezeAllNPCs(),
	SetVarToConst(ROSE_WAY_7038, 2176),
	SetVarToConst(ROSE_WAY_703A, 7296),
	SetVarToConst(ROSE_WAY_703C, 1280),
	RunBackgroundEvent(event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1824_jmp_to_event_16"]),
	ClearBit(TEMP_7095_4),
	JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES, identifier="EVENT_1824_jmp_to_event_16")
])
