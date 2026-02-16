# E2063_SUPER_JUMP_PRIZE_GRANT
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
	Set7000To7FMemVar(0xF8C0),
	JmpIfBitSet(SUPER_JUMP_PRIZE_2_GRANTED, ["EVENT_2063_run_dialog_23"]),
	JmpIfBitSet(SUPER_JUMP_PRIZE_1_GRANTED, ["EVENT_2063_run_dialog_15"]),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RunEventAsSubroutine(E3393_SUPER_JUMP_COMPARE_FOR_1ST_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_8"]),
	RunDialog(dialog_id=DI2628_SUPERJUMP_CHALLENGE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI2629_SUPER_JUMP_PRIZE_1, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_8"),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	SetBit(SUPER_JUMP_PRIZE_1_GRANTED),
	Set7000To7FMemVar(0xF8C0),
	RunEventAsSubroutine(E3394_SUPER_JUMP_COMPARE_FOR_2ND_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_19"]),
	Return(),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_15"),
	RunEventAsSubroutine(E3394_SUPER_JUMP_COMPARE_FOR_2ND_PRIZE),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_19"]),
	Return(),
	RunDialog(dialog_id=DI2631_SUPER_JUMP_PRIZE_2, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_19"),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	SetBit(SUPER_JUMP_PRIZE_2_GRANTED),
	Return(),
	RunDialog(dialog_id=DI2632_DOG_OUT_OF_PRIZES, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_23"),
	Return()
])
