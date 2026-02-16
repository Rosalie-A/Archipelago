# E1829_KEEP_DISPLAY_REMAINING_TRIES
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
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	CopyVarToVar(from_var=KEEP_DOOR_LIVES, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 10),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_16"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_14"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_12"]),
	RunDialog(dialog_id=DI1319_LAST_CHANCE, above_object=NPC_12, closable=False, sync=False, multiline=False, use_background=False, bit_6=True),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
	RunDialog(dialog_id=DI1318_ONLY_GOT_X_CHANCES_LEFT, above_object=NPC_12, closable=False, sync=False, multiline=False, use_background=False, bit_6=True, identifier="EVENT_1829_run_dialog_12"),
	Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
	RunDialog(dialog_id=DI1317_GOT_X_CHANCES, above_object=NPC_12, closable=False, sync=False, multiline=False, use_background=False, bit_6=True, identifier="EVENT_1829_run_dialog_14"),
	Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
	RunDialog(dialog_id=DI1316_GOT_X_TRIES, above_object=NPC_12, closable=False, sync=False, multiline=False, use_background=False, bit_6=True, identifier="EVENT_1829_run_dialog_16"),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"),
	Return()
])
