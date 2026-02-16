# E0389_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_SHYSTER
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
	PlaySound(sound=SO000_SILENCE, channel=6),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	JmpIfObjectNotInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_389_jmp_if_object_not_in_level_11"]),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	RemoveObjectFromSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_2, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_389_jmp_if_object_not_in_level_11"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=25, y=27, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM),
	PauseActionScript(NPC_2),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceNortheast()
	]),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FadeInFromBlack(sync=False),
	JmpIfObjectNotInSpecificLevel(NPC_0, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_389_action_queue_26"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastSteps(4),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_FixedFCoordOff(),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNorth()
	], identifier="EVENT_389_action_queue_22"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouth()
	]),
	RemoveObjectFromSpecificLevel(NPC_2, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM),
	Return(),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_WalkNortheastSteps(6),
		A_VisibilityOff()
	], identifier="EVENT_389_action_queue_26"),
	Jmp(["EVENT_389_action_queue_22"])
])
