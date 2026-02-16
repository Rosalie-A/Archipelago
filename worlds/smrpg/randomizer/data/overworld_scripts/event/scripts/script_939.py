# E0939_STATUE_SUBROUTINE_1
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

script = EventScript([
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=2, y=56),
		A_WalkSouthwestPixels(5),
		A_WalkSoutheastPixels(16),
		A_SequencePlaybackOff(),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_VisibilityOn(),
		A_Pause(31),
		A_SetSpriteSequence(index=5, is_mold=True, looping=True, mirror_sprite=True, identifier="statue_keeper_introduced_1"),
		A_Pause(31),
		A_SetSequenceSpeed(SLOW),
		A_SequencePlaybackOn(),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=4, looping=False, mirror_sprite=True, identifier="statue_keeper_introduced_2"),
		A_Pause(66),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(17)
	], identifier="statue_keeper_introduced_aq"),
	Return()
])
