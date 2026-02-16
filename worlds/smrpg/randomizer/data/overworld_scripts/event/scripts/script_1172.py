# E1172_MUSHROOM_BOY
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
	JmpIfBitSet(UNKNOWN_7087_2, ["EVENT_1172_run_dialog_3"]),
	RunDialog(dialog_id=DI2928_MUSHROOM_BOY_INTRO, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_2),
	RunDialog(dialog_id=DI2929_MUSHROOM_BOY_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_3"),
	JmpIfDialogOptionBSelected(["EVENT_1172_run_dialog_28"]),
	StoreItemAmountTo7000(MushroomItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1172_run_dialog_27"]),
	RunDialog(dialog_id=DI2930_MUSHROOM_BOY_CONFIRM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RemoveOneOfItemFromInventory(MushroomItem),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(85),
		A_SequenceLoopingOn()
	]),
	RunEventAsSubroutine(E1972_MUSHROOM_BOY_ODDS),
	CompareVarToConst(PRIMARY_TEMP_7000, 400),
	JmpIfComparisonResultIsLesser(["EVENT_1172_play_sound_18"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 1000),
	JmpIfComparisonResultIsLesser(["EVENT_1172_jmp_to_event_22"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2400),
	JmpIfComparisonResultIsLesser(["EVENT_1172_play_sound_23"]),
	JmpToEvent(E1973_CLONE_RESERVED),
	PlaySound(sound=SO085_FLOWER, channel=6, identifier="EVENT_1172_play_sound_18"),
	RunDialog(dialog_id=DI2939_RECEIVED_FLOWER_TAB, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(FlowerTabItem),
	Return(),
	JmpToEvent(E1971_MUSHROOM_BOY_GRANTS_ROCK_CANDY, identifier="EVENT_1172_jmp_to_event_22"),
	PlaySound(sound=SO085_FLOWER, channel=6, identifier="EVENT_1172_play_sound_23"),
	RunDialog(dialog_id=DI2937_RECEIVED_MAPLE_SYRUP, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(MapleSyrupItem),
	Return(),
	RunDialog(dialog_id=DI2936_NO_MUSHROOMS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_27"),
	RunDialog(dialog_id=DI2935_MUSHROOM_BOY_GOODBYE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_28"),
	Return()
])
