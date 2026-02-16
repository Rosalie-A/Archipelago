# E3284_SHIP_SAVE_ROOMS_LOADER
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
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3284_clear_bit_10"]),
	ClearBit(TEMP_7043_0),
	SetVarToConst(TEMP_70AE, 0),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_6),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3284_ret_9"]),
	RunEventAsSubroutine(E3906_SHIP_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3284_ret_9"),
	ClearBit(EXP_STAR_BIT_1, identifier="EVENT_3284_clear_bit_10"),
	ClearBit(EXP_STAR_BIT_2),
	ClearBit(EXP_STAR_BIT_3),
	ClearBit(EXP_STAR_BIT_4),
	SetVarToConst(COIN_COUNTER_1, 0),
	SetVarToConst(COIN_COUNTER_2, 0),
	SetVarToConst(COIN_COUNTER_3, 0),
	SetVarToConst(COIN_COUNTER_4, 0),
	SetVarToConst(COIN_COUNTER_5, 0),
	SetVarToConst(COIN_COUNTER_6, 0),
	FadeInFromBlack(sync=False),
	Return()
])
