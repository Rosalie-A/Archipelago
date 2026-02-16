# E2403_8BIT_END_EAST
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
	JmpIfBitClear(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2403_ret_25"]),
	JmpIfBitSet(TOWER_8BIT_EASTER_EGG_BIT_2, ["EVENT_2403_ret_25"]),
	StopAllBackgroundEvents(),
	FadeOutMusicFDA3(),
	SetBit(TOWER_8BIT_EASTER_EGG_BIT_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(64),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\xc0\xff')),
		A_Pause(54),
		A_BPL262728(),
		A_Pause(16),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	Pause(64),
	PlayMusicAtDefaultVolume(M0045_HEARTBEATINGALITTLEFASTER_PART1),
	StopEmbeddedActionScript(NPC_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_WalkNorthwestSteps(8)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_VisibilityOff()
	], identifier="EVENT_2403_action_queue_10"),
	ResetCoords(NPC_0),
	FadeOutMusicFDA3(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_ShadowOn(),
		A_Pause(16),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(5),
		A_Pause(24),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(8)
	]),
	Pause(32),
	PlayMusicAtDefaultVolume(M0046_HEARTBEATINGALITTLEFASTER_PART2),
	StopEmbeddedActionScript(MARIO),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	PlayMusicAtDefaultVolume(M0032_ANDMYNAME_SBOOSTER),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ResetPrioritySet(),
	ClearBit(TOWER_8BIT_EASTER_EGG_BIT_1),
	ClearBit(TOWER_8BIT_EASTER_EGG_BIT_2),
	Return(identifier="EVENT_2403_ret_25")
])
