# E3285_SEA_SINGLE_CHEST_ROOM_LOADER
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
	JmpIfBitSet(UNKNOWN_SEA_7055_6, ["EVENT_3285_jmp_if_bit_clear_3"]),
	SetBit(UNKNOWN_SEA_7055_6),
	ApplyTileModToLevel(use_alternate=True, room_id=R131_SEA_AREA_04_BUNCH_OF_ZEOSTARS, mod_id=32),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3285_jmp_to_event_13"], identifier="EVENT_3285_jmp_if_bit_clear_3"),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 133, ["EVENT_3285_set_var_to_const_8"]),
	SetVarToConst(TIMER_7022, 5),
	Jmp(["EVENT_3285_jmp_to_event_13"]),
	SetVarToConst(TIMER_7022, 40, identifier="EVENT_3285_set_var_to_const_8"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3285_jmp_to_event_13"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3285_jmp_to_event_13"]),
	RunEventAsSubroutine(E3905_SEA_STAR_PIECE_SIGNAL),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3285_jmp_to_event_13")
])
