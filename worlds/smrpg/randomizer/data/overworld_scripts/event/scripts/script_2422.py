# E2422_ABYSS_ROOM_BEFORE_1ST_BOSS_LOWER_TRAMPOLINE
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
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, looping=False, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_ShadowOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(8)
	]),
	SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
	PlaySound(sound=SO010_TRAMPOLINE, channel=6),
	SetBit(TEMP_7043_0),
	ClearBit(DIRECTIONAL_7045_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_ShiftToXYCoords(x=23, y=53),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(2),
		A_WalkSoutheastPixels(5),
		A_FaceNorthwest(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xc0\xff\x80\xfe')),
		A_UnknownCommand(bytearray(b'%\x00\t\x80\xff')),
		A_Pause(32),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
