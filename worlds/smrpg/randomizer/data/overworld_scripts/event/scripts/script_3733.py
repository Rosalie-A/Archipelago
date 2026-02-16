# E3733_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_PLATFORM
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
	MoveScriptToBackgroundThread2(),
	JmpIfBitSet(NIMBUS_PLATFORM_ACTIVE, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3584_ret_0"]),
	SetBit(TEMP_7043_1),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Set7000ToTappedButton(identifier="EVENT_3733_set_7000_to_tapped_button_5"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3584_ret_0"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_3733_jmp_if_present_in_current_level_11"]),
	JmpIf7000AnyBitsSet(bits=[0, 1, 2, 3], destinations=["EVENT_3584_ret_0"]),
	Pause(1),
	Jmp(["EVENT_3733_set_7000_to_tapped_button_5"]),
	JmpIfObjectInCurrentLevel(NPC_6, ["EVENT_3733_play_sound_13"], identifier="EVENT_3733_jmp_if_present_in_current_level_11"),
	Jmp(["EVENT_3733_summon_to_current_level_15"]),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3733_play_sound_13"),
	SetBit(NIMBUS_PLATFORM_ACTIVE),
	SummonObjectToCurrentLevel(NPC_6, identifier="EVENT_3733_summon_to_current_level_15"),
	Return()
])
