# E3335_CORKPEDITE_COLLISION
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
	StopAllBackgroundEvents(),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3335_start_battle_3"]),
	JmpToEvent(E0255_EXP_STAR_HIT),
	StartBattleAtBattlefield(PACK145_CORKPEDITE_ENCOUNTER, BF20_BARREL_VOLCANO, identifier="EVENT_3335_start_battle_3"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3335_set_temp_action_script_12"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_3335_reset_and_choose_game_16"]),
	SetAsyncActionScript(MEM_70A8, A1023_ERUPTED_MAGMITES),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	DisableObjectTrigger(MEM_70A8),
	Pause(2),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3335_set_temp_action_script_12"),
	RunBackgroundEvent(event_id=E3337_CORKPEDITE_ANIMATION, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3335_reset_and_choose_game_16")
])
