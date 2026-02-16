# E0391_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_LOADER
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
	RunEventAsSubroutine(E0766_MUSHROOM_KINGDOM_OCCUPIED_STAIRWAY_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfObjectNotInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfObjectNotInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_391_jmp_if_object_not_in_level_5"]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_2, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_391_jmp_if_object_not_in_level_5"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=25, y=28, z=0, direction=EAST)
	]),
	JmpIfObjectInSpecificLevel(NPC_0, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_391_fade_in_from_black_async_11"]),
	JmpIfObjectInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_391_fade_in_from_black_async_11"]),
	FadeInFromBlack(sync=False),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_391_fade_in_from_black_async_11"),
	Return()
])
