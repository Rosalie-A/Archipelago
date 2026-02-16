# E1078_MELODY_BAY_FINAL_SONG
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
	JmpIfBitClear(TEMP_7043_0, ["EVENT_1078_jmp_if_bit_clear_3"], identifier="EVENT_1078_jmp_if_bit_clear_0"),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_1078_jmp_if_bit_clear_6"], identifier="EVENT_1078_jmp_if_bit_clear_3"),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_1078_jmp_if_bit_clear_9"], identifier="EVENT_1078_jmp_if_bit_clear_6"),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_1078_jmp_if_bit_clear_12"], identifier="EVENT_1078_jmp_if_bit_clear_9"),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_1078_jmp_if_bit_clear_15"], identifier="EVENT_1078_jmp_if_bit_clear_12"),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_1078_jmp_if_bit_clear_18"], identifier="EVENT_1078_jmp_if_bit_clear_15"),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_1078_jmp_if_bit_clear_21"], identifier="EVENT_1078_jmp_if_bit_clear_18"),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_1078_ret_24"], identifier="EVENT_1078_jmp_if_bit_clear_21"),
	SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	Return(identifier="EVENT_1078_ret_24")
])
