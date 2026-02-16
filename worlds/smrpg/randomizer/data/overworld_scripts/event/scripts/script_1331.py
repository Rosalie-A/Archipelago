# E1331_TOWER_BREAK_DOWN_DOOR
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
	JmpIfBitSet(TOWER_OPENED, ["EVENT_1331_ret_20"]),
	JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["EVENT_1331_ret_20"]),
	RemoveObjectFromCurrentLevel(NPC_1),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=4, y=114),
		A_FaceEast(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(25),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=5, y=115),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(15),
		A_FaceSouthwest(),
		A_Pause(15),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(15),
		A_SetSequenceSpeed(FAST),
		A_Pause(15),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(45),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(18),
		A_WalkSouthwestPixels(12),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(6),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4)
	]),
	Pause(5),
	ApplySolidityModToLevel(permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=32),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromSpecificLevel(NPC_2, R202_BOOSTER_TOWER_ENTRANCE),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(60),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=5, y=116),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(NORMAL),
		A_WalkToXYCoords(x=5, y=116),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	SetBit(TOWER_OPENED),
	Return(identifier="EVENT_1331_ret_20")
])
