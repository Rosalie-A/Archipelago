# E2544_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_LOADER
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
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	FreezeCamera(),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2544_apply_tile_mod_5"]),
	SetBit(TEMP_7043_0),
	ApplyTileModToLevel(use_alternate=True, room_id=R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, mod_id=0, identifier="EVENT_2544_apply_tile_mod_5"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_2544_action_queue_6_SUBSCRIPT_shift_z_up_steps_4"]),
		A_WalkNorthwestPixels(8),
		A_FaceSouth(),
		A_ShiftZUpSteps(11, identifier="EVENT_2544_action_queue_6_SUBSCRIPT_shift_z_up_steps_4"),
		A_SetWalkingSpeed(NORMAL),
		A_ClearBit(TEMP_7043_0)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(8),
		A_FaceNortheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(8),
		A_FaceNortheast(),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_2544_action_queue_11_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2544_action_queue_11_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_Pause(24)
	]),
	UnfreezeCamera(),
	Return()
])
