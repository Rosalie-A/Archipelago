# E1622_BUCKET_WARP
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
	Set7000ToTappedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1622_ret_12"]),
	Set7000ToPressedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1622_ret_12"]),
	PlaySound(sound=SO032_UNDERGROUND_WARP, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_sequence=True, looping=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=3, y=62),
		A_StartLoopNTimes(11),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_ShiftZDownPixels(1),
		A_EndLoop()
	]),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=8, duration=4, bit_6=True, bit_7=True),
	JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["EVENT_1622_set_bit_9"]),
	JmpIfBitSet(BUCKET_WARP_ENABLED, ["EVENT_1622_set_bit_13"]),
	SetBit(BUCKET_WARP_BIT, identifier="EVENT_1622_set_bit_9"),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=108, z=0, run_entrance_event=True),
	Return(identifier="EVENT_1622_ret_12"),
	SetBit(BUCKET_WARP_DIRECTIONAL_BIT, identifier="EVENT_1622_set_bit_13"),
	JmpToEvent(E2651_BUCKET_WARP_CHECK_GRANTER)
])
