# E0372_MUSHROOM_KINGDOM_BOSS_FIGHT_CUTSCENE
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
	JmpIfBitSet(UNKNOWN_7082_4, ["EVENT_256_ret_0"]),
	SetBit(UNKNOWN_7082_4),
	SetBit(TEMP_7043_5),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_372_action_queue_3_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_372_action_queue_3_SUBSCRIPT_pause_0"]),
		A_FloatingOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=15, y=31, height=4),
		A_FaceNortheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn()
	], identifier="EVENT_372_action_queue_3"),
	RememberLastObject(),
	Pause(60),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_8, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_9, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x07p\xff')),
		A_WalkSoutheastPixels(15),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastPixels(10),
		A_BPL262728(),
		A_FixedFCoordOn(),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=6),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(9),
		A_Pause(1, identifier="EVENT_372_action_queue_19_SUBSCRIPT_pause_17"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_372_action_queue_19_SUBSCRIPT_pause_17"]),
		A_JumpToHeight(height=64, silent=True),
		A_Walk1StepNorthwest(),
		A_Pause(1, identifier="EVENT_372_action_queue_19_SUBSCRIPT_pause_21"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_372_action_queue_19_SUBSCRIPT_pause_21"]),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ClearSolidityBits(bit_4=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x07p\xff')),
		A_WalkNorthwestPixels(15),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestPixels(10),
		A_BPL262728(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(9),
		A_Pause(1, identifier="EVENT_372_action_queue_20_SUBSCRIPT_pause_15"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_372_action_queue_20_SUBSCRIPT_pause_15"]),
		A_JumpToHeight(height=64, silent=True),
		A_Walk1StepSoutheast(),
		A_Pause(1, identifier="EVENT_372_action_queue_20_SUBSCRIPT_pause_19"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_372_action_queue_20_SUBSCRIPT_pause_19"]),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	Pause(60),
	SetSyncActionScript(NPC_4, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_5, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_8, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_9, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_6, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_7, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast()
	]),
	Jmp(["EVENT_373_action_queue_6"])
])
