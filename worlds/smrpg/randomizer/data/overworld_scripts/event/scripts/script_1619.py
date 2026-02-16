# E1619_OCCUPIED_MOLEVILLE_EXTERIOR_NPC_TRIGGER_CUTSCENE
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
	PauseActionScript(NPC_0),
	RunDialog(dialog_id=DI1095_MOLEVILLE_NPC_BEFORE_CLEAR, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitClear(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_1619_jmp_if_bit_set_4"]),
	RunDialog(dialog_id=DI1051_MOLEVILLE_CLOSED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(MOLE_DESCENDED, ["EVENT_1619_resume_action_script_17"], identifier="EVENT_1619_jmp_if_bit_set_4"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetAllSpeeds(NORMAL),
		A_StartLoopNTimes(1),
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_Pause(16),
		A_FixedFCoordOff(),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_FaceNortheast(),
		A_EndLoop()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=14, y=27, height=0)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkEastSteps(2),
		A_FaceSoutheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest7D(arg=0x15)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSequenceSpeed(FAST),
		A_StartLoopNTimes(3),
		A_JumpToHeight(48),
		A_Pause(20),
		A_EndLoop(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	RunDialog(dialog_id=DI1098_MOLEVILLE_CUTSCENE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_StartLoopNTimes(3),
		A_JumpToHeight(48),
		A_Pause(20),
		A_EndLoop(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	RunDialog(dialog_id=DI1099_MOLEVILLE_CUTSCENE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOn()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOn()
	]),
	SetSyncActionScript(NPC_1, A0648_MOLEVILLE_WOMAN_NEAR_MOUNTAIN),
	SetBit(MOLE_DESCENDED),
	ResumeActionScript(NPC_0, identifier="EVENT_1619_resume_action_script_17"),
	Return()
])
