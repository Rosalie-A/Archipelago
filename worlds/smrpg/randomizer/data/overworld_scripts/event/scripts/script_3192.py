# E3192_MINES_LEFT_HENCHMAN
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
	MoveScriptToMainThread(),
	SetBit(TEMP_7043_0),
	RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3192_clear_bit_9"]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4], identifier="EVENT_3192_action_queue_5_SUBSCRIPT_object_memory_set_bit_0"),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FaceMario(),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(NORMAL),
		A_Pause(32),
		A_JumpToHeight(56),
		A_Pause(32),
		A_JumpToHeight(56),
		A_Pause(32),
		A_Pause(1, identifier="EVENT_3192_action_queue_5_SUBSCRIPT_pause_10"),
		A_JmpIfBitClear(TEMP_7043_1, ["EVENT_3192_action_queue_5_SUBSCRIPT_pause_10"]),
		A_Pause(32),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(56),
		A_Pause(32),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestSteps(3),
		A_WalkSoutheastSteps(2),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ReturnQueue()
	]),
    RemoveObjectFromCurrentLevel(NPC_1),
	SetBit(MINES_HENCHMAN_LEFT_DEFEATED),
	SetBit(TEMP_7043_1),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	ClearBit(TEMP_7043_0, identifier="EVENT_3192_clear_bit_9"),
	Return()
])
