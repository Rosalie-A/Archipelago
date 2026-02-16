# E3745_NIMBUS_BACK_EXIT_INITIATE_FALLING_SEQUENCE
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
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=27, y=29, z=16, direction=SOUTHEAST),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_FloatingOn(),
		A_ShadowOn(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	FadeInFromBlack(sync=True),
	Pause(50),
	PauseScriptUntilEffectDone(),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, face_direction=SOUTHEAST, x=19, y=95, z=10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=19, y=95, z=27, direction=SOUTHEAST),
		A_SetSpriteSequence(index=10, sprite_offset=3, is_sequence=True, looping=True),
		A_ShadowOn(),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x00\x08\x00'))
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3745_action_queue_9_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_3745_action_queue_9_SUBSCRIPT_pause_0"]),
		A_BPL262728(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOn()
	]),
	SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	Pause(8),
	PauseScriptUntilEffectDone(),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, face_direction=SOUTHEAST, x=27, y=91, z=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=27, y=91, z=16, direction=SOUTHEAST),
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x00\x0c\x00'))
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3745_action_queue_17_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_3745_action_queue_17_SUBSCRIPT_pause_0"]),
		A_BPL262728(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_ShadowOn()
	]),
	SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	Pause(15),
	PauseScriptUntilEffectDone(),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH, face_direction=SOUTHEAST, x=27, y=115, z=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=27, y=115, z=16, direction=SOUTHEAST),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_ShadowOn(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x00\x0e\x00'))
	]),
	FadeInFromBlack(sync=True),
	Pause(50),
	PauseScriptUntilEffectDone(),
	FadeOutToBlack(sync=False),
	SetBit(TEMP_704A_2),
	EnterArea(room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS, face_direction=SOUTHEAST, x=20, y=50, z=0, run_entrance_event=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=20, y=50, z=0, direction=SOUTHEAST),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_FloatingOn()
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3745_action_queue_32_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_3745_action_queue_32_SUBSCRIPT_pause_0"]),
		A_StopSound(),
		A_BPL262728(),
		A_JumpToHeight(height=108, silent=True)
	]),
	SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
