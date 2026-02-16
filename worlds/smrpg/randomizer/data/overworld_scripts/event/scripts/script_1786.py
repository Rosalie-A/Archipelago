# E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE
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
	JmpIfBitSet(MOUSE_RETURNED_TO_MONSTRO, ["EVENT_1786_summon_to_level_2"]),
	SummonObjectToSpecificLevel(NPC_1, R317_LANDS_END_DESERT_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06, identifier="EVENT_1786_summon_to_level_2"),
	SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
	SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x16')),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1786_set_var_to_const_11"]),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	FadeInFromBlack(sync=False),
	SetVarToConst(SECONDARY_TEMP_7024, 20, identifier="EVENT_1786_set_var_to_const_11"),
	SetBit(TEMP_7044_5),
	Return()
])
