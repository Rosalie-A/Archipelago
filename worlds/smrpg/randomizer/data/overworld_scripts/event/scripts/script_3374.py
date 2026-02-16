# E3374_KEEP_THWOMP_ROOM_BACKGROUND
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
	JmpIfBitSet(TEMP_7044_7, ["EVENT_3374_jmp_if_bit_set_2"], identifier="EVENT_3374_jmp_if_bit_set_0"),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3374_jmp_if_mario_in_air_9"], identifier="EVENT_3374_jmp_if_bit_set_2"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3374_jmp_if_mario_in_air_9"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3374_jmp_if_mario_in_air_9"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_3374_jmp_if_mario_in_air_9"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3374_jmp_if_mario_in_air_9"]),
	Pause(1),
	Jmp(["EVENT_3374_jmp_if_bit_set_0"]),
	JmpIfMarioInAir(["EVENT_3374_action_queue_11"], identifier="EVENT_3374_jmp_if_mario_in_air_9"),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(4),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3374_action_queue_11"),
	Jmp(["EVENT_3374_jmp_if_bit_set_0"])
])
