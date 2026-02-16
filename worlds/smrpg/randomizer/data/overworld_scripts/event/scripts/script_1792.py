# E1792_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_ObjectMemorySetBit(arg_1=0x09, bits=[7])
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ObjectMemorySetBit(arg_1=0x09, bits=[7])
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ObjectMemorySetBit(arg_1=0x09, bits=[7])
	]),
	JmpIfBitSet(LANDS_END_UNDERGROUND_DOGS_MOVED, ["EVENT_1792_jmp_to_event_7"]),
	SetBit(LANDS_END_UNDERGROUND_DOGS_MOVED),
	SetVarToConst(TIMER_701C, 80),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1790_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER_BACKGROUND, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1792_jmp_to_event_7")
])
