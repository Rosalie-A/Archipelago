# E2603_FACTORY_4TH_BOSS_FIGHT
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
	JmpIfBitSet(INNER_FACTORY_ROOM_4_COMPLETED, ["EVENT_2603_ret_38"]),
	SetBit(INNER_FACTORY_ROOM_4_COMPLETED),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=5, y=75)
	]),
	Pause(16),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(16),
		A_FaceSoutheast(),
		A_WalkSoutheastSteps(2)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(10),
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2603_restore_all_hp_14"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2603_restore_all_hp_14"),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromSpecificLevel(NPC_0, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_1, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_2, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_4, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_5, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_6, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_12, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=10, y=91),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	RunEventAsSubroutine(E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED),
	JmpIfComparisonResultIsLesser(["EVENT_2603_fade_in_from_black_async_36"]),
	SummonObjectToSpecificLevel(NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	FadeInFromBlack(sync=False, identifier="EVENT_2603_fade_in_from_black_async_36"),
	RunEventAsSubroutine(E1244_INNER_FACTORY_4_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2603_ret_38")
])
