# E1538_BANDITS_WAY_STAR_CHEST_CAMERA_AND_DOGS
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1538_run_background_event_3"]),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	RunBackgroundEvent(event_id=E1706_BANDITS_WAY_LEFT_CHEST_STAR_CHECK, return_on_level_exit=True, bit_6=True, identifier="EVENT_1538_run_background_event_3"),
	JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1538_jmp_to_event_7"]),
	SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_ClearBit(UNIVERSAL_CHEST_ANIMATION_BIT)
	]),
	JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_1538_jmp_to_event_7")
])
