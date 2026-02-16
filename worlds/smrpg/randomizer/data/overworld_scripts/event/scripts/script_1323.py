# E1323_TOWER_LOBBY_HENCHMAN
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
	RunEventAsSubroutine(E1602_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_DO_NOT_REMOVE_FROM_LEVEL),
	RunDialog(dialog_id=DI2560_TOWER_HENCHMAN_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(5),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	JmpIfBitClear(GAME_OVER, ["EVENT_1323_remove_from_current_level_6"]),
	ResetAndChooseGame(),
	RemoveObjectFromCurrentLevel(NPC_4, identifier="EVENT_1323_remove_from_current_level_6"),
	RemoveObjectFromSpecificLevel(NPC_4, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	FadeInFromBlack(sync=False),
	Return()
])
