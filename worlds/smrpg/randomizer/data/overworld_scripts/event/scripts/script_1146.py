# E1146_SEASIDE_INITIATE_BOSS_FIGHT
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
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=6, y=26, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_VisibilityOn()
	], identifier="EVENT_1146_action_queue_0"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=26, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=6, y=28, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=6, y=24, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=7, y=26, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_0, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_1, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_2, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_3, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_6, A0147_SEASIDE_HENCHMAN),
	RunEventAsSubroutine(E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(6),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(2)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(30),
		A_JumpToHeight(96),
		A_Pause(15)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(9)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(45),
		A_VisibilityOff(),
		A_Pause(1),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=19, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(1),
		A_VisibilityOn(),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
		A_Pause(15),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Pause(45),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=19, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_Pause(5),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_JumpToHeight(128),
		A_WalkSoutheastSteps(2),
		A_SetSequenceSpeed(NORMAL)
	], identifier="ship_henchman_1_beach_1"),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=2, y=17, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, sprite_offset=3, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
		A_Pause(15),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=2, y=17, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_Pause(5),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_JumpToHeight(128),
		A_WalkSoutheastSteps(2),
		A_SetSequenceSpeed(NORMAL)
	], identifier="ship_henchman_2_beach_1"),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=17, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, sprite_offset=3, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
		A_Pause(15),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=17, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_Pause(5),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(128),
		A_WalkSoutheastSteps(4),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(1)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST)
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkSoutheastSteps(1),
		A_FaceNortheast()
	], identifier="ship_henchman_1_beach_2"),
	Pause(5),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkNorthwestSteps(1),
		A_FaceSoutheast()
	], identifier="ship_henchman_1_beach_3"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FixedFCoordOff(),
		A_WalkSoutheastSteps(3)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(5)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=8, y=30, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(40),
		A_FaceNorthwest(),
		A_Pause(40),
		A_FaceSoutheast()
	]),
	Pause(60),
	JmpToEvent(E1147_SEASIDE_INITIATE_BOSS_FIGHT_ANIMATION),
	Return()
])
