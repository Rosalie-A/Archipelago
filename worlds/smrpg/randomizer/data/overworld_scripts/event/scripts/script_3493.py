# E3493_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT
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
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_2, ["EVENT_3493_fade_in_from_black_sync_2"]),
	RunBackgroundEvent(event_id=E3496_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT_BACKGROUND, return_on_level_exit=True),
	FadeInFromBlack(sync=True, identifier="EVENT_3493_fade_in_from_black_sync_2"),
	FreezeCamera(),
	SetSyncActionScript(MARIO, A0600_MIDAS_RIVER_MID_RIGHT_TUNNEL_PLAYER_OUTER),
	SetSyncActionScript(SCREEN_FOCUS, A0647_MIDAS_MID_RIGHT_TUNNEL_CAMERA),
	JmpToSubroutine(["EVENT_3491_action_queue_16"]),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=56, z=0),
	FadeOutMusicToVolume(duration=1, volume=56),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=12, y=67),
		A_SetVarToConst(X_COORD_2, 6528),
		A_SetVarToConst(Y_COORD_2, 8320),
		A_TransferTo70167018()
	]),
	JmpToSubroutine(["EVENT_3480_action_queue_40"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthPixels(32),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x80\x02\xf2\xff')),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_WalkNorthwestSteps(6),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
	Jmp(["EVENT_3489_enable_controls_3"]),
	Return()
])
