# E1408_MARIOS_PAD_EXTERIOR_LOADER
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
	Pause(4),
	JmpIfBitClear(TEMP_7042_0, ["EVENT_1408_action_queue_3"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=33),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_ReturnQueue()
	], identifier="EVENT_1408_action_queue_3"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1408_run_event_as_subroutine_7"]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_1408_jmp_if_bit_clear_9"]),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_1408_run_event_as_subroutine_7"),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1408_ret_13"], identifier="EVENT_1408_jmp_if_bit_clear_9"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1408_ret_13"]),
	RunEventAsSubroutine(E3887_MARIOS_PAD_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1408_ret_13")
])
