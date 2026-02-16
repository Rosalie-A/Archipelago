# E1312_TOWER_LOBBY_LOADER
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
	PauseActionScript(NPC_4, identifier="EVENT_1312_pause_action_script_0"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(6)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(9),
		A_WalkSouthwestPixels(12),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkNortheastPixels(4),
		A_WalkSoutheastPixels(5),
		A_SetPriority(1),
		A_ShadowOn()
	]),
	RunEventAsSubroutine(E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfObjectNotInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["EVENT_1312_pause_action_script_9"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["EVENT_1312_pause_action_script_9"]),
	FadeInFromBlack(sync=False),
	Return(),
	PauseActionScript(NPC_1, identifier="EVENT_1312_pause_action_script_9"),
	PauseActionScript(NPC_2),
	RemoveObjectFromSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	RemoveObjectFromSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	FadeInFromBlack(sync=False),
	Return()
])
