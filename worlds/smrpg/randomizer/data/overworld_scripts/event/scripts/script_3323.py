# E3323_VOLCANO_1ST_ROOM_LOADER
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
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3323_set_7000_to_current_level_3"], identifier="EVENT_3323_jmp_if_bit_set_0"),
	JmpToSubroutine(["EVENT_3323_summon_to_level_7"]),
	SetBit(TEMP_7042_0),
	Set7000ToCurrentLevel(identifier="EVENT_3323_set_7000_to_current_level_3"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 354, ["EVENT_3333_set_var_to_const_0"]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	SummonObjectToSpecificLevel(NPC_3, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, identifier="EVENT_3323_summon_to_level_7"),
	SummonObjectToSpecificLevel(NPC_4, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS),
	SummonObjectToSpecificLevel(NPC_5, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS),
	SummonObjectToSpecificLevel(NPC_0, R356_VOLCANO_AREA_08),
	SummonObjectToSpecificLevel(NPC_1, R356_VOLCANO_AREA_08),
	SummonObjectToSpecificLevel(NPC_2, R356_VOLCANO_AREA_08),
	SummonObjectToSpecificLevel(NPC_6, R358_VOLCANO_AREA_11),
	SummonObjectToSpecificLevel(NPC_7, R358_VOLCANO_AREA_11),
	SummonObjectToSpecificLevel(NPC_1, R359_VOLCANO_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R359_VOLCANO_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R360_VOLCANO_AREA_04_BUNCH_OF_STEPS),
	SummonObjectToSpecificLevel(NPC_1, R360_VOLCANO_AREA_04_BUNCH_OF_STEPS),
	SummonObjectToSpecificLevel(NPC_2, R361_VOLCANO_AREA_09),
	SummonObjectToSpecificLevel(NPC_3, R361_VOLCANO_AREA_09),
	SummonObjectToSpecificLevel(NPC_4, R361_VOLCANO_AREA_09),
	SummonObjectToSpecificLevel(NPC_5, R361_VOLCANO_AREA_09),
	SummonObjectToSpecificLevel(NPC_6, R361_VOLCANO_AREA_09),
	SummonObjectToSpecificLevel(NPC_0, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_1, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_2, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_3, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_4, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE),
	SummonObjectToSpecificLevel(NPC_0, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_1, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_2, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_3, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE),
	RemoveObjectFromSpecificLevel(NPC_4, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE),
	SummonObjectToSpecificLevel(NPC_0, R364_VOLCANO_AREA_14),
	SummonObjectToSpecificLevel(NPC_1, R364_VOLCANO_AREA_14),
	SummonObjectToSpecificLevel(NPC_2, R364_VOLCANO_AREA_14),
	RemoveObjectFromSpecificLevel(NPC_3, R364_VOLCANO_AREA_14),
	RemoveObjectFromSpecificLevel(NPC_4, R364_VOLCANO_AREA_14),
	SummonObjectToSpecificLevel(NPC_0, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_1, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_2, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_3, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_4, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_5, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_6, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_7, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_8, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_9, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_10, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_11, R386_VOLCANO_AREA_12_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_1, R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP),
	SummonObjectToSpecificLevel(NPC_2, R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP),
	SummonObjectToSpecificLevel(NPC_4, R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP),
	SummonObjectToSpecificLevel(NPC_1, R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_2, R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_5, R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_2, R384_VOLCANO_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R384_VOLCANO_AREA_05),
	RemoveObjectFromSpecificLevel(NPC_4, R384_VOLCANO_AREA_05),
	RemoveObjectFromSpecificLevel(NPC_5, R384_VOLCANO_AREA_05),
	SummonObjectToSpecificLevel(NPC_1, R385_VOLCANO_AREA_06),
	RemoveObjectFromSpecificLevel(NPC_2, R385_VOLCANO_AREA_06),
	RemoveObjectFromSpecificLevel(NPC_3, R385_VOLCANO_AREA_06),
	RemoveObjectFromSpecificLevel(NPC_4, R385_VOLCANO_AREA_06),
	SummonObjectToSpecificLevel(NPC_8, R389_VOLCANO_AREA_20_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_9, R389_VOLCANO_AREA_20_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_10, R389_VOLCANO_AREA_20_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_11, R389_VOLCANO_AREA_20_JUMPING_PYROSPHERES),
	SummonObjectToSpecificLevel(NPC_0, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_1, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_2, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_3, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_4, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	SummonObjectToSpecificLevel(NPC_5, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_6, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_7, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_8, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	RemoveObjectFromSpecificLevel(NPC_9, R390_VOLCANO_AREA_16_ERUPTING_STUMPET),
	ApplyTileModToLevel(use_alternate=True, room_id=R390_VOLCANO_AREA_16_ERUPTING_STUMPET, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R390_VOLCANO_AREA_16_ERUPTING_STUMPET, mod_id=1),
	Return()
])
