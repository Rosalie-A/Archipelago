# E0617_MARIO_AS_BELLHOP_MAIN_EVENT
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
	Set7000ToObjectCoord(target_npc=NPC_5, coord=COORD_Y, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 63, ["EVENT_617_enable_controls_until_return_3"]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_FaceNorthwest()
	]),
	EnableControlsUntilReturn([], identifier="EVENT_617_enable_controls_until_return_3"),
	Pause(60),
	JmpIfRandom1of2(["EVENT_617_action_queue_10"]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=64, z=0, direction=EAST),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW)
	]),
	SetVarToConst(TEMP_70A9, 27),
	SetVarToConst(TEMP_70B8, 1),
	Jmp(["EVENT_617_pause_13"]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=6, y=64, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW)
	], identifier="EVENT_617_action_queue_10"),
	SetVarToConst(TEMP_70A9, 26),
	SetVarToConst(TEMP_70B8, 3),
	Pause(120, identifier="EVENT_617_pause_13"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI1005_PLAYER_ESCORTS_GUEST, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouth()
	]),
	ClearBit(TEMP_7042_4),
	ClearBit(TEMP_7042_5),
	ClearBit(TEMP_7042_6),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_617_set_action_script_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_617_set_action_script_31"]),
	SetSyncActionScript(NPC_7, A0321_BELLHOP_FACE_PLAYER),
	Return(),
	SetSyncActionScript(NPC_8, A0321_BELLHOP_FACE_PLAYER, identifier="EVENT_617_set_action_script_28"),
	SetSyncActionScript(NPC_9, A0321_BELLHOP_FACE_PLAYER),
	Return(),
	SetSyncActionScript(NPC_6, A0321_BELLHOP_FACE_PLAYER, identifier="EVENT_617_set_action_script_31"),
	Return()
])
