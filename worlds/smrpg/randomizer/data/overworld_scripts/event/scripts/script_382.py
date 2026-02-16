# E0382_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_LOADER
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
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_382_jmp_if_bit_clear_56"]),
	JmpIfObjectNotInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_382_jmp_if_object_in_level_6"]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_382_jmp_if_object_in_level_6"),
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED, ["EVENT_382_action_queue_64"]),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=3, y=67, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast()
	]),
	PauseScriptUntilEffectDone(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepNortheast(),
		A_WalkSoutheastSteps(3),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast()
	]),
	RememberLastObject(),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Walk1StepNorthwest(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(1),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(1),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(10),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceEast()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	Pause(10),
	PauseActionScript(NPC_3),
	SetVarToConst(TEMP_70A9, 23),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	Pause(10),
	PauseActionScript(NPC_3),
	SetVarToConst(TEMP_70A9, 23),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(7),
		A_WalkSoutheastSteps(3),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(7),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(120),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(120),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(120),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouth()
	]),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED),
	Return(),
	JmpIfBitClear(OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED, ["EVENT_382_run_event_as_subroutine_58"], identifier="EVENT_382_jmp_if_bit_clear_56"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=63, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_382_run_event_as_subroutine_58"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_382_ret_62"]),
	RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_382_ret_62"),
	JmpIfObjectInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_257_fade_in_from_black_async_0"]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=63, z=0, direction=EAST),
		A_FaceSouthwest()
	], identifier="EVENT_382_action_queue_64"),
	FadeInFromBlack(sync=False),
	Return()
])
