# E3773_HOT_SPRINGS_EJECT_FROM_WATER
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
	FreezeCamera(),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=17, y=114),
		A_FaceSouth()
	]),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=142, row=8),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=80, silent=True),
		A_WalkSouthwestPixels(8),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_Pause(1, identifier="EVENT_3773_action_queue_5_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_3773_action_queue_5_SUBSCRIPT_pause_6"]),
		A_Pause(30),
		A_ResetProperties(),
		A_StartLoopNTimes(19),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=15, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=12, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(50),
		A_ResetProperties()
	]),
	PaletteSet(palette_set=84, row=1, bit_3=True, identifier="hot_spring_reset_palette"),
	UnfreezeCamera(),
	Return()
])
