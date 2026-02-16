# E3644_NIMBUS_INNKEEPER
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
	SetVarToConst(TEMP_70AE, 20),
	SetVarToConst(SECONDARY_TEMP_7024, 30),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_3644_run_dialog_181"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_3644_run_dialog_181"]),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3644_run_dialog_181"]),
	JmpIfBitSet(TEMP_7042_7, ["EVENT_3644_run_dialog_181"]),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_3644_run_dialog_181"]),
	RunDialog(dialog_id=DI3729_NIMBUS_INNKEEPER, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3644_pause_168"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3644_clear_bit_171"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	SetBit(NIMBUS_INN),
	RunDialog(dialog_id=DI3730_DREAM_CUSHION_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3644_pause_177"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3644_clear_bit_174"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	FadeOutMusicToVolume(duration=2, volume=0),
	CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
	Pause(10),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
	PauseScriptUntilEffectDone(),
	JmpIfBitClear(NIMBUS_INN_PRIZE_GRANTED, ["EVENT_3644_set_bit_55"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 51),
	CompareVarToConst(PRIMARY_TEMP_7000, 45),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3644_jmp_if_bit_set_54"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 41),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3644_set_bit_158"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 34),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3644_set_bit_142"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 17),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3644_copy_var_to_var_73"]),
	SetBit(TEMP_7042_4),
	EnterArea(room_id=R504_NIMBUS_LAND_DREAM_CUSHION_DREAM_TORTES_ARE_SEASONING_MARIO, face_direction=SOUTH, x=26, y=84, z=1),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=0, y=6, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3)
	]),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(240),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	JmpIfBitSet(NIMBUS_INN_PRIZE_GRANTED, ["EVENT_3644_set_bit_158"], identifier="EVENT_3644_jmp_if_bit_set_54"),
	SetBit(TEMP_7042_5, identifier="EVENT_3644_set_bit_55"),
	EnterArea(room_id=R502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, face_direction=SOUTH, x=23, y=20, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=8, y=248, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastSteps(7),
		A_WalkEastPixels(8)
	]),
	SummonObjectToCurrentLevel(NPC_4),
	SetSyncActionScript(NPC_4, A0099_LOOPED_JUMPING),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(120),
	SetBit(TEMP_7043_1),
	Pause(30),
	ActionQueueSync(target=NPC_4, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(1),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(32),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop(),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_VisibilityOn()
	]),
	RememberLastObject(),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	SetBit(TEMP_704C_0),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	CopyVarToVar(from_var=NIMBUS_INN_COUNTER, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3644_copy_var_to_var_73"),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3644_set_bit_158"]),
	SetBit(TEMP_7042_6),
	EnterArea(room_id=R502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, face_direction=SOUTH, x=23, y=20, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=8, y=248, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastSteps(7),
		A_WalkEastPixels(8)
	]),
	SetVarToRandom(PRIMARY_TEMP_7000, 4),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_3644_jmp_if_bit_set_98"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3644_jmp_if_bit_set_111"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3644_jmp_if_bit_set_125"]),
	JmpIfBitSet(NIMBUS_INN_UNKNOWN_1, ["EVENT_3644_copy_var_to_var_73"]),
	SetBit(NIMBUS_INN_UNKNOWN_1),
	Inc(NIMBUS_INN_COUNTER),
	SummonObjectToCurrentLevel(NPC_0),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	SetAsyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	RunDialog(dialog_id=DI3803_DREAM_GAZ, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	JmpIfBitSet(NIMBUS_INN_UNKNOWN_2, ["EVENT_3644_copy_var_to_var_73"], identifier="EVENT_3644_jmp_if_bit_set_98"),
	SetBit(NIMBUS_INN_UNKNOWN_2),
	Inc(NIMBUS_INN_COUNTER),
	SummonObjectToCurrentLevel(NPC_3),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=20, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO063_YOSHI_TALK, channel=4),
		A_Pause(10),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3804_DREAM_YOSHI, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	JmpIfBitSet(NIMBUS_INN_UNKNOWN_3, ["EVENT_3644_copy_var_to_var_73"], identifier="EVENT_3644_jmp_if_bit_set_111"),
	SetBit(NIMBUS_INN_UNKNOWN_3),
	Inc(NIMBUS_INN_COUNTER),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Pause(60),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(8),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI3805_DREAM_CHANCELLOR, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	JmpIfBitSet(NIMBUS_INN_UNKNOWN_4, ["EVENT_3644_copy_var_to_var_73"], identifier="EVENT_3644_jmp_if_bit_set_125"),
	SetBit(NIMBUS_INN_UNKNOWN_4),
	Inc(NIMBUS_INN_COUNTER),
	SummonObjectToCurrentLevel(NPC_2),
	SetSyncActionScript(NPC_2, A0099_LOOPED_JUMPING),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(60),
	RunDialog(dialog_id=DI3806_DREAM_JUMPING_KID, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_1),
	Pause(30),
	SetSyncActionScript(NPC_2, A0023_FAST_REPEATED_JUMPING),
	RunDialog(dialog_id=DI3807_DREAM, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	SetBit(TEMP_7042_7, identifier="EVENT_3644_set_bit_142"),
	EnterArea(room_id=R502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, face_direction=SOUTH, x=22, y=19, z=0),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(16)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=30, y=19, z=2, direction=EAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_ShadowOn()
	]),
	RememberLastObject(),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkEastSteps(7),
		A_WalkEastPixels(16),
		A_BPL262728()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkWestSteps(7),
		A_WalkWestPixels(16),
		A_BPL262728()
	]),
	Pause(120),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkEastSteps(6),
		A_BPL262728()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkWestSteps(6),
		A_BPL262728()
	]),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	SetBit(TEMP_7042_3, identifier="EVENT_3644_set_bit_158"),
	EnterArea(room_id=R503_NIMBUS_LAND_DREAM_CUSHION_DREAM_HEAVY_TROOPA_LAYING_ON_MARIO, face_direction=SOUTH, x=25, y=52, z=1),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_ShadowOn(),
		A_TransferToXYZF(x=25, y=52, z=2, direction=EAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=4, y=248, z=0, direction=EAST),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=248, y=4, z=0, direction=EAST),
		A_SequenceLoopingOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_Pause(240),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(50),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True, duration=120),
	PauseScriptUntilEffectDone(),
	Pause(240),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0736_ROSE_TOWN_INN_SLEEP_SUBROUTINE),
	Pause(10, identifier="EVENT_3644_pause_168"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(),
	ClearBit(INSUFFICIENT_COINS, identifier="EVENT_3644_clear_bit_171"),
	RunDialog(dialog_id=DI3731_NIMBUS_INN_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	ClearBit(INSUFFICIENT_COINS, identifier="EVENT_3644_clear_bit_174"),
	RunDialog(dialog_id=DI3774_NIMBUS_INN_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpToEvent(E0280_SLEEP_IN_NIMBUS_INN),
	Pause(10, identifier="EVENT_3644_pause_177"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	JmpToEvent(E0280_SLEEP_IN_NIMBUS_INN),
	Return(),
	RunDialog(dialog_id=DI3767_DUPLICATE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_3644_run_dialog_181"),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_3644_run_dialog_187"]),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3644_run_dialog_189"]),
	JmpIfBitSet(TEMP_7042_7, ["EVENT_3644_run_dialog_191"]),
	RunDialog(dialog_id=DI3769_NIMBUS_INNKEEPER_AFTER_DREAM_CUSHION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3644_clear_bit_192"]),
	RunDialog(dialog_id=DI3768_NIMBUS_INNKEEPER_AFTER_DREAM_CUSHION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3644_run_dialog_187"),
	Jmp(["EVENT_3644_clear_bit_192"]),
	RunDialog(dialog_id=DI3770_NIMBUS_INNKEEPER_AFTER_DREAM_CUSHION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3644_run_dialog_189"),
	Jmp(["EVENT_3644_clear_bit_192"]),
	RunDialog(dialog_id=DI3771_NIMBUS_INNKEEPER_AFTER_DREAM_CUSHION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3644_run_dialog_191"),
	ClearBit(TEMP_7042_4, identifier="EVENT_3644_clear_bit_192"),
	ClearBit(TEMP_7042_5),
	ClearBit(TEMP_7042_6),
	ClearBit(TEMP_7042_7),
	ClearBit(TEMP_7042_3),
	Return()
])
