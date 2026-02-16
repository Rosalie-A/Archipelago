# E3766_BEAN_VALLEY_LOWER_CHEST_ROOM_FALL_TO_HOT_SPRINGS_MEZZANINE
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
	EnterArea(room_id=R374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH, face_direction=SOUTH, x=27, y=115, z=4),
	EnableControls([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x00')),
		A_AddConstToVar(Z_COORD_2, 2304),
		A_UnknownCommand(bytearray(b'\x99')),
		A_JumpToHeight(height=0, silent=True)
	]),
	FadeInFromBlack(sync=True),
	Pause(24),
	PauseScriptUntilEffectDone(),
	SetBit(TEMP_704A_2),
	EnterArea(room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS, face_direction=SOUTH, x=20, y=50, z=0, run_entrance_event=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=20, y=50, z=0, direction=SOUTHEAST),
		A_VisibilityOn(),
		A_FloatingOn()
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3766_action_queue_10_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_3766_action_queue_10_SUBSCRIPT_pause_0"]),
		A_BPL262728(),
		A_JumpToHeight(height=80, silent=True)
	]),
	SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(8)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
