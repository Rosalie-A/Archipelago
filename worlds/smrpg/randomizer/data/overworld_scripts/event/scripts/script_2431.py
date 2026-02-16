# E2431_FOREST_MAZE_AREA_LOADER
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
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	JmpIfRandom2of3(['EVENT_2431_jmp_if_random_above_66_7', 'EVENT_2431_jmp_if_random_above_66_7']),
	SummonObjectToCurrentLevel(NPC_0),
	SetSyncActionScript(NPC_0, A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA),
	JmpIfRandom2of3(['EVENT_2431_jmp_if_random_above_66_10', 'EVENT_2431_jmp_if_random_above_66_10'], identifier="EVENT_2431_jmp_if_random_above_66_7"),
	SummonObjectToCurrentLevel(NPC_1),
	SetSyncActionScript(NPC_1, A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA),
	JmpIfRandom2of3(['EVENT_2431_jmp_if_random_above_128_13', 'EVENT_2431_jmp_if_random_above_128_13'], identifier="EVENT_2431_jmp_if_random_above_66_10"),
	SummonObjectToCurrentLevel(NPC_2),
	SetSyncActionScript(NPC_2, A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA),
	JmpIfRandom1of2(["EVENT_2431_remove_from_current_level_18"], identifier="EVENT_2431_jmp_if_random_above_128_13"),
	RemoveObjectFromCurrentLevel(NPC_5),
	JmpIfRandom1of2(["EVENT_2431_jmp_if_random_above_128_24"]),
	RemoveObjectFromCurrentLevel(NPC_3),
	Jmp(["EVENT_2431_jmp_if_random_above_128_24"]),
	RemoveObjectFromCurrentLevel(NPC_3, identifier="EVENT_2431_remove_from_current_level_18"),
	JmpIfRandom1of2(["EVENT_2431_summon_to_current_level_22"]),
	RemoveObjectFromCurrentLevel(NPC_5),
	Jmp(["EVENT_2431_jmp_if_random_above_128_24"]),
	SummonObjectToCurrentLevel(NPC_5, identifier="EVENT_2431_summon_to_current_level_22"),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	JmpIfRandom1of2(["EVENT_2431_remove_from_current_level_29"], identifier="EVENT_2431_jmp_if_random_above_128_24"),
	RemoveObjectFromCurrentLevel(NPC_6),
	JmpIfRandom1of2(["EVENT_2431_jmp_if_random_above_128_35"]),
	RemoveObjectFromCurrentLevel(NPC_4),
	Jmp(["EVENT_2431_jmp_if_random_above_128_35"]),
	RemoveObjectFromCurrentLevel(NPC_4, identifier="EVENT_2431_remove_from_current_level_29"),
	JmpIfRandom1of2(["EVENT_2431_summon_to_current_level_33"]),
	RemoveObjectFromCurrentLevel(NPC_6),
	Jmp(["EVENT_2431_jmp_if_random_above_128_35"]),
	SummonObjectToCurrentLevel(NPC_6, identifier="EVENT_2431_summon_to_current_level_33"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	JmpIfRandom1of2(["EVENT_2431_jmp_if_random_above_128_38"], identifier="EVENT_2431_jmp_if_random_above_128_35"),
	SummonObjectToCurrentLevel(NPC_7),
	SetSyncActionScript(NPC_7, A0410_FOREST_MAZE_AREA_BEE),
	JmpIfRandom1of2(["EVENT_2431_jmp_if_random_above_128_41"], identifier="EVENT_2431_jmp_if_random_above_128_38"),
	SummonObjectToCurrentLevel(NPC_8),
	SetSyncActionScript(NPC_8, A0411_FOREST_MAZE_AREA_BEE),
	JmpIfRandom1of2(["EVENT_2431_jmp_if_random_above_128_44"], identifier="EVENT_2431_jmp_if_random_above_128_41"),
	SummonObjectToCurrentLevel(NPC_9),
	SetSyncActionScript(NPC_9, A0412_FOREST_MAZE_AREA_BEE),
	JmpIfRandom1of2(["EVENT_2431_fade_in_from_black_async_47"], identifier="EVENT_2431_jmp_if_random_above_128_44"),
	SummonObjectToCurrentLevel(NPC_10),
	SetSyncActionScript(NPC_10, A0412_FOREST_MAZE_AREA_BEE),
	FadeInFromBlack(sync=False, identifier="EVENT_2431_fade_in_from_black_async_47"),
	Return()
])
