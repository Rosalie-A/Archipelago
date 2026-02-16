# E3345_VOLCANO_CHASE_SEQEUNCE
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
	SetBit(VOLCANO_STAIRCASE_ANIMATION_COMPLETED),
    JmpIfObjectNotInSpecificLevel(NPC_0, R394_VOLCANO_POSTCD_AREA_05, ["EVENT_3345_pause_141"]),
	Pause(1, identifier="EVENT_3345_pause_5"),
	JmpIfObjectsAreLessThanXYStepsApart(MARIO, NPC_0, 0, 4, ["EVENT_3345_remove_from_current_level_8"]),
	Jmp(["EVENT_3345_pause_5"]),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_3345_remove_from_current_level_8"),
	RemoveObjectFromSpecificLevel(NPC_0, R394_VOLCANO_POSTCD_AREA_05),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_0, destinations=["EVENT_3345_pause_11"]),
    
	Pause(1, identifier="EVENT_3345_pause_11"),
	JmpIfObjectsAreLessThanXYStepsApart(MARIO, NPC_0, 0, 2, ["EVENT_3345_pause_14"]),
	Jmp(["EVENT_3345_pause_11"]),
    JmpIfObjectNotInSpecificLevel(NPC_1, R394_VOLCANO_POSTCD_AREA_05, ["EVENT_3345_pause_20"], identifier="EVENT_3345_pause_141"),
	Pause(1, identifier="EVENT_3345_pause_14"),
	JmpIfObjectsAreLessThanXYStepsApart(MARIO, NPC_1, 0, 4, ["EVENT_3345_remove_from_current_level_17"]),
	Jmp(["EVENT_3345_pause_14"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_3345_remove_from_current_level_17"),
	RemoveObjectFromSpecificLevel(NPC_1, R394_VOLCANO_POSTCD_AREA_05),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_1, destinations=["EVENT_3345_pause_20"]),
	Pause(1, identifier="EVENT_3345_pause_20"),
	JmpIfObjectsAreLessThanXYStepsApart(MARIO, NPC_2, 0, 4, ["EVENT_3345_remove_from_current_level_23"]),
	Jmp(["EVENT_3345_pause_20"]),
	RemoveObjectFromCurrentLevel(NPC_2, identifier="EVENT_3345_remove_from_current_level_23"),
	RemoveObjectFromSpecificLevel(NPC_2, R394_VOLCANO_POSTCD_AREA_05),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_2, destinations=["EVENT_3345_create_packet_at_npc_coords_26"]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_0, destinations=["EVENT_3345_ret_27"], identifier="EVENT_3345_create_packet_at_npc_coords_26"),
	Return(identifier="EVENT_3345_ret_27")
])
