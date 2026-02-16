# E2353_TOWER_HENCHMAN_3
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
	Set7000ToObjectCoord(target_npc=NPC_8, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2353_stop_all_background_events_4"]),
	RunDialog(dialog_id=DI3072_TOWER_HENCHMAN_3_WINDOW, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	StopAllBackgroundEvents(identifier="EVENT_2353_stop_all_background_events_4"),
	RunDialog(dialog_id=DI3073_TOWER_HENCHMAN_3, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	JmpIfBitClear(GAME_OVER, ["EVENT_2353_remove_from_current_level_9"]),
	ResetAndChooseGame(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_2353_remove_from_current_level_9"),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS),
	Pause(2),
	FadeInFromBlack(sync=False),
	Return()
])
