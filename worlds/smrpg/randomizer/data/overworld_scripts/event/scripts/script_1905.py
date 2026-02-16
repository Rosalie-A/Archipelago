# E1905_ABYSS_EXIT_TO_BOSS_2_ROOM
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
	JmpIfBitSet(ABYSS_BOSS_2_DEFEATED, ["EVENT_1905_enter_area_9"]),
	RemoveObjectFromCurrentLevel(MARIO),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(50),
	FadeOutToBlack(sync=True, duration=180),
	PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(59),
		A_WalkEastPixels(8),
		A_WalkWestPixels(8),
		A_EndLoop()
	]),
	EnterArea(room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, face_direction=SOUTH, x=23, y=54, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, face_direction=SOUTH, x=23, y=54, z=0, identifier="EVENT_1905_enter_area_9"),
	FadeInFromBlack(sync=True),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=24, y=54, z=18, direction=EAST),
		A_JumpToHeight(height=0, silent=True)
	]),
	Return()
])
