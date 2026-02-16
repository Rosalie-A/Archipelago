#A0524_TOWER_SNIFIT_RIGHT_VISITOR
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SequenceLoopingOff(identifier="ACTION_524_sequence_looping_off_0"),
	A_JmpIfObjectNotInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	A_Pause(120),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(NORMAL),
	A_JmpIfObjectNotInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	A_Pause(120),
	A_SequenceLoopingOff(),
	A_JmpIfObjectNotInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	A_Pause(120),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(60),
	A_SequenceLoopingOff(),
	A_Pause(60),
	A_JmpIfObjectNotInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	A_JumpToHeight(64),
	A_Pause(15),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(FAST),
	A_Pause(45),
	A_SequenceLoopingOff(),
	A_Pause(30),
	A_FaceSouthwest(),
	A_Pause(30),
	A_FaceNorthwest(),
	A_Pause(60),
	A_Jmp(["ACTION_524_sequence_looping_off_0"]),
	A_SequenceLoopingOff(identifier="ACTION_524_sequence_looping_off_28"),
	A_Pause(60),
	A_FaceSouthwest(),
	A_Pause(15),
	A_FaceNorthwest(),
	A_Pause(15),
	A_FaceSouthwest(),
	A_Pause(15),
	A_FaceNorthwest(),
	A_Pause(15),
	A_FaceSouthwest(),
	A_Pause(15),
	A_SetWalkingSpeed(VERY_FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkNortheastSteps(1),
	A_WalkNorthwestSteps(12),
	A_WalkToXYCoords(x=22, y=101),
	A_FaceNorthwest(),
	A_FixedFCoordOn(),
	A_SequencePlaybackOff(),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestPixels(2, identifier="ACTION_524_shift_southwest_pixels_49"),
	A_WalkNortheastPixels(2),
	A_Jmp(["ACTION_524_shift_southwest_pixels_49"])
])
