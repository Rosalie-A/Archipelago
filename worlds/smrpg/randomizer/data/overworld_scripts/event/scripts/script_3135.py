# E3135_SEWERS_GENERIC_LOADER
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
	Set7000ToCurrentLevel(),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, R333_KERO_SEWERS_ENTRANCE, ["event_3135_init"]),
    JmpIfBitSet(SEWERS_CLOSED, ["EVENT_3135_a"]),
    RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
    Jmp(["event_3135_init"]),
    SummonObjectToCurrentLevel(NPC_0, identifier="EVENT_3135_a"),
	SummonObjectToCurrentLevel(NPC_1),
	ClearBit(TEMP_707C_5, "event_3135_init"),
	SetVarToConst(TIMER_701C, 300),
	StopBackgroundEvent(TIMER_701C),
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 14, ["EVENT_3135_jmp_if_bit_set_7"]),
	JmpToSubroutine(["EVENT_3134_summon_to_level_0"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 14),
	Jmp(["EVENT_3135_jmp_if_bit_clear_9"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3135_jmp_if_bit_clear_9"], identifier="EVENT_3135_jmp_if_bit_set_7"),
	JmpToSubroutine(["EVENT_3134_summon_to_level_0"]),
	JmpIfBitClear(SEWER_WATER_LEVEL, ["EVENT_3135_reset_priority_set_14"], identifier="EVENT_3135_jmp_if_bit_clear_9"),
	Set7000ToCurrentLevel(),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, R333_KERO_SEWERS_ENTRANCE, ["EVENT_3135_run_event_as_subroutine_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE, ["EVENT_3135_run_event_as_subroutine_17"]),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[]),
	Jmp(["EVENT_3135_run_event_as_subroutine_17"]),
	ResetPrioritySet(identifier="EVENT_3135_reset_priority_set_14"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3135_run_event_as_subroutine_17"]),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),


	JmpIfBitSet(SEWERS_FLIPPED_CHEST_OPENED, ["EVENT_3135_fade"], identifier="EVENT_3135_run_event_as_subroutine_17"),
    JmpIfBitClear(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_3135_fade"]),
    EnableObjectTrigger(NPC_1),


	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3135_fade"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3135_ret_22"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3135_ret_22"]),
	RunEventAsSubroutine(E3891_SEWERS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3135_ret_22")
])
