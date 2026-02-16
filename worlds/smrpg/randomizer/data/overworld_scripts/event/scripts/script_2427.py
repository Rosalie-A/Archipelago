# E2427_FOREST_UNDERGROUND_2_LOADER
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
	JmpIfBitSet(TEMP_7044_6, ["EVENT_2427_ret_60"]),
	SetBit(TEMP_7044_6),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_6', 'EVENT_2427_remove_from_level_9']),
	SummonObjectToSpecificLevel(NPC_0, R224_FOREST_MAZE_AREA_01),
	RemoveObjectFromSpecificLevel(NPC_1, R224_FOREST_MAZE_AREA_01),
	Jmp(["EVENT_2427_jmp_if_random_above_66_11"]),
	SummonObjectToSpecificLevel(NPC_1, R224_FOREST_MAZE_AREA_01, identifier="EVENT_2427_summon_to_level_6"),
	RemoveObjectFromSpecificLevel(NPC_0, R224_FOREST_MAZE_AREA_01),
	Jmp(["EVENT_2427_jmp_if_random_above_66_11"]),
	RemoveObjectFromSpecificLevel(NPC_0, R224_FOREST_MAZE_AREA_01, identifier="EVENT_2427_remove_from_level_9"),
	RemoveObjectFromSpecificLevel(NPC_1, R224_FOREST_MAZE_AREA_01),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_15', 'EVENT_2427_remove_from_level_18'], identifier="EVENT_2427_jmp_if_random_above_66_11"),
	SummonObjectToSpecificLevel(NPC_6, R226_FOREST_MAZE_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_7, R226_FOREST_MAZE_AREA_02),
	Jmp(["EVENT_2427_jmp_if_random_above_66_20"]),
	SummonObjectToSpecificLevel(NPC_6, R226_FOREST_MAZE_AREA_02, identifier="EVENT_2427_summon_to_level_15"),
	RemoveObjectFromSpecificLevel(NPC_7, R226_FOREST_MAZE_AREA_02),
	Jmp(["EVENT_2427_jmp_if_random_above_66_20"]),
	RemoveObjectFromSpecificLevel(NPC_6, R226_FOREST_MAZE_AREA_02, identifier="EVENT_2427_remove_from_level_18"),
	RemoveObjectFromSpecificLevel(NPC_7, R226_FOREST_MAZE_AREA_02),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_24', 'EVENT_2427_remove_from_level_27'], identifier="EVENT_2427_jmp_if_random_above_66_20"),
	SummonObjectToSpecificLevel(NPC_2, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_6, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_29"]),
	SummonObjectToSpecificLevel(NPC_6, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_24"),
	RemoveObjectFromSpecificLevel(NPC_2, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_29"]),
	RemoveObjectFromSpecificLevel(NPC_2, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_remove_from_level_27"),
	RemoveObjectFromSpecificLevel(NPC_6, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_33', 'EVENT_2427_summon_to_level_36'], identifier="EVENT_2427_jmp_if_random_above_66_29"),
	SummonObjectToSpecificLevel(NPC_3, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_7, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_38"]),
	SummonObjectToSpecificLevel(NPC_7, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_33"),
	RemoveObjectFromSpecificLevel(NPC_3, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_38"]),
	SummonObjectToSpecificLevel(NPC_3, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_36"),
	RemoveObjectFromSpecificLevel(NPC_7, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_42', 'EVENT_2427_summon_to_level_45'], identifier="EVENT_2427_jmp_if_random_above_66_38"),
	SummonObjectToSpecificLevel(NPC_4, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_8, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_47"]),
	SummonObjectToSpecificLevel(NPC_4, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_42"),
	RemoveObjectFromSpecificLevel(NPC_8, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_47"]),
	SummonObjectToSpecificLevel(NPC_4, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_45"),
	RemoveObjectFromSpecificLevel(NPC_8, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2427_summon_to_level_51', 'EVENT_2427_summon_to_level_54'], identifier="EVENT_2427_jmp_if_random_above_66_47"),
	SummonObjectToSpecificLevel(NPC_5, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_9, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_56"]),
	SummonObjectToSpecificLevel(NPC_5, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_51"),
	RemoveObjectFromSpecificLevel(NPC_9, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	Jmp(["EVENT_2427_jmp_if_random_above_66_56"]),
	SummonObjectToSpecificLevel(NPC_5, R233_FOREST_MAZE_AREA_03_UNDERGROUND, identifier="EVENT_2427_summon_to_level_54"),
	RemoveObjectFromSpecificLevel(NPC_9, R233_FOREST_MAZE_AREA_03_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2427_remove_from_level_59', 'EVENT_2427_remove_from_level_59'], identifier="EVENT_2427_jmp_if_random_above_66_56"),
	SummonObjectToSpecificLevel(NPC_0, R228_FOREST_MAZE_AREA_04),
	Jmp(["EVENT_2427_ret_60"]),
	RemoveObjectFromSpecificLevel(NPC_0, R228_FOREST_MAZE_AREA_04, identifier="EVENT_2427_remove_from_level_59"),
	Return(identifier="EVENT_2427_ret_60")
])
