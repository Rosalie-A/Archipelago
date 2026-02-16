# E1694_TEMPLE_ELEVATOR
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
	JmpIfBitSet(TEMPLE_ELEVATOR_DIRECTION, ["EVENT_1694_set_7016_to_object_xyz_3"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1694_set_7016_to_object_xyz_3"]),
	Return(),
	Set7016701BToObjectXYZ(target=MEM_70A8, identifier="EVENT_1694_set_7016_to_object_xyz_3"),
	AddConstToVar(X_COORD_2, 48),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=48, silent=True),
		A_Pause(3),
		A_TransferTo70167018(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouth(),
		A_SetPriority(2)
	]),
	JmpToSubroutine(["EVENT_1694_play_sound_18"]),
	JmpIfBitSet(TEMPLE_ELEVATOR_DIRECTION, ["EVENT_1694_action_queue_13"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkSouthSteps(16)
	]),
	JmpToSubroutine(["EVENT_1694_stop_sound_24"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOff(),
		A_Walk1StepSoutheast(),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetBit(TEMPLE_ELEVATOR_DIRECTION),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNorthSteps(16)
	], identifier="EVENT_1694_action_queue_13"),
	JmpToSubroutine(["EVENT_1694_stop_sound_24"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOff(),
		A_Walk1StepNorthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ClearBit(TEMPLE_ELEVATOR_DIRECTION),
	Return(),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6, identifier="EVENT_1694_play_sound_18"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(8),
	PlaySound(sound=SO048_MINECART_START, channel=6),
	Return(),
	StopSound(identifier="EVENT_1694_stop_sound_24"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
	]),
	Pause(4),
	PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	Return()
])
