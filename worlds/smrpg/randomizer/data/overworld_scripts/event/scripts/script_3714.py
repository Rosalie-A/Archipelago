# E3714_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_LOADER
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
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_6"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_12"]),
	RunBackgroundEvent(event_id=E3713_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_NPC_ANIMATIONS, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_2, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3585_fade_in_from_black_async_0"], identifier="EVENT_3714_jmp_if_object_not_in_level_6"),
	JmpIfObjectNotInSpecificLevel(NPC_3, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_set_action_script_9"]),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(NPC_2, A0257_NIMBUS_PINWHEEL_LEFT, identifier="EVENT_3714_set_action_script_9"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_3, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_jmp_if_object_not_in_level_14"], identifier="EVENT_3714_jmp_if_object_not_in_level_12"),
	RunBackgroundEvent(event_id=E3716_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_GUST, return_on_level_exit=True, bit_6=True),
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3714_fade_in_from_black_async_16"], identifier="EVENT_3714_jmp_if_object_not_in_level_14"),
	SetSyncActionScript(NPC_4, A0881_NIMBUS_SHAMAN),
	FadeInFromBlack(sync=False, identifier="EVENT_3714_fade_in_from_black_async_16"),
	Return()
])
