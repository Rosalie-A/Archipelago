# E3478_MIDAS_RIVER_TRAMPOLINE
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
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3478_action_queue_7"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	ClearBit(TEMP_7043_0),
	ClearBit(UNKNOWN_MIDAS_RIVER_7079_1),
	ClearBit(UNKNOWN_MIDAS_RIVER_704D_6),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=108, z=0, run_entrance_event=True),
	Return(),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, looping=False),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(36),
		A_SetSequenceSpeed(FAST),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_Pause(5),
		A_SequenceLoopingOff()
	], identifier="EVENT_3478_action_queue_7"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(3),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(1),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(2),
		A_Pause(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(1),
		A_Pause(9),
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOn(),
		A_JumpToHeight(height=96, silent=True),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkToXYCoords(x=21, y=35),
		A_JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3478_jmp_if_bit_set_9"]),
		A_FaceWest()
	]),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3478_ret_14"], identifier="EVENT_3478_jmp_if_bit_set_9"),
	Pause(20),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceSoutheast(),
		A_SetAllSpeeds(FAST),
		A_StartLoopNTimes(2),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_WalkSoutheastSteps(2),
		A_WalkEastPixels(16),
		A_FaceSoutheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	RunEventAsSubroutine(E3479_MIDAS_RIVER_SCORE_SUBMISSION),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkWestPixels(16),
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	Return(identifier="EVENT_3478_ret_14")
])
