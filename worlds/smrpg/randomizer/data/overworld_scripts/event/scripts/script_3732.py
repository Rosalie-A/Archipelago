# E3732_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_LOADER
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
	JmpIfBitClear(NIMBUS_PLATFORM_ACTIVE, ["EVENT_3732_action_queue_2"]),
	SummonObjectToCurrentLevel(NPC_6),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	], identifier="EVENT_3732_action_queue_2"),
    JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_3732_run_event_as_subroutine_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, ["EVENT_3732_run_event_as_subroutine_0"]),
	RemoveObjectFromSpecificLevel(NPC_0, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND),
	SummonObjectToSpecificLevel(NPC_1, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND),
    
	RunEventAsSubroutine(E0839_NIMBUS_CASTLE_SECOND_POST_THRONE_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_3732_run_event_as_subroutine_0"),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_3584_ret_0"]),
	ClearBit(EXP_STAR_BIT_6),
	CreatePacketAtObjectCoords(packet=P022_RECURSIVE_SPARKLES, target_npc=MARIO, destinations=["EVENT_3584_ret_0"]),
	Return()
])
