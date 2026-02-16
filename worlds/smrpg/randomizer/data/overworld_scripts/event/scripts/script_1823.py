# E1823_LANDS_END_GROTTO_FIRST_ROOM_UPPER_CHEST
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
	JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1823_jmp_to_event_7"]),
	SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetVarToConst(TIMER_701C, 40),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1543_CHEST_CAMERA_SHIFT, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(),
	JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_1823_jmp_to_event_7"),
	Return()
])
