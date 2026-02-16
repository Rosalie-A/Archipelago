# E3337_CORKPEDITE_ANIMATION
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
	ClearBit(TEMP_7043_0, identifier="EVENT_3337_clear_bit_0"),
	Pause(1),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_3337_set_bit_7"]),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_3337_set_bit_7"]),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_3337_set_bit_7"]),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_3337_set_bit_7"]),
	Jmp(["EVENT_3337_clear_bit_0"]),
	SetBit(TEMP_7043_0, identifier="EVENT_3337_set_bit_7"),
	Pause(1, identifier="EVENT_3337_pause_8"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3337_pause_8"]),
	Pause(8),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9c\x15')),
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(23),
		A_WalkNorthPixels(2),
		A_WalkSouthPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3337_jmp_if_bit_set_15"]),
	SetSyncActionScript(NPC_1, A0935_EJECTING_AN_OERLIKON),
	SetBit(TEMP_7043_4),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3337_jmp_if_bit_set_18"], identifier="EVENT_3337_jmp_if_bit_set_15"),
	SetSyncActionScript(NPC_2, A0935_EJECTING_AN_OERLIKON),
	SetBit(TEMP_7043_5),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_3337_jmp_if_bit_set_21"], identifier="EVENT_3337_jmp_if_bit_set_18"),
	SetSyncActionScript(NPC_3, A0935_EJECTING_AN_OERLIKON),
	SetBit(TEMP_7043_6),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3337_pause_24"], identifier="EVENT_3337_jmp_if_bit_set_21"),
	SetSyncActionScript(NPC_4, A0935_EJECTING_AN_OERLIKON),
	SetBit(TEMP_7043_7),
	Pause(16, identifier="EVENT_3337_pause_24"),
	Jmp(["EVENT_3337_clear_bit_0"])
])
