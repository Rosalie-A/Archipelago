# E2814_MUSHROOM_WAY_3_LOADER
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
	RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
	ClearBit(EXP_STAR_BIT_1),
	ClearBit(EXP_STAR_BIT_2),
	ClearBit(EXP_STAR_BIT_3),
	ClearBit(EXP_STAR_BIT_4),
	SetVarToConst(COIN_COUNTER_1, 0),
	SetVarToConst(COIN_COUNTER_2, 0),
	SetVarToConst(COIN_COUNTER_3, 0),
	SetVarToConst(COIN_COUNTER_4, 0),
	SetVarToConst(COIN_COUNTER_5, 0),
	SetVarToConst(COIN_COUNTER_6, 0),
	RemoveObjectFromSpecificLevel(NPC_0, R205_MUSHROOM_WAY_AREA_03),
	RemoveObjectFromSpecificLevel(NPC_1, R205_MUSHROOM_WAY_AREA_03),
	RemoveObjectFromSpecificLevel(NPC_2, R205_MUSHROOM_WAY_AREA_03),
	RunEventAsSubroutine(E0755_MUSHROOM_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2814_run_background_event_20"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2814_run_background_event_20"]),
	RunEventAsSubroutine(E3888_MUSHROOM_WAY_STAR_PIECE_SIGNAL),
	RunBackgroundEvent(event_id=E2813_MUSHROOM_WAY_3_SUMMON_SPINYS, return_on_level_exit=True, identifier="EVENT_2814_run_background_event_20"),
	RunBackgroundEvent(event_id=E2809_MUSHROOM_WAY_BOSS_THREATENS_YOU, return_on_level_exit=True, bit_6=True),
	Return()
])
