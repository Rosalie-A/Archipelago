# E3704_NIMBUS_CASTLE_OCCUPIED_5_DOOR_ROOM_LOADER
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
	ApplyTileModToLevel(use_alternate=True, room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, mod_id=0),
	JmpIfObjectNotInSpecificLevel(NPC_9, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_3704_jmp_if_object_in_level_3"]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_TransferXYZFPixels(x=244, y=250, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	JmpIfObjectInSpecificLevel(NPC_1, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_3704_jmp_if_object_in_level_7"], identifier="EVENT_3704_jmp_if_object_in_level_3"),
	JmpIfObjectNotInSpecificLevel(NPC_3, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_3704_jmp_if_object_in_level_7"]),
	UnsyncActionScript(NPC_3),
	SetSyncActionScript(NPC_3, A0245_NIMBUS_5_EXIT_HALLWAY_FAKE_BIRD_STATUES_ACTIVATE),
	JmpIfObjectInSpecificLevel(NPC_2, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_3704_fade_in_from_black_async_11"], identifier="EVENT_3704_jmp_if_object_in_level_7"),
	JmpIfObjectNotInSpecificLevel(NPC_4, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_3704_fade_in_from_black_async_11"]),
	UnsyncActionScript(NPC_4),
	SetSyncActionScript(NPC_4, A0245_NIMBUS_5_EXIT_HALLWAY_FAKE_BIRD_STATUES_ACTIVATE),
	FadeInFromBlack(sync=False, identifier="EVENT_3704_fade_in_from_black_async_11"),
	Return()
])
