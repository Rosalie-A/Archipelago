# E1647_MOLEVILLE_MINECART_FREEPLAY_ENTRANCE
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
	JmpIfBitClear(PAID_FOR_MINECART, ["EVENT_1647_jmp_if_bit_set_14"]),
	Pause(20),
	PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_Pause(8)
	]),
	RemoveObjectFromCurrentLevel(MARIO),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(30),
	FadeOutToBlack(sync=False, duration=48),
	EnterArea(room_id=R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING, face_direction=SOUTH, x=19, y=27, z=12),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	Return(),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1647_ret_19"], identifier="EVENT_1647_jmp_if_bit_set_14"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_BounceToXYWithHeight(x=20, y=39, height=20),
		A_FaceWest()
	]),
	SetSyncActionScript(NPC_2, A0040_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_WATER_DROPLETS),
	RunDialog(dialog_id=DI1135_TRY_TO_SNEAK_INTO_MINECART, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7044_3),
	Return(identifier="EVENT_1647_ret_19")
])
