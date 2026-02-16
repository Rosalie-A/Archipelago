# E2074_ENTER_MONSTRO_SEALED_ROOM
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
	EnterArea(room_id=R351_CULEXS_ROOM, face_direction=NORTH, x=29, y=45, z=0),
    JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["door_1_boss_sequence_begins"]),
    JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["EVENT_2074_enter_area_21"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_2074_enter_area_21"]),
    SummonObjectToCurrentLevel(NPC_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkEastPixels(12)
	]),
    SetSyncActionScript(LAYER_1, A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER),
	FadeInFromBlack(sync=False, duration=70),
	Pause(60),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30)
	]),
    RunDialog(dialog_id=DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["initiate_monstro_door_postgame"]),
	SetVarToConst(PRIMARY_TEMP_7000, 524),
    RunEventAsSubroutine(E0353_BOSS_BATTLE),
    JmpIfBitClear(GAME_OVER, ["EVENT_2074_fade_in_from_black_async_230"]),
	ResetAndChooseGame(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30)
	], identifier="initiate_monstro_door_postgame"),
	JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["EVENT_2074_apply_solidity_mod_170"]),
    EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT_2),
	Jmp(["EVENT_2048_set_bit_0"]),
	ApplySolidityModToLevel(permanent=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_2074_apply_solidity_mod_170"),
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33),
    EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	Jmp(["EVENT_2048_set_bit_0"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2074_fade_in_from_black_async_230"),
	Pause(5),
	PlayMusicAtDefaultVolume(M0058_CONVERSATIONWITHCULEX),
	Pause(60),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	RunEventAsSubroutine(E1219_POSTGAME_MONSTRO_SEALED_BOSS_UNLOCKS),
	Pause(15),
	SetBit(CULEX_POSTGAME_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	Jmp(["initiate_monstro_door_postgame"]),
	
	
    Return(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkEastPixels(12)
	], identifier="door_1_boss_sequence_begins"),
	SetSyncActionScript(LAYER_1, A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER),
	RunEventAsSubroutine(E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False, duration=70),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI3057_MONSTRO_SUPERBOSS_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_2074_action_queue_12"]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2074_fade_in_from_black_async_23"]),
	ResetAndChooseGame(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30)
	], identifier="EVENT_2074_action_queue_12"),
	JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_apply_solidity_mod_17"]),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	Jmp(["EVENT_2048_set_bit_0"]),
    ApplySolidityModToLevel(permanent=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_2074_apply_solidity_mod_17"),
	JmpIfBitSet(STAY_VOUCHER_USED, ["monstro_mod_check"]), # don't remove culex's door if postgame voucher is used
	# still apply solidity though, need extra shiny stone to get in
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33),
	SummonObjectToSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
	JmpIfBitClear(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_2074_enter_area_21"], identifier="monstro_mod_check"),
	JmpToEvent(E3886_END_GAME_CONTAINER_FROM_ALT_WIN_CONDITIONS),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4, identifier="EVENT_2074_enter_area_21"),
	Jmp(["EVENT_2048_set_bit_0"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2074_fade_in_from_black_async_23"),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	Pause(5),
	PlayMusicAtDefaultVolume(M0058_CONVERSATIONWITHCULEX),
	Pause(60),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunEventAsSubroutine(E1218_MONSTRO_SEALED_BOSS_UNLOCKS),
	Pause(15),
	SetBit(MONSTRO_MIDDLE_DOOR_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	Jmp(["EVENT_2074_action_queue_12"]),
])
