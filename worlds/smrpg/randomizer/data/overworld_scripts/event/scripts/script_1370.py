# E1370_CURTAIN_GAME_SUCCESS_FAILURE_GENERAL
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
	Pause(30),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_1370_play_sound_1"),
	JmpIfVarEqualsConst(TEMP_7026, 2, ["EVENT_1369_pause_0"]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=40),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=44),
	MoveScriptToBackgroundThread2(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=5, y=19, height=0),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=3, y=20, height=0),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=22, height=0),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=5, y=24, height=0),
		A_FaceNortheast()
	]),
	Pause(20),
	Inc(TEMP_7026),
	Jmp(["EVENT_1358_jmp_13"])
])
