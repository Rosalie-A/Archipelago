# E2312_BOOSTER_PASS_SPINY_COIN_BUTTON
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
	JmpIfBitSet(BOOSTER_PASS_2ND_ROOM_BUTTON_PRESSED, ["EVENT_2312_ret_78"]),
	DisableObjectTrigger(NPC_5),
	SetBit(BOOSTER_PASS_2ND_ROOM_BUTTON_PRESSED),
	RemoveObjectFromSpecificLevel(NPC_0, R101_BOOSTER_PASS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_1, R101_BOOSTER_PASS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_2, R101_BOOSTER_PASS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_3, R101_BOOSTER_PASS_AREA_02),
	Store01To0248(),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=3, y=94)
	]),
	Pause(8),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2312_apply_tile_mod_18"]),
	Pause(1, identifier="EVENT_2312_pause_12"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2312_pause_12"]),
	SetBit(TEMP_7042_0),
	RemoveObjectFromCurrentLevel(NPC_0),
	AddCoins(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=7, y=115, z=8, direction=EAST),
		A_VisibilityOn(),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_SetPriority(3),
		A_JumpToHeight(128),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=4, identifier="EVENT_2312_apply_tile_mod_18"),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_2312_set_action_script_21"]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE, identifier="EVENT_2312_set_action_script_21"),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=0),
	Pause(48),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=4, y=85)
	]),
	Pause(8),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2312_apply_tile_mod_34"]),
	Pause(1, identifier="EVENT_2312_pause_28"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2312_pause_28"]),
	SetBit(TEMP_7042_1),
	RemoveObjectFromCurrentLevel(NPC_1),
	AddCoins(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=8, y=109, z=8, direction=EAST),
		A_VisibilityOn(),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_JumpToHeight(128),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=5, identifier="EVENT_2312_apply_tile_mod_34"),
	JmpIfBitSet(TEMP_7042_1, ["EVENT_2312_set_action_script_37"]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE, identifier="EVENT_2312_set_action_script_37"),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=1),
	Pause(48),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=8, y=85)
	]),
	Pause(8),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2312_apply_tile_mod_50"]),
	Pause(1, identifier="EVENT_2312_pause_44"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_2312_pause_44"]),
	SetBit(TEMP_7042_2),
	RemoveObjectFromCurrentLevel(NPC_2),
	AddCoins(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=12, y=109, z=8, direction=EAST),
		A_VisibilityOn(),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_JumpToHeight(128),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=6, identifier="EVENT_2312_apply_tile_mod_50"),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_2312_set_action_script_53"]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE, identifier="EVENT_2312_set_action_script_53"),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=2),
	Pause(48),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=8, y=73)
	]),
	Pause(8),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2312_apply_tile_mod_65"]),
	Pause(1, identifier="EVENT_2312_pause_60"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2312_pause_60"]),
	RemoveObjectFromCurrentLevel(NPC_3),
	AddCoins(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetBit(TEMP_7042_3),
		A_FloatingOff(),
		A_TransferToXYZF(x=11, y=97, z=12, direction=EAST),
		A_VisibilityOn(),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_JumpToHeight(128),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=7, identifier="EVENT_2312_apply_tile_mod_65"),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_2312_set_action_script_68"]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE, identifier="EVENT_2312_set_action_script_68"),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=3),
	Pause(48),
	ApplySolidityModToLevel(permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=3),
	Store00To0248(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=6, y=95)
	]),
	Return(identifier="EVENT_2312_ret_78")
])
