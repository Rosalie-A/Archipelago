# E2429_FOREST_UNKNOWN_SUMMONER
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
	JmpIfBitSet(TEMP_7044_5, ["EVENT_2429_ret_47"]),
	SetBit(TEMP_7044_5),
	JmpIfRandom2of3(['EVENT_2429_remove_from_level_6', 'EVENT_2429_remove_from_level_9']),
	SummonObjectToSpecificLevel(NPC_0, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	RemoveObjectFromSpecificLevel(NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	Jmp(["EVENT_2429_jmp_if_random_above_66_11"]),
	RemoveObjectFromSpecificLevel(NPC_0, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, identifier="EVENT_2429_remove_from_level_6"),
	SummonObjectToSpecificLevel(NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	Jmp(["EVENT_2429_jmp_if_random_above_66_11"]),
	RemoveObjectFromSpecificLevel(NPC_0, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, identifier="EVENT_2429_remove_from_level_9"),
	RemoveObjectFromSpecificLevel(NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	JmpIfRandom2of3(['EVENT_2429_remove_from_level_15', 'EVENT_2429_remove_from_level_18'], identifier="EVENT_2429_jmp_if_random_above_66_11"),
	SummonObjectToSpecificLevel(NPC_1, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	RemoveObjectFromSpecificLevel(NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	Jmp(["EVENT_2429_jmp_if_random_above_66_20"]),
	RemoveObjectFromSpecificLevel(NPC_1, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, identifier="EVENT_2429_remove_from_level_15"),
	SummonObjectToSpecificLevel(NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	Jmp(["EVENT_2429_jmp_if_random_above_66_20"]),
	RemoveObjectFromSpecificLevel(NPC_1, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, identifier="EVENT_2429_remove_from_level_18"),
	RemoveObjectFromSpecificLevel(NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER),
	JmpIfRandom2of3(['EVENT_2429_remove_from_level_24', 'EVENT_2429_remove_from_level_27'], identifier="EVENT_2429_jmp_if_random_above_66_20"),
	SummonObjectToSpecificLevel(NPC_0, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_jmp_if_random_above_66_29"]),
	RemoveObjectFromSpecificLevel(NPC_0, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_24"),
	SummonObjectToSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_jmp_if_random_above_66_29"]),
	RemoveObjectFromSpecificLevel(NPC_0, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_27"),
	RemoveObjectFromSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2429_remove_from_level_33', 'EVENT_2429_remove_from_level_36'], identifier="EVENT_2429_jmp_if_random_above_66_29"),
	SummonObjectToSpecificLevel(NPC_1, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_jmp_if_random_above_66_38"]),
	RemoveObjectFromSpecificLevel(NPC_1, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_33"),
	SummonObjectToSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_jmp_if_random_above_66_38"]),
	RemoveObjectFromSpecificLevel(NPC_1, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_36"),
	RemoveObjectFromSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	JmpIfRandom2of3(['EVENT_2429_remove_from_level_42', 'EVENT_2429_remove_from_level_45'], identifier="EVENT_2429_jmp_if_random_above_66_38"),
	SummonObjectToSpecificLevel(NPC_2, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	RemoveObjectFromSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_ret_47"]),
	RemoveObjectFromSpecificLevel(NPC_2, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_42"),
	SummonObjectToSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Jmp(["EVENT_2429_ret_47"]),
	RemoveObjectFromSpecificLevel(NPC_2, R235_FOREST_MAZE_AREA_08_UNDERGROUND, identifier="EVENT_2429_remove_from_level_45"),
	RemoveObjectFromSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
	Return(identifier="EVENT_2429_ret_47")
])
