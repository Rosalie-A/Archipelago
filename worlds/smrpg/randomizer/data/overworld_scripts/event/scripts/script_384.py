# E0384_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_LOADER
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
	RunEventAsSubroutine(E0769_MUSHROOM_KINGDOM_OCCUPIED_PEACHS_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfObjectNotInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_384_jmp_if_object_not_in_level_12"]),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=12, y=97, z=4, direction=EAST),
		A_FaceNortheast()
	], identifier="EVENT_384_action_queue_4"),
	ApplySolidityModToLevel(permanent=True, room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, mod_id=1),
	JmpIfObjectInSpecificLevel(NPC_0, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, ["EVENT_384_fade_in_from_black_async_10"]),
	RemoveObjectFromSpecificLevel(NPC_2, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM),
	RemoveObjectFromCurrentLevel(NPC_2),
	ApplySolidityModToLevel(permanent=True, room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, mod_id=2),
	FadeInFromBlack(sync=False, identifier="EVENT_384_fade_in_from_black_async_10"),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_384_action_queue_4"], identifier="EVENT_384_jmp_if_object_not_in_level_12"),
	JmpToEvent(E0257_FADE_IN_ASYNC)
])
