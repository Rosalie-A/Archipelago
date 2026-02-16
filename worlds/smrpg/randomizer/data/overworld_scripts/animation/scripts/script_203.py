#A0203_SHIP_PASSWORD_BOSS_REVEAL
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_203_set_animation_speed_18"]),
	A_VisibilityOff(),
	A_WalkEastPixels(6),
	A_ShiftZUpPixels(5),
	A_ResetProperties(),
	A_FaceSouthwest(),
	A_Pause(60),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=False, identifier="password_boss_reveal_sequence"),
	A_Pause(16),
	A_PlaySound(sound=SO118_BECKONING_TENTACLE, channel=4),
	A_Pause(56),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="password_boss_vanilla_1"),
	A_Pause(60),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False, identifier="password_boss_vanilla_2"),
	A_Pause(24),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_203_set_animation_speed_18"),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepFDirection(),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_203_set_animation_speed_18"]),
	A_FaceMario(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(VERY_FAST),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_203_set_animation_speed_18"])
])
