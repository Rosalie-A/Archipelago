# E3336_CORKPEDITE_ROOM_LOADER
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
	SetSyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 363, ["EVENT_3336_jmp_if_object_not_in_level_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 362, ["EVENT_3336_jmp_if_object_not_in_level_9"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE, ["EVENT_3336_run_event_as_subroutine_12"], identifier="EVENT_3336_jmp_if_object_not_in_level_7"),
	Jmp(["EVENT_3336_action_queue_10"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE, ["EVENT_3336_run_event_as_subroutine_12"], identifier="EVENT_3336_jmp_if_object_not_in_level_9"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestPixels(8),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3336_action_queue_10"),
	RunBackgroundEvent(event_id=E3337_CORKPEDITE_ANIMATION, return_on_level_exit=True),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3336_run_event_as_subroutine_12"),
	Return()
])
