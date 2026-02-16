# E1698_BANDITS_WAY_4_LOADER
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
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	SetVarToConst(TEMP_70AB, 22),
	StartLoopNTimes(3),
	SummonObjectToSpecificLevel(MEM_70AB, R078_BANDITS_WAY_AREA_04),
	SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	Pause(1),
	PauseActionScript(MEM_70AB),
	Inc(TEMP_70AB),
	EndLoop(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftZDownPixels(2)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShiftZDownPixels(2)
	]),
	SetVarToConst(TEMP_702C, 26),
	SetVarToConst(TEMP_70A9, 26),
	SetVarToConst(TEMP_70AA, 27),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b'\xfd$\x11\x12')),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A)
	]),
	PauseActionScript(NPC_9),
	SetSyncActionScript(MEM_70AA, A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT),
	Pause(2),
	SetSyncActionScript(NPC_9, A0653_SLOW_ROTATING_PLATFORM),
	RunBackgroundEvent(event_id=E1699_BANDITS_WAY_4_LOADER_BACKGROUND, return_on_level_exit=True),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_4_VIEWED, ["EVENT_1698_action_queue_32"]),
	ResumeActionScript(NPC_2),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ResumeActionScript(NPC_5),
	RunEventAsSubroutine(E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
	Pause(3),
	PauseActionScript(NPC_7),
	Return(),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True)
	], identifier="EVENT_1698_action_queue_32"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(5),
		A_WalkNorthSteps(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNortheastSteps(2),
		A_Walk1StepNorth(),
		A_FaceNortheast()
	]),
	SetBit(BANDITS_WAY_CUTSCENE_4_VIEWED),
	RunEventAsSubroutine(E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
	PauseActionScript(NPC_6),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ShadowOn(),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_WalkNortheastPixels(1),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(8),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	Pause(80),
	StartLoopNTimes(1),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(108),
		A_Pause(27)
	]),
	ResumeActionScript(NPC_7),
	Pause(80),
	EndLoop(),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(108),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FAST),
		A_WalkEastPixels(4),
		A_ShadowOff(),
		A_WalkEastPixels(2, identifier="EVENT_1698_action_queue_48_SUBSCRIPT_shift_east_pixels_6"),
		A_JmpIfObjectInAir(NPC_12, ["EVENT_1698_action_queue_48_SUBSCRIPT_shift_east_pixels_6"]),
		A_FixedFCoordOff()
	]),
	Jmp(["EVENT_1698_action_queue_51"]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(20),
		A_WalkSouthwestSteps(3),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetAllSpeeds(FAST),
		A_FaceSoutheast(),
		A_Pause(30),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(112),
		A_FixedFCoordOn(),
		A_WalkEastSteps(4),
		A_VisibilityOff()
	], identifier="EVENT_1698_action_queue_51"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True)
	]),
	ResumeActionScript(NPC_2),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ResumeActionScript(NPC_5),
	Return()
])
