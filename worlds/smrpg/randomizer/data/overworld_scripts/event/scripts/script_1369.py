# E1369_CURTAIN_GAME_SUCCESS_FAILURE_FIGHT_BOSS
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
	Pause(30, identifier="EVENT_1369_pause_0"),
	EnableControlsUntilReturn([]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_1369_action_queue_5"]),
	ResetAndChooseGame(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceNortheast()
	], identifier="EVENT_1369_action_queue_5"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=4, y=21, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=5, y=20, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=5, y=19, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=6, y=18, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	UnfreezeCamera(),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=2),
	SetBit(TOWER_BOSS_1_DEFEATED),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestSteps(4)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestSteps(4)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestSteps(4)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestSteps(4)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(96),
		A_WalkNorthwestSteps(2),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestSteps(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSouthwestSteps(4),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	Pause(30),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RestoreAllHP(),
	RestoreAllFP(),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
    JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_1369_failed_spgrant"]),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunEventAsSubroutine(E1201_TOWER_CURTAIN_BOSS_UNLOCKS),
    SetBit(TOWER_BOSS_1_STAR_PIECE, identifier="EVENT_1369_failed_spgrant"),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
