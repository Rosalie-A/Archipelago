# E2404_8BIT_END_WEST
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
	JmpIfBitClear(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2404_ret_13"]),
	JmpIfBitSet(TOWER_8BIT_EASTER_EGG_BIT_2, ["EVENT_2404_ret_13"]),
	StopAllBackgroundEvents(),
	FadeOutMusicFDA3(),
	SetBit(TOWER_8BIT_EASTER_EGG_BIT_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(64),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(6),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_Pause(54),
		A_Pause(16),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkEastPixels(6),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(64),
	PlayMusicAtDefaultVolume(M0045_HEARTBEATINGALITTLEFASTER_PART1),
	StopEmbeddedActionScript(NPC_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShadowOff(),
		A_WalkSoutheastSteps(7),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastPixels(8),
		A_JumpToHeight(108),
		A_WalkNortheastSteps(2),
		A_JumpToHeight(108),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNorthwestSteps(8)
	]),
	Jmp(["EVENT_2403_action_queue_10"]),
	Return(identifier="EVENT_2404_ret_13")
])
