# E3282_SHIP_BOSS_ROOM_LOADER
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
	RunEventAsSubroutine(E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitSet(SHIP_LIBERATED, ["EVENT_3282_jmp_if_bit_clear_27"]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_Walk1StepSouth(),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SequenceLoopingOff(),
		A_Pause(50),
		A_WalkSouthwestSteps(2)
	]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	ClearBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	RunEventAsSubroutine(E0210_UNLOCK_SEASIDE_BOSS_IF_GATED_BY_SHIP_BOSS),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(SHIP_LIBERATED),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	UnknownCommand(bytearray(b'\xfd\x8er\x00(')),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNorthwestSteps(6),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_Pause(2)
	]),
	SetBit(JOHNNY_POSITION),
	RunEventAsSubroutine(E1208_SHIP_END_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(),
	JmpIfBitClear(JOHNNY_POSITION, ["ship_postgame_check"], identifier="EVENT_3282_jmp_if_bit_clear_27"),
	SetSyncActionScript(NPC_0, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=24, y=110),
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_FaceNorthwest()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3282_jmp_to_event_30"),
    JmpIfBitSet(POSTGAME_SHIP_COMPLETED, ["bring_back_original_npc"], identifier="ship_postgame_check"),
	JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_3282_jmp_to_event_30"]),
    RemoveObjectFromCurrentLevel(NPC_0),
    SummonObjectToCurrentLevel(NPC_7),
    Jmp(["EVENT_3282_jmp_to_event_30"]),
    RemoveObjectFromCurrentLevel(NPC_7, identifier="bring_back_original_npc"),
    SummonObjectToCurrentLevel(NPC_0),
    Jmp(["EVENT_3282_jmp_to_event_30"]),
])
