# E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND
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
	Pause(1, identifier="EVENT_2385_pause_0"),
	JmpIfMarioInAir(["EVENT_2385_set_bit_4"]),
	ClearBit(TEMP_7044_6),
	Jmp(["EVENT_2385_pause_0"]),
	SetBit(TEMP_7044_6, identifier="EVENT_2385_set_bit_4"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2385_action_queue_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2385_action_queue_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2385_action_queue_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2385_enter_area_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2385_enter_area_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2385_enter_area_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2385_enter_area_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2385_enter_area_15"]),
	Jmp(["EVENT_2385_pause_0"]),
	EnterArea(room_id=R238_SMITHY_FACTORY_FALL_FROM_LUGNUT_ROOMS_AREA_06_PRIOR, face_direction=NORTHWEST, x=15, y=10, z=0, run_entrance_event=True, identifier="EVENT_2385_enter_area_15"),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	], identifier="EVENT_2385_action_queue_17"),
	Jmp(["EVENT_2385_pause_0"])
])
