# E1537_SPINNING_FLOWER_CORE_LOGIC
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
	JmpIfBitClear(SPINNING_FLOWER_1, ["EVENT_1537_set_bit_2"]),
	Return(),
	SetBit(SPINNING_FLOWER_1, identifier="EVENT_1537_set_bit_2"),
	MoveScriptToBackgroundThread2(),
	CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2),
	VarShiftLeft(X_COORD_2, 8),
	SetAsyncActionScript(MARIO, A0781_PLAYER_SPINS_ON_FLOWER),
	SetVarToConst(TEMP_70AE, 0),
	PlaySound(sound=SO031_SPINNING_FLOWER, channel=6, identifier="EVENT_1537_play_sound_8"),
	StartLoopNTimes(15),
	Pause(1),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1537_set_action_script_18"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_TurnClockwise45DegreesNTimes(1)
	]),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 40, ["EVENT_1537_set_action_script_23"]),
	Jmp(["EVENT_1537_play_sound_8"]),
	SetAsyncActionScript(MARIO, A0820_JUMP_OFF_SPINNING_FLOWER, identifier="EVENT_1537_set_action_script_18"),
	ClearBit(SPINNING_FLOWER_1),
	ClearBit(SPINNING_FLOWER_2),
	MoveScriptToMainThread(),
	Return(),
	SetSyncActionScript(MARIO, A0165_FALL_OFF_SPINNING_FLOWER, identifier="EVENT_1537_set_action_script_23"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOff(),
		A_TurnClockwise45DegreesNTimes(1),
		A_FixedFCoordOn()
	], identifier="EVENT_1537_action_queue_24"),
	Pause(6),
	JmpIfObjectActionScriptIsRunning(MARIO, ["EVENT_1537_action_queue_24"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOn(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(40),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(1, identifier="EVENT_1537_pause_28"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1537_action_queue_32"]),
	Jmp(["EVENT_1537_pause_28"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth(),
		A_JumpToHeight(108)
	], identifier="EVENT_1537_action_queue_32"),
	ClearBit(SPINNING_FLOWER_1),
	ClearBit(SPINNING_FLOWER_2),
	MoveScriptToMainThread(),
	Return()
])
