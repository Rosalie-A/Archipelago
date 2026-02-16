# E1086_MELODY_BAY_SWIM_ANIMATION
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
	PauseActionScript(MARIO),
	UnfreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(64),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\x00\xff')),
		A_Pause(16),
		A_BPL262728()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
		A_Pause(10),
		A_WalkToXYCoords(x=15, y=32)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(10),
		A_JumpToHeight(64),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\x00\xff')),
		A_Pause(16),
		A_BPL262728()
	]),
	Return()
])
