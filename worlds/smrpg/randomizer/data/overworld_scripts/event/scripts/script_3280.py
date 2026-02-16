# E3280_SHIP_LOWER_HENCHMAN_ROOM_LOADER
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
	JmpIfBitSet(SHIP_PRE_BOSS_BATTLE_1_CLEARED, ["EVENT_3280_jmp_to_event_48"]),
	SetSyncActionScript(NPC_4, A0015_DO_NOTHING),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferXYZFSteps(x=0, y=0, z=25, direction=NORTHEAST)
	]),
	RunEventAsSubroutine(E0803_SHIP_1ST_PREBOSS_BATTLE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(20),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(3),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(8),
		A_FaceMario(),
		A_Walk1StepSouth(),
		A_FaceMario()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceMario()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorth()
	]),
	JmpIfBitSet(UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5, ["EVENT_3280_action_queue_11"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(3),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3280_action_queue_11"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkToXYCoords(x=3, y=125),
		A_FaceMario()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkToXYCoords(x=4, y=122),
		A_FaceMario(),
		A_WalkToXYCoords(x=3, y=123)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkToXYCoords(x=2, y=123),
		A_FaceMario()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkToXYCoords(x=3, y=122),
		A_FaceMario()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(40),
		A_TurnClockwise45DegreesNTimes(255),
		A_Pause(2),
		A_TurnClockwise45DegreesNTimes(255),
		A_Pause(12),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(12),
		A_TurnClockwise45DegreesNTimes(255),
		A_Pause(2),
		A_TurnClockwise45DegreesNTimes(255)
	]),
	SetSyncActionScript(NPC_4, A0014_FLOATING_CHEST),
	JmpIfBitSet(UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5, ["EVENT_3280_run_event_as_subroutine_23"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(height=48, silent=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(height=48, silent=True)
	]),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR, identifier="EVENT_3280_run_event_as_subroutine_23"),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3280_set_bit_49"]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=48, silent=True),
		A_JumpToHeight(height=48, silent=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_FaceNorthwest(),
		A_FaceNorth(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(13),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(11),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(20),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(4),
		A_WalkNortheastSteps(11),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(20),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(10),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_0, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL),
	RemoveObjectFromSpecificLevel(NPC_1, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL),
	RemoveObjectFromSpecificLevel(NPC_2, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL),
	RemoveObjectFromSpecificLevel(NPC_3, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL),
	SetBit(SHIP_PRE_BOSS_BATTLE_1_CLEARED),
	ClearBit(UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5),
	Return(),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3280_jmp_to_event_48"),
	SetBit(UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5, identifier="EVENT_3280_set_bit_49"),
	RunEventAtReturn(E3306_SHIP_LOWER_HENCHMAN_ROOM_LOADER_CONTINUED),
	Return()
])
