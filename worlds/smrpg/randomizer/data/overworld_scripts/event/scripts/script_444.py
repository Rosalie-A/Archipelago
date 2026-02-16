# E0444_GOOMBA_THUMPIN_ADMINISTRATOR
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
	JmpIfBitSet(TEMP_7044_5, ["EVENT_444_copy_var_to_var_44"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_444_close_dialog_80"]),
	CloseDialog(),
	RunDialog(dialog_id=DI2541_GOOMBA_THUMPIN_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_444_close_dialog_40"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	SetVarToConst(PRIMARY_TEMP_7000, 10),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_444_run_dialog_61"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	JmpIfBitSet(UNKNOWN_7083_7, ["EVENT_444_run_dialog_17"]),
	SetVarToConst(PRIMARY_TEMP_7000, 20),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=GOOMBA_THUMPIN_THRESHOLD),
	RunDialog(dialog_id=DI2542_GOOMBA_THUMPIN_RULES_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_444_run_dialog_17"),
	JmpIfDialogOptionBSelected(["EVENT_444_set_action_script_29"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	CloseDialog(identifier="EVENT_444_close_dialog_21"),
	RunDialog(dialog_id=DI0836_GOOMBA_THUMPIN_TIP, above_object=MARIO, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=4, y=115),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSoutheastSteps(2),
		A_WalkSouthPixels(8),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI0822_GOOMBA_THUMPIN_START, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	FadeOutMusicToVolume(duration=2, volume=0),
	SetBit(TEMP_7044_6),
	JmpToEvent(E0445_GOOMBA_THUMPIN_BEGINS),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_444_set_action_script_29"),
	Pause(10),
	CopyVarToVar(from_var=GOOMBA_THUMPIN_THRESHOLD, to_var=PRIMARY_TEMP_7000, identifier="EVENT_444_copy_var_to_var_31"),
	RunDialog(dialog_id=DI2543_GOOMBA_THUMPIN_RULES, above_object=MARIO, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_444_set_action_script_37"]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	Jmp(["EVENT_444_close_dialog_21"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES, identifier="EVENT_444_set_action_script_37"),
	Pause(10),
	Jmp(["EVENT_444_copy_var_to_var_31"]),
	CloseDialog(identifier="EVENT_444_close_dialog_40"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	Return(),
	CopyVarToVar(from_var=GOOMBA_THUMPIN_THRESHOLD, to_var=PRIMARY_TEMP_7000, identifier="EVENT_444_copy_var_to_var_44"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Compare7000ToVar(ROSE_WAY_703A),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_444_copy_var_to_var_63"]),
	JmpIfBitClear(GOOMBA_THUMPIN_PRIZE_1_GRANTED, ["EVENT_444_run_dialog_56"]),
	JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_2_GRANTED, ["EVENT_444_run_dialog_56"]),
	AddConstToVar(TEMP_7028, 1),
	JmpIfVarNotEqualsConst(TEMP_7028, 3, ["EVENT_444_run_dialog_56"]),
	RunDialog(dialog_id=DI0841_GOOMBA_THUMPIN_PITY_MECHANIC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(TEMP_7028, 0),
	Jmp(["EVENT_444_set_bit_73"]),
	RunDialog(dialog_id=DI0840_GOOMBA_THUMPIN_NO_DICE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_444_run_dialog_56"),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_444_enable_controls_57"),
	ClearBit(TEMP_7049_6),
	ClearBit(TEMP_7044_5),
	Return(),
	RunDialog(dialog_id=DI0879_OUT_OF_CASH_LEARN_TO_STASH, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_444_run_dialog_61"),
	Return(),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_444_copy_var_to_var_63"),
	SetVarToConst(TEMP_7028, 0),
	AddConstToVar(PRIMARY_TEMP_7000, 2),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=GOOMBA_THUMPIN_THRESHOLD),
	RunDialog(dialog_id=DI0837_GOOMBA_THUMPIN_PRIZE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_1_GRANTED, ["EVENT_444_jmp_if_bit_set_72"]),
	SetBit(GOOMBA_THUMPIN_PRIZE_1_GRANTED),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Jmp(["EVENT_444_enable_controls_57"]),
	JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_2_GRANTED, ["EVENT_444_play_sound_76"], identifier="EVENT_444_jmp_if_bit_set_72"),
	SetBit(GOOMBA_THUMPIN_PRIZE_2_GRANTED, identifier="EVENT_444_set_bit_73"),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Jmp(["EVENT_444_enable_controls_57"]),
	PlaySound(sound=SO094_FROG_COIN, channel=6, identifier="EVENT_444_play_sound_76"),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=MARIO, closable=True, sync=False, multiline=False, use_background=False),
	AddFrogCoins(1),
	Jmp(["EVENT_444_enable_controls_57"]),
	CloseDialog(identifier="EVENT_444_close_dialog_80"),
	RunDialog(dialog_id=DI0838_GOOMBA_THUMPIN_DURING_GAME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
