# E2477_BEAN_VALLEY_PIRANHA_PLANT_ANIMATIONS
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
	Pause(1, identifier="EVENT_2477_pause_0"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2477_jmp_if_bit_set_28"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2477_jmp_if_bit_set_33"], identifier="EVENT_2477_jmp_if_bit_set_2"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_2477_jmp_if_bit_set_18"], identifier="EVENT_2477_jmp_if_bit_set_3"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2477_jmp_if_bit_set_8"], identifier="EVENT_2477_jmp_if_bit_set_4"),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_2477_jmp_if_bit_set_23"], identifier="EVENT_2477_jmp_if_bit_set_5"),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_2477_jmp_if_bit_set_13"], identifier="EVENT_2477_jmp_if_bit_set_6"),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_2477_jmp_if_bit_set_5"], identifier="EVENT_2477_jmp_if_bit_set_8"),
	SetBit(TEMP_7044_1),
	SetSyncActionScript(NPC_6, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_0),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_2477_pause_0"], identifier="EVENT_2477_jmp_if_bit_set_13"),
	SetBit(TEMP_7044_3),
	SetSyncActionScript(NPC_7, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_1),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2477_jmp_if_bit_set_4"], identifier="EVENT_2477_jmp_if_bit_set_18"),
	SetBit(TEMP_7044_0),
	SetSyncActionScript(NPC_8, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_2),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_2477_jmp_if_bit_set_6"], identifier="EVENT_2477_jmp_if_bit_set_23"),
	SetBit(TEMP_7044_2),
	SetSyncActionScript(NPC_9, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_3),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_2477_jmp_if_bit_set_2"], identifier="EVENT_2477_jmp_if_bit_set_28"),
	SetBit(TEMP_7043_6),
	SetSyncActionScript(NPC_10, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_4),
	Jmp(["EVENT_2477_pause_0"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2477_jmp_if_bit_set_3"], identifier="EVENT_2477_jmp_if_bit_set_33"),
	SetBit(TEMP_7043_7),
	SetSyncActionScript(NPC_11, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	SummonObjectToCurrentLevel(NPC_5),
	Jmp(["EVENT_2477_pause_0"])
])
