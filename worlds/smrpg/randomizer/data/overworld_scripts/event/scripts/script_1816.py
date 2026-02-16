# E1816_TROOPA_CLIFF_FINISH
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
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1816_ret_51"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1816_ret_51"]),
	SetBit(TEMP_7044_2),
	StopAllBackgroundEvents(),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_1),
	StopSound(),
	Pause(1),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	FadeOutMusicToVolume(duration=2, volume=127),
	SetVarToConst(TEMP_70AB, 21),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=25, y=112),
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_Pause(20),
		A_PlaySound(sound=SO133_CLOSE_HIT_DOOR, channel=4),
		A_Pause(20)
	]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1263_TROOPA_CLIFF_TIME, above_object=MARIO, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 1800),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_21"]),
	Return(),
	CompareVarToConst(PRIMARY_TEMP_7000, 840, identifier="EVENT_1816_compare_var_to_const_21"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_24"]),
	Return(),
	CompareVarToConst(PRIMARY_TEMP_7000, 720, identifier="EVENT_1816_compare_var_to_const_24"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_29"]),
	JmpIfRandom2of3(['EVENT_1816_ret_51', 'EVENT_1816_ret_51']),
	SetVarToConst(TEMP_7028, 1),
	Jmp(["EVENT_1816_action_queue_43"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 660, identifier="EVENT_1816_compare_var_to_const_29"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_jmp_if_bit_clear_41"]),
	JmpIfBitSet(TROOPA_CLIMB_COMPLETED, ["EVENT_1816_set_var_to_const_35"]),
	SetBit(TROOPA_CLIMB_COMPLETED, identifier="EVENT_1816_set_bit_32"),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return(),
	SetVarToConst(TEMP_7028, 1, identifier="EVENT_1816_set_var_to_const_35"),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 690),
	JmpIfComparisonResultIsLesser(["EVENT_1816_jmp_40"]),
	JmpIfRandom1of2(["EVENT_1816_ret_51"]),
	Jmp(["EVENT_1816_action_queue_43"], identifier="EVENT_1816_jmp_40"),
	JmpIfBitClear(TROOPA_CLIMB_COMPLETED, ["EVENT_1816_set_bit_32"], identifier="EVENT_1816_jmp_if_bit_clear_41"),
	SetVarToConst(TEMP_7028, 5),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_1816_action_queue_43"),
	SetObjectMemoryToVar(TEMP_7028),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_UnknownCommand(bytearray(b'\x97\x15')),
		A_SetAllSpeeds(FASTEST),
		A_ShiftZUpPixels(16),
		A_SetAllSpeeds(NORMAL),
		A_VisibilityOn(),
		A_FloatingOff(),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSouthwest(),
		A_Pause(6),
		A_VisibilityOff()
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddFrogCoins(PRIMARY_TEMP_7000),
	EndLoop(),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	Return(identifier="EVENT_1816_ret_51")
])
