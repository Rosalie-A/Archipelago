# E0530_ROSE_TOWN_OCCUPIED_BACKGROUND_1
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
	ClearBit(TEMP_7044_6, identifier="EVENT_530_clear_bit_0"),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_1),
	Pause(1, identifier="EVENT_530_pause_4"),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_530_run_event_as_subroutine_7"]),
	Jmp(["EVENT_530_pause_4"]),
	RunEventAsSubroutine(E0548_ROSE_TOWN_OCCUPIED_ARROW_ANIMATE, identifier="EVENT_530_run_event_as_subroutine_7"),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_530_jmp_if_random_above_128_11"], identifier="EVENT_530_jmp_if_bit_set_8"),
	Pause(1),
	Jmp(["EVENT_530_jmp_if_bit_set_8"]),
	JmpIfRandom1of2(["EVENT_530_pause_14"], identifier="EVENT_530_jmp_if_random_above_128_11"),
	Pause(60),
	Jmp(["EVENT_530_clear_bit_0"]),
	Pause(30, identifier="EVENT_530_pause_14"),
	Jmp(["EVENT_530_clear_bit_0"])
])
