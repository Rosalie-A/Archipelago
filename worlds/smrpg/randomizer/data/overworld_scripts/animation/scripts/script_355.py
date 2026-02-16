#A0355_PLAYER_IN_FOREST_1ST_TRUNK
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
	A_JmpToSubroutine(["ACTION_355_shadow_on_3"]),
	A_WalkToXYCoords(x=16, y=24),
	A_Jmp(["ACTION_355_set_animation_speed_10"]),
	A_ShadowOn(identifier="ACTION_355_shadow_on_3"),
	A_FaceSouth(),
	A_FixedFCoordOn(),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	A_SetWalkingSpeed(FAST),
	A_ReturnQueue(),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_355_set_animation_speed_10"),
	A_SetSolidityBits(cant_pass_walls=True),
	A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
	A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_DecZCoord1Step(),
	A_SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	A_ResetProperties(),
	A_FixedFCoordOff(),
	A_ReturnQueue()
])
