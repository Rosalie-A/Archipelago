# E3480_MIDAS_RIVER_WATERFALL_LOADER
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
	EnableControls([]),
	FadeOutMusicToVolume(duration=0, volume=8),
	FadeOutSoundToVolume(duration=0, volume=0),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	FadeOutSoundToVolume(duration=2, volume=127),
	SetVarToConst(TEMP_70A9, 32),
	SetVarToConst(X_COORD_2, 4480),
	SetVarToConst(Y_COORD_2, 256),
	SetVarToConst(Z_COORD_2, 0),
	StartLoopNTimes(2),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	AddConstToVar(X_COORD_2, 128),
	AddConstToVar(Y_COORD_2, 64),
	Inc(TEMP_70A9),
	EndLoop(),
	SetVarToConst(X_COORD_2, 4608),
	SetVarToConst(Y_COORD_2, 512),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	FadeInFromBlack(sync=True, duration=80),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3480_jmp_if_bit_set_23"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3480_jmp_if_bit_set_23"]),
	RunEventAsSubroutine(E3892_MIDAS_RIVER_STAR_PIECE_SIGNAL),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3480_action_queue_26"], identifier="EVENT_3480_jmp_if_bit_set_23"),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704D_6, ["EVENT_3480_action_queue_26"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(148),
		A_ShiftToXYCoords(x=6, y=73),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(27),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(34),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_3480_action_queue_26"),
	FadeOutMusicToVolume(duration=1, volume=56),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3480_action_queue_34"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704D_6, ["EVENT_3480_action_queue_32"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=9, y=2),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkNorthPixels(5),
		A_SetWalkingSpeed(NORMAL),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_WalkSouthPixels(1),
		A_EndLoop(),
		A_WalkSouthSteps(5),
		A_FixedFCoordOff()
	]),
	Jmp(["EVENT_3480_action_queue_35"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=10, y=4, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x02\xf0\xff')),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(3),
		A_BPL262728(),
		A_FixedFCoordOff()
	], identifier="EVENT_3480_action_queue_32"),
	Jmp(["EVENT_3480_set_action_script_36"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=8),
		A_FaceNortheast(),
		A_FloatingOn(),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(6),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%p\x02\xf5\xff')),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_WalkNortheastSteps(6),
		A_Walk1StepNorth(),
		A_BPL262728()
	], identifier="EVENT_3480_action_queue_34"),
	ActionQueueSync(target=NPC_16, subscript=[
		A_TransferToObjectXY(NPC_1),
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(60),
		A_VisibilityOff()
	], identifier="EVENT_3480_action_queue_35"),
	SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE, identifier="EVENT_3480_set_action_script_36"),
	JmpToSubroutine(["EVENT_3480_action_queue_40"]),
	RunEventAtReturn(E3489_MIDAS_RIVER_WATERFALL_LISTEN_FOR_BUTTON_INPUTS),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x00')),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_ShadowOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	], identifier="EVENT_3480_action_queue_40"),
	Return()
])
