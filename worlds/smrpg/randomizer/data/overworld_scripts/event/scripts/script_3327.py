# E3327_STUMPET_FIGHT
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	StopAllBackgroundEvents(),
	StartBattleAtBattlefield(PACK144_STUMPET_ENCOUNTER, BF20_BARREL_VOLCANO),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3327_set_temp_action_script_14"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_3327_reset_and_choose_game_23"]),
	MoveScriptToMainThread(),
	SetAsyncActionScript(NPC_0, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_5, A1023_ERUPTED_MAGMITES),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(NPC_0, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3327_set_temp_action_script_14"),
	SetTempSyncActionScript(NPC_1, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_2, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_3, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_4, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_5, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	RunBackgroundEvent(event_id=E3326_STUMPET_ERUPTION, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3327_reset_and_choose_game_23")
])
