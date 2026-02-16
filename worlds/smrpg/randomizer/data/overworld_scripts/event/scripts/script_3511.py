# E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND
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
	SetVarToConst(TEMP_70AE, 3),
	StartLoopNTimes(6),
	JmpIfRandom2of3(['EVENT_3511_set_action_script_5', 'EVENT_3511_set_action_script_7']),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_8"]),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_5"),
	Jmp(["EVENT_3511_pause_8"]),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_7"),
	Pause(210, identifier="EVENT_3511_pause_8"),
	EndLoop(),
	Pause(30),
	StartLoopNTimes(6),
	JmpIfRandom2of3(['EVENT_3511_set_action_script_16', 'EVENT_3511_set_action_script_19']),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_21"]),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_16"),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_21"]),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_19"),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	Pause(210, identifier="EVENT_3511_pause_21"),
	EndLoop(),
	Pause(30),
	StartLoopNTimes(6),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Pause(210),
	EndLoop(),
	Pause(30),
	Pause(210),
	Pause(210),
	StartLoopNTimes(1),
	Pause(210),
	Pause(210),
    JmpIfBitSet(BOOSTER_HILL_CLOSED, ["EVENT_3511_end_loop_41"]),
	
	CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3511_end_loop_41"]),
	PlaySoundBalance(sound=SO014_FLOWER, balance=40),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["summon_flower_floor_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["summon_flower_floor_2"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["summon_flower_floor_3"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["summon_flower_floor_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["summon_flower_floor_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["summon_flower_floor_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["summon_flower_floor_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["summon_flower_floor_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["summon_flower_floor_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["summon_flower_floor_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["summon_flower_floor_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["summon_flower_floor_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["summon_flower_floor_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["summon_flower_floor_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["summon_flower_floor_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["summon_flower_floor_16"]),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P069_BOOSTER_HILL_PRIZE_STANDING_0, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_1"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P071_BOOSTER_HILL_PRIZE_STANDING_1, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_2"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P072_BOOSTER_HILL_PRIZE_STANDING_2, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_3"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P074_BOOSTER_HILL_PRIZE_STANDING_3, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_4"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P075_BOOSTER_HILL_PRIZE_STANDING_4, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_5"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P077_BOOSTER_HILL_PRIZE_STANDING_5, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_6"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P078_BOOSTER_HILL_PRIZE_STANDING_6, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_7"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P080_BOOSTER_HILL_PRIZE_STANDING_7, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_8"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P081_BOOSTER_HILL_PRIZE_STANDING_8, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_9"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P082_BOOSTER_HILL_PRIZE_STANDING_9, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_10"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P083_BOOSTER_HILL_PRIZE_STANDING_10, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_11"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P084_BOOSTER_HILL_PRIZE_STANDING_11, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_12"),
    Jmp(["EVENT_3511_end_loop_41"]),
    CreatePacketAt7010WithEvent(P085_BOOSTER_HILL_PRIZE_STANDING_12, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_13"),
    Jmp(["EVENT_3511_end_loop_41"]),
	CreatePacketAt7010WithEvent(P086_BOOSTER_HILL_PRIZE_STANDING_13, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_14"),
    Jmp(["EVENT_3511_end_loop_41"]),
	CreatePacketAt7010WithEvent(P087_BOOSTER_HILL_PRIZE_STANDING_14, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_15"),
    Jmp(["EVENT_3511_end_loop_41"]),
	CreatePacketAt7010WithEvent(P088_BOOSTER_HILL_PRIZE_STANDING_15, E3512_BOOSTER_HILL_FLOWER_PICKUP, ["EVENT_3511_end_loop_41"], identifier="summon_flower_floor_16"),
    EndLoop(identifier="EVENT_3511_end_loop_41"),
	Return()
])
