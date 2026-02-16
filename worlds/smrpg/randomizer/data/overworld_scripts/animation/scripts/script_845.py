#A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE
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
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_Pause(32),
	A_JmpIfRandom1of2(["ACTION_845_pause_6"]),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Jmp(["ACTION_845_pause_8"]),
	A_Pause(1, identifier="ACTION_845_pause_6"),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(48, identifier="ACTION_845_pause_8"),
	A_JmpIfRandom1of2(["ACTION_845_start_loop_n_times_23"], identifier="ACTION_845_jmp_if_random_above_128_9"),
	A_StartLoopNTimes(2),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_EndLoop(),
	A_Jmp(["ACTION_845_jmp_if_random_above_128_9"]),
	A_StartLoopNTimes(2, identifier="ACTION_845_start_loop_n_times_23"),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(4),
	A_EndLoop(),
	A_Jmp(["ACTION_845_jmp_if_random_above_128_9"])
])
