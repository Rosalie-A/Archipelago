#A0657_PIPE_VAULT_THWOMP
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
	A_ShadowOn(identifier="ACTION_657_shadow_on_0"),
	A_SetWalkingSpeed(NORMAL),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_ClearBit(TEMP_7043_4),
	A_ShiftZUpPixels(10),
	A_ShiftZUpPixels(6),
	A_ShiftZUpSteps(4),
	A_JmpIfRandom1of2(["ACTION_657_pause_9"]),
	A_Pause(60),
	A_Pause(30, identifier="ACTION_657_pause_9"),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownSteps(4),
	A_SetBit(TEMP_7043_4),
	A_DecZCoord1Step(),
	A_PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
	A_SetBit(TEMP_7043_1),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_Pause(2),
	A_ClearBit(TEMP_7043_1),
	A_Pause(28),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Jmp(["ACTION_657_shadow_on_0"])
])
