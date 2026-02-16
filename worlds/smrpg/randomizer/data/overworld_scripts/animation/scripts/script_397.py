#A0397_PLAYER_TUMBLES_DOWN_BOOSTER_PASS
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
	A_FloatingOff(),
	A_OverwriteSolidity(),
	A_ShadowOn(),
	A_SetWalkingSpeed(FASTER),
	A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_PlaySound(sound=SO048_MINECART_START, channel=4),
	A_WalkSouthwestSteps(3),
	A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_FloatingOn(),
	A_ShadowOff(),
	A_WalkSouthwestSteps(18),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthPixels(8),
	A_SetSpriteSequence(index=1, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_ClearBit(DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING),
	A_SetBit(TEMP_7043_0),
	A_ReturnQueue()
])
