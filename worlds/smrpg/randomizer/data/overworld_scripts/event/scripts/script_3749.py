# E3749_NIMBUS_MEZZANINE_TRAMPOLINE_TO_TOWN_SQUARE
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
    JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["EVENT_3749_trampoline_defunct"]),
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_3749_run_event_as_subroutine_12"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	JmpIfBitSet(NIMBUS_BOSS_IN_TOWN_SQUARE, ["EVENT_3749_enter_area_10"]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3749_set_bit_7"]),
	SetBit(TEMP_7042_0),
	EnterArea(room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True),
	Return(),
	SetBit(TEMP_7042_0, identifier="EVENT_3749_set_bit_7"),
	EnterArea(room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA, face_direction=NORTHEAST, x=11, y=59, z=0, run_entrance_event=True, identifier="EVENT_3749_enter_area_10"),
	Return(),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE, identifier="EVENT_3749_run_event_as_subroutine_12"),
	Return(identifier="EVENT_3749_trampoline_defunct"),
])
