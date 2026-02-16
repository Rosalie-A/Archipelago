# E1428_RESCUE_TOAD_MUSHROOM_WAY_1
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
	DisableObjectTrigger(NPC_8),
	DisableObjectTrigger(NPC_9),
	FreezeAllNPCsUntilReturn(),
	StartBattleAtBattlefield(PACK006_JUST_GOOMBAS, BF09_GRASSLANDS),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1428_enable_trigger_19"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1428_reset_and_choose_game_25"]),
	RemoveObjectFromSpecificLevel(NPC_9, R203_MUSHROOM_WAY_AREA_01),
	RemoveObjectFromCurrentLevel(NPC_9),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=10, y=22, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=10, y=23, z=0, direction=EAST),
		A_FaceNorthwest()
	]),
	SetBit(TOAD_IN_MUSHROOM_WAY_1),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetAllSpeeds(FASTER),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(4),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R203_MUSHROOM_WAY_AREA_01),
	UnfreezeAllNPCs(),
	Return(),
	EnableObjectTrigger(NPC_8, identifier="EVENT_1428_enable_trigger_19"),
	EnableObjectTrigger(NPC_9),
	SetTempSyncActionScript(NPC_8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_9, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_1428_reset_and_choose_game_25"),
	Return()
])
