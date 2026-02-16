# E2391_BEANSTALK_FROM_INSIDE_GARDENERS_HOUSE
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
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FloatingOff(),
		A_ShadowOn(),
		A_OverwriteSolidity(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_TransferToXYZF(x=26, y=17, z=5, direction=EAST),
		A_WalkWestPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_Pause(4),
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$ \x00\x00\x00')),
		A_ShiftZUpSteps(10),
		A_BPL262728()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthSteps(5)
	]),
	Pause(112),
	FadeOutToBlack(sync=False, duration=32),
	SetBit(TEMP_GARDENER_EXTERIOR_2),
	EnterArea(room_id=R417_GARDENERS_HOUSE_OUTSIDE, face_direction=SOUTH, x=8, y=87, z=3, run_entrance_event=True),
	Return()
])
