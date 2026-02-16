# E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER
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
	SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
	SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
	SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_0, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_1, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_1, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_0, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_1, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_2, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_3, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_4, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_5, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_6, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_7, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_8, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_9, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_10, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_11, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_12, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_13, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_14, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_15, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	ClearBit(UNKNOWN_704F_5),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x15')),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1783_set_var_to_const_35"]),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	FadeInFromBlack(sync=False),
	SetVarToConst(SECONDARY_TEMP_7024, 20, identifier="EVENT_1783_set_var_to_const_35"),
	SetVarToConst(TEMP_7026, 21),
	SetBit(TEMP_7044_5),
	Return()
])
