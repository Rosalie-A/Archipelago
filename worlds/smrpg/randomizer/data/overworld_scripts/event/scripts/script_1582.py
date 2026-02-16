# E1582_LANDS_END_TRAMPOLINE_TO_SEWER
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
	JmpIfBitSet(SEWERS_FLIPPED_CHEST_OPENED, ["EVENT_1582_run_event_as_subroutine_4"]),
	JmpIfBitClear(TEMP_7044_0, ["EVENT_1582_run_event_as_subroutine_4"]),
	SetBit(TEMP_7042_2),
	EnableObjectTriggerInSpecificLevel(NPC_1, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE, identifier="EVENT_1582_run_event_as_subroutine_4"),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, face_direction=SOUTH, x=8, y=100, z=14, run_entrance_event=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
