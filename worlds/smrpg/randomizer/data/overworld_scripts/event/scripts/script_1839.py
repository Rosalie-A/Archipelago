# E1839_UNKNOWN
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
	RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1839_ret_7"]),
	SetBit(TEMP_7043_1),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(8),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_Jmp(["EVENT_1839_non_embedded_action_queue_8"])
	]),
	Return(identifier="EVENT_1839_ret_7"),
	NonEmbeddedActionQueue(required_offset=0x22, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_ShiftZUpSteps(2),
		A_ShiftZDownSteps(4),
		A_WalkNortheastSteps(4),
		A_ShiftZUpSteps(7),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(6),
		A_ShiftZUpSteps(3),
		A_WalkSouthwestSteps(6),
		A_WalkNortheastSteps(10),
		A_ShiftZUpSteps(4),
		A_ShiftZDownSteps(4),
		A_WalkNorthwestSteps(2),
		A_ShiftZDownSteps(4),
		A_WalkSoutheastSteps(2),
		A_ShiftZUpSteps(2),
		A_PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(6),
		A_ShiftZDownSteps(2),
		A_WalkSouthwestSteps(9),
		A_ShiftZUpSteps(4),
		A_PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
		A_Pause(60),
		A_Jmp(["EVENT_1839_non_embedded_action_queue_8"])
	], identifier="EVENT_1839_non_embedded_action_queue_8")
])
