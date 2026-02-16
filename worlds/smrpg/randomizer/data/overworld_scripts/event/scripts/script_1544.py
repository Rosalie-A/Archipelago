# E1544_SAND_WHIRLPOOL
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
	FreezeAllNPCsUntilReturn(),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
	SetSyncActionScript(MARIO, A0781_PLAYER_SPINS_ON_FLOWER),
	Pause(1),
	ActionQueueSync(target=MARIO, subscript=[
		A_Inc(PRIMARY_TEMP_700C),
		A_FixedFCoordOff(),
		A_FaceEast7C(),
		A_FixedFCoordOn()
	], identifier="EVENT_1544_action_queue_7"),
	Pause(2),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1544_action_queue_7"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1544_action_queue_7"]),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=9, duration=6, bit_6=True, bit_7=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO112_DRAINING_WATER, channel=4),
		A_FixedFCoordOff(),
		A_SetVarToConst(PRIMARY_TEMP_700C, 2),
		A_StartLoopNTimes(15),
		A_Inc(PRIMARY_TEMP_700C),
		A_FaceEast7C(),
		A_VisibilityOn(),
		A_WalkFDirectionPixels(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop()
	]),
	FadeOutToBlack(sync=False, duration=30),
	Return()
])
