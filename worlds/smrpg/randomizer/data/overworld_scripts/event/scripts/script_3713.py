# E3713_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_NPC_ANIMATIONS
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
	SetSyncActionScript(NPC_2, A0257_NIMBUS_PINWHEEL_LEFT),
	SetSyncActionScript(NPC_4, A0890_NIMBUS_DIZZY_SHY_GUY),
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3584_ret_0"], identifier="EVENT_3713_jmp_if_object_not_in_level_2"),
	Pause(1),
	Set7000ToObjectCoord(target_npc=NPC_4, coord=COORD_X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 12032),
	JmpIfComparisonResultIsLesser(["EVENT_3713_jmp_if_object_not_in_level_8"]),
	Jmp(["EVENT_3713_jmp_if_object_not_in_level_2"]),
	JmpIfObjectNotInSpecificLevel(NPC_4, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_3584_ret_0"], identifier="EVENT_3713_jmp_if_object_not_in_level_8"),
	PauseActionScript(NPC_4),
	SetBit(TEMP_7043_1),
	SetAsyncActionScript(NPC_4, A0256_NIMBUS_SHY_GUY_LEFT),
	ClearBit(TEMP_7043_2),
	Pause(1, identifier="EVENT_3713_pause_13"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_3713_clear_bit_16"]),
	Jmp(["EVENT_3713_pause_13"]),
	ClearBit(TEMP_7043_1, identifier="EVENT_3713_clear_bit_16"),
	ClearBit(TEMP_7043_3),
	JmpToEvent(E3713_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_NPC_ANIMATIONS)
])
