# E1545_SAND_WHIRLPOOL
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
	Set7016701BToObjectXYZ(target=MEM_70A8, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FASTEST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FixedFCoordOff(),
		A_UnknownCommand(bytearray(b'\x98')),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(NORMAL)
	]),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=9, duration=0, bit_6=False, bit_7=False),
	FadeInFromBlack(sync=True, duration=40),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=0, duration=6, bit_6=True, bit_7=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_Pause(30),
		A_ResetProperties(),
		A_VisibilityOn(),
		A_JumpToHeight(108),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_Walk1StepFDirection()
	]),
	SetBit(TEMP_7044_6),
	Return()
])
