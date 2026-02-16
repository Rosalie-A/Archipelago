# E3494_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ANIMATION_AND_EXIT
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
	RunBackgroundEvent(event_id=E3497_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ITEM_GRANTER, return_on_level_exit=True),
	FadeInFromBlack(sync=True),
	FreezeCamera(),
	SetSyncActionScript(MARIO, A0601_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_PLAYER_OUTER),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(220),
		A_SetWalkingSpeed(NORMAL),
		A_WalkWestSteps(4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(7),
		A_Walk1StepNorthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	MoveScriptToBackgroundThread2(),
	JmpToSubroutine(["EVENT_3491_action_queue_16"]),
	MoveScriptToMainThread(),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=4, y=83, z=0),
	FadeOutMusicToVolume(duration=1, volume=56),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=4, y=76),
		A_SetVarToConst(X_COORD_2, 1408),
		A_SetVarToConst(Y_COORD_2, 8576),
		A_TransferTo70167018()
	]),
	JmpToSubroutine(["EVENT_3480_action_queue_40"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(8),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x80\x02\xe4\xff')),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_WalkSoutheastSteps(3),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
	Jmp(["EVENT_3489_enable_controls_3"]),
	Return()
])
