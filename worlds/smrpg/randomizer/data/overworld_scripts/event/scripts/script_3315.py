# E3315_SEWERS_3RD_WATER_ROOM_EXIT_TO_RAT_LINE_ROOM
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
	EnterArea(room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, face_direction=NORTHEAST, x=20, y=42, z=2),
	JmpIfBitClear(SEWER_WATER_LEVEL, ["EVENT_3315_jmp_to_event_3"], identifier="EVENT_3315_jmp_if_bit_clear_1"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_3315_action_queue_2_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3315_action_queue_2_SUBSCRIPT_pause_1"])
	]),
	JmpToEvent(E3135_SEWERS_GENERIC_LOADER, identifier="EVENT_3315_jmp_to_event_3")
])
