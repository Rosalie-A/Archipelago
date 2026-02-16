# E3885_END_GAME
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
	FreezeCamera(),
	Set0158Bit7Offset(0x0158, True),
	PlayMusicAtCurrentVolume(M0023_GOTASTARPIECE_PART1),
	Pause(1),
	StopMusicFDA2(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(8)
	]),
	ActionQueueSync(target=LAYER_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(22),
		A_WalkNorthSteps(16)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=50, z=0, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=3, y=53, z=0, direction=EAST),
		A_FaceEast()
	]),
	ActionQueueSync(target=NPC_20, subscript=[
		A_TransferToXYZF(x=1, y=54, z=0, direction=EAST),
		A_TransferXYZFPixels(x=16, y=0, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_21, subscript=[
		A_TransferToXYZF(x=2, y=59, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=12, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_TransferToXYZF(x=3, y=58, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_23, subscript=[
		A_TransferToXYZF(x=1, y=57, z=0, direction=EAST),
		A_TransferXYZFPixels(x=16, y=0, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
	FadeInFromColour(duration=90, colour=WHITE),
	PauseScriptUntilEffectDone(),
	Pause(120),
	PauseActionScript(NPC_7),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShadowOn(),
		A_BPL262728(),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(4),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(3)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_VisibilityOff(),
		A_Pause(11),
		A_TransferToXYZF(x=6, y=50, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=0, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkEastPixels(16),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
	Pause(60),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_23, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_20, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=12, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=14, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_21, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_20, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_23, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(6),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	RememberLastObject(),
	Pause(60),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_BounceToXYWithHeight(x=6, y=50, height=10),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=54, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST)
	]),
	SetSyncActionScript(NPC_0, A0248_ENDING_CUTSCENE_EFFECT),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(2),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 2])
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\xf0\xff\xc0\xff')),
		A_Pause(64),
		A_BPL262728()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_Pause(4),
		A_StartLoopNTimes(4),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(4),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\x00\xe0\xff')),
		A_Pause(140),
		A_BPL262728(),
		A_SequenceLoopingOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_20, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$0\x00\x80\xff')),
		A_Pause(64),
		A_BPL262728(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8e\x16\n\x0b')),
	RememberLastObject(),
	UnsyncActionScript(NPC_0),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
	Pause(120),
	PauseActionScript(NPC_7),
	StartSyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(7),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(2)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SequencePlaybackOff(),
		A_Pause(12),
		A_SequencePlaybackOn(),
		A_TransferToXYZF(x=4, y=46, z=0, direction=EAST),
		A_TransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
	Pause(120),
	PauseActionScript(NPC_7),
	StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(62),
		A_SetSequenceSpeed(FASTEST)
	]),
	Pause(60),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	Pause(60),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownSteps(5),
		A_ShiftZDownPixels(4),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	Pause(200),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(6),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(1),
		A_ShiftZUpPixels(6)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(34),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpSteps(4),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step()
	]),
	Pause(100),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\n\n')),
	RememberLastObject(),
	SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
	Pause(98),
	PauseActionScript(NPC_7),
	ActionQueueSync(target=NPC_7, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(8)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_TransferToXYZF(x=4, y=38, z=0, direction=EAST),
		A_TransferXYZFPixels(x=250, y=0, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(4)
	]),
	RememberLastObject(),
	RunStarPieceSequence(7),
	UnknownCommand(bytearray(b'\xfd\x8er\x00\x00')),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_TransferXYZFPixels(x=0, y=16, z=0, direction=EAST)
	]),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=4, y=51, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(2),
		A_WalkWestPixels(8)
	]),
	ActionQueueSync(target=NPC_21, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\x00\x80\xff')),
		A_Pause(88),
		A_BPL262728(),
		A_SequenceLoopingOff()
	]),
	Clear0158Bit7Offset(0x0158, True),
	FadeInFromBlack(sync=True, duration=60),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(60),
	ActionQueueSync(target=NPC_20, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_23, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=False)
	]),
	Pause(60),
	PlayMusicAtDefaultVolume(M0070_ENDINGPART1),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_20, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSoutheast(),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorthwest(),
		A_Pause(60),
		A_FaceSoutheast(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_23, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=64, silent=True),
		A_Walk1StepSouthwest(),
		A_Pause(60),
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNorthwest(),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=64, silent=True),
		A_Walk1StepSoutheast(),
		A_Pause(60),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=92, silent=True),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(10),
		A_Pause(80),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(20),
		A_TransferToXYZF(x=4, y=49, z=20, direction=EAST),
		A_TransferXYZFPixels(x=246, y=8, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_TransferToXYZF(x=4, y=53, z=20, direction=EAST),
		A_TransferXYZFPixels(x=4, y=248, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(32),
		A_TransferToXYZF(x=4, y=56, z=20, direction=EAST),
		A_TransferXYZFPixels(x=12, y=246, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(24),
		A_TransferToXYZF(x=4, y=56, z=20, direction=EAST),
		A_TransferXYZFPixels(x=244, y=0, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(34),
		A_TransferToXYZF(x=3, y=54, z=20, direction=EAST),
		A_TransferXYZFPixels(x=252, y=0, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(50),
		A_TransferToXYZF(x=3, y=52, z=20, direction=EAST),
		A_TransferXYZFPixels(x=250, y=252, z=0, direction=EAST),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(40),
		A_TransferToXYZF(x=4, y=50, z=20, direction=EAST),
		A_TransferXYZFPixels(x=238, y=252, z=0, direction=EAST),
		A_FloatingOn()
	]),
	RememberLastObject(),
	UnknownCommand(bytearray(b'^')),
	SetSyncActionScript(NPC_8, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_9, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_10, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_11, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_12, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_13, A0120_EMBEDDED_ROUTINE),
	SetSyncActionScript(NPC_14, A0120_EMBEDDED_ROUTINE),
	Pause(90),
	SetSyncActionScript(NPC_4, A0251_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_5, A0252_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_6, A0253_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_0, A0254_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_1, A0255_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_2, A0224_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	SetSyncActionScript(NPC_3, A0225_ENDING_CUTSCENE_EFFECT),
	Pause(24),
	PauseActionScript(NPC_12),
	PauseActionScript(NPC_13),
	PauseActionScript(NPC_14),
	PauseActionScript(NPC_8),
	PauseActionScript(NPC_9),
	PauseActionScript(NPC_10),
	PauseActionScript(NPC_11),
	SetSyncActionScript(NPC_12, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_13, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_14, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_8, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_9, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_10, A0226_ENDING_CUTSCENE_EFFECT),
	SetSyncActionScript(NPC_11, A0226_ENDING_CUTSCENE_EFFECT),
	Pause(420),
	SetSyncActionScript(NPC_21, A0227_ENDING_CUTSCENE_EFFECT),
	Pause(1, identifier="EVENT_3885_pause_168"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3885_action_queue_171"]),
	Jmp(["EVENT_3885_pause_168"]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(8),
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=42, z=0, direction=EAST),
		A_TransferXYZFPixels(x=248, y=248, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	], identifier="EVENT_3885_action_queue_171"),
	Pause(1, identifier="EVENT_3885_pause_172"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3885_action_queue_175"]),
	Jmp(["EVENT_3885_pause_172"]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(6),
		A_TransferToXYZF(x=4, y=41, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=0, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_Pause(10),
		A_VisibilityOff(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	], identifier="EVENT_3885_action_queue_175"),
	Pause(1, identifier="EVENT_3885_pause_176"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3885_action_queue_179"]),
	Jmp(["EVENT_3885_pause_176"]),
	ActionQueueSync(target=NPC_17, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=43, z=0, direction=EAST),
		A_TransferXYZFPixels(x=250, y=12, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xfa\x00\xfa')),
		A_Pause(32),
		A_BPL262728(),
		A_VisibilityOff()
	], identifier="EVENT_3885_action_queue_179"),
	Pause(1, identifier="EVENT_3885_pause_180"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_3885_action_queue_183"]),
	Jmp(["EVENT_3885_pause_180"]),
	ActionQueueSync(target=NPC_18, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=46, z=0, direction=EAST),
		A_TransferXYZFPixels(x=6, y=244, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$ \xfc\xe0\xfb')),
		A_Pause(32),
		A_BPL262728(),
		A_VisibilityOff()
	], identifier="EVENT_3885_action_queue_183"),
	Pause(1, identifier="EVENT_3885_pause_184"),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3885_action_queue_187"]),
	Jmp(["EVENT_3885_pause_184"]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(4),
		A_TransferToXYZF(x=2, y=45, z=0, direction=EAST),
		A_TransferXYZFPixels(x=4, y=6, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(8),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\xe0\x05\xe0\xf8')),
		A_Pause(32),
		A_BPL262728(),
		A_VisibilityOff()
	], identifier="EVENT_3885_action_queue_187"),
	Pause(1, identifier="EVENT_3885_pause_188"),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3885_action_queue_191"]),
	Jmp(["EVENT_3885_pause_188"]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_TransferToXYZF(x=4, y=49, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xfe\x00\xf8')),
		A_Pause(32),
		A_BPL262728(),
		A_VisibilityOff()
	], identifier="EVENT_3885_action_queue_191"),
	Pause(1, identifier="EVENT_3885_pause_192"),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_3885_action_queue_195"]),
	Jmp(["EVENT_3885_pause_192"]),
	ActionQueueSync(target=NPC_17, subscript=[
		A_TransferToXYZF(x=5, y=45, z=0, direction=EAST),
		A_TransferXYZFPixels(x=232, y=4, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xfe\x00\xf8')),
		A_Pause(32),
		A_BPL262728(),
		A_VisibilityOff()
	], identifier="EVENT_3885_action_queue_195"),
	Pause(180),
	ActionQueueAsync(target=LAYER_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(40)
	]),
	Pause(90),
	FadeOutToColour(duration=120, colour=WHITE),
	PauseScriptUntilEffectDone(),
	Pause(30),
	JmpToEvent(E3950_POST_FINAL_BOSS_INIT)
])
