# E1912_ABYSS_MACHINE_ARROW_HIT
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
	EnableControls([]),
	SetBit(TEMP_7043_1),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_JumpToHeight(128),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(2),
		A_VisibilityOff(),
		A_ClearBit(TEMP_7043_0)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(3),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO012_DIZZINESS, channel=4),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_sequence=True, looping=True)
	]),
	SetVarToConst(TIMER_701C, 90),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1914_ABYSS_MACHINE_ARROW_RESET, timer_var=TIMER_701C),
	Return()
])
