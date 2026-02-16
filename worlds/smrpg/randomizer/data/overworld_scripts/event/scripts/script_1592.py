# E1592_BELOME_STATUE
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
	StoreItemAmountTo7000(TempleKeyItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1592_summon_to_current_level_at_marios_coords_4"]),
	RunDialog(dialog_id=DI1235_BELOME_STATUE_KEY_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_12, identifier="EVENT_1592_summon_to_current_level_at_marios_coords_4"),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetPriority(3),
		A_SetVRAMPriority(PRIORITY_3),
		A_JumpToHeight(112),
		A_WalkToXYCoords(x=1, y=118),
		A_Pause(1, identifier="EVENT_1592_action_queue_5_SUBSCRIPT_pause_6"),
		A_JmpIfObjectInAir(NPC_12, ["EVENT_1592_action_queue_5_SUBSCRIPT_pause_6"]),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2)
	]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(50),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False)
	]),
	RemoveObjectFromCurrentLevel(NPC_12),
	Pause(60),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(target=NPC_16),
	StartLoopNTimes(2),
	Pause(1, identifier="EVENT_1592_pause_13"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1592_pause_13"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	EndLoop(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_JumpToHeight(128),
		A_StartLoopNTimes(4),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	RemoveOneOfItemFromInventory(TempleKeyItem),
	ApplySolidityModToLevel(permanent=True, room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, mod_id=0),
	SetBit(TEMPLE_KEY_USED),
    ClearBit(TEMPLE_BOSS_GATED),
	Return()
])
