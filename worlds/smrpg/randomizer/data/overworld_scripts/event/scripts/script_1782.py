# E1782_LANDS_END_DESERT_1_LOADER
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
	ApplyTileModToLevel(use_alternate=True, room_id=R317_LANDS_END_DESERT_AREA_01, mod_id=32),
	SummonObjectToSpecificLevel(NPC_5, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_6, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_7, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_8, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_9, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_10, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_11, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_12, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
	SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
	SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SummonObjectToSpecificLevel(NPC_1, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SummonObjectToSpecificLevel(NPC_2, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SummonObjectToSpecificLevel(NPC_3, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SummonObjectToSpecificLevel(NPC_4, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SummonObjectToSpecificLevel(NPC_5, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
	SetVarToConst(SECONDARY_TEMP_7024, 22),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1782_run_event_as_subroutine_25"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1782_ret_30"]),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_1782_run_event_as_subroutine_25"]),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1782_run_event_as_subroutine_25"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1782_ret_30"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1782_ret_30"]),
	RunEventAsSubroutine(E3907_LANDS_END_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1782_ret_30")
])
