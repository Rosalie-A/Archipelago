# E1358_CURTAIN_GAME_BEGINS_NPCS_WALK_INTO_ROOM
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
	RemoveObjectFromSpecificLevel(NPC_6, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	RemoveObjectFromSpecificLevel(NPC_8, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS),
	RemoveObjectFromSpecificLevel(NPC_4, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	RemoveObjectFromSpecificLevel(NPC_0, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM),
	MoveScriptToBackgroundThread2(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(70),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(5),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(70),
		A_Pause(40),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(3),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(70),
		A_Pause(40),
		A_Pause(120),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(1),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(1),
		A_WalkNorthwestSteps(1),
		A_SetAllSpeeds(NORMAL),
		A_Pause(30),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="tower_boss_laughing_seq_1"),
		A_Pause(30),
		A_ResetProperties()
	], identifier="tower_boss_laughing_aqueue_1"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	Jmp(["EVENT_1365_play_music_default_volume_0"], identifier="EVENT_1358_jmp_13")
])
