# E3200_MINES_TRAMPOLINE
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
	ClearBit(TEMP_7043_1),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_SequencePlaybackOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(36),
		A_SetSequenceSpeed(FAST),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_FloatingOff(),
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
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x10\x80\xff')),
		A_FloatingOn(),
		A_Pause(12),
		A_BPL262728(),
		A_FloatingOff(),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkToXYCoords(x=7, y=49)
	]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	StartAsyncEmbeddedActionScript(target=SCREEN_FOCUS, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(2),
		A_WalkWestPixels(2),
		A_WalkNorthPixels(4),
		A_WalkEastPixels(2),
		A_WalkSouthPixels(1),
		A_WalkWestPixels(1),
		A_WalkSouthPixels(5),
		A_WalkEastPixels(1),
		A_WalkNorthPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL)
	]),
	StartSyncEmbeddedActionScript(target=MEM_70AA, prefix=0xF1, subscript=[
		A_Pause(1, identifier="EVENT_3200_start_embedded_action_script_7_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_1, ["EVENT_3200_start_embedded_action_script_7_SUBSCRIPT_pause_0"]),
		A_ClearBit(TEMP_7043_1),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, looping=False),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_Pause(24),
		A_SetSequenceSpeed(NORMAL),
		A_ResetProperties(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(1, identifier="EVENT_3200_action_queue_8_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_3200_action_queue_8_SUBSCRIPT_pause_3"]),
		A_SetBit(TEMP_7043_1),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_FloatingOff(),
		A_ShiftZDownPixels(8),
		A_Pause(2),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_FloatingOn(),
		A_Walk1StepSouth(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	Pause(48),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(128),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
		A_Pause(24),
		A_SetSequenceSpeed(NORMAL),
		A_ResetProperties(),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_ClearBit(TEMP_7043_1)
	]),
	Return()
])
