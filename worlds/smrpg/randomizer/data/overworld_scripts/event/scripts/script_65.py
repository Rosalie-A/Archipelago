# E0065_TRAMPOLINE_SUBROUTINE
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
	PauseScriptIfMenuOpen(),
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_65_action_queue_6"]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(36),
		A_SetSequenceSpeed(FAST),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_FloatingOff(),
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
		A_JumpToHeight(height=256, silent=True),
		A_FloatingOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Pause(6),
	Return(),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(24),
		A_SetSequenceSpeed(NORMAL),
		A_ResetProperties(),
		A_SequenceLoopingOff()
	], identifier="EVENT_65_action_queue_6"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(14),
		A_Pause(8),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=108, silent=True),
		A_FloatingOn(),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_Walk1StepSouth(),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	RememberLastObject(),
	ClearBit(DIRECTIONAL_7049_0),
	MoveScriptToMainThread(),
	ReturnAll()
])
