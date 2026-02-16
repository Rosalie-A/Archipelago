# E2346_TOWER_THWOMP_SEESAW_CONTD
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
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	SetSyncActionScript(NPC_1, A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
		A_JumpToHeight(128),
		A_Pause(32)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftZUpPixels(4)
	]),
	Pause(1),
	SetAsyncActionScript(NPC_1, A0739_TOWER_SEESAW_CHEST_ITEM),
	JmpIfMarioInAir(["EVENT_2346_clear_bit_9"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_2346_enable_controls_11"]),
	ClearBit(TEMP_7043_0, identifier="EVENT_2346_clear_bit_9"),
	Return(),
	EnableControls([], identifier="EVENT_2346_enable_controls_11"),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(384)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_ShiftZUpSteps(16)
	]),
	Pause(32),
	FadeOutToBlack(sync=False, duration=16),
	SetBit(DIRECTIONAL_7045_0),
	EnterArea(room_id=R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, face_direction=SOUTHEAST, x=3, y=53, z=0, run_entrance_event=True),
	Return()
])
