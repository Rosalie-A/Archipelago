# E0708_MARRYMORE_TIP_DECISION_SUBROUTINE
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_708_jmp_to_event_7"], identifier="suite_threshold_1"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_708_jmp_to_event_9"], identifier="suite_threshold_2"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_708_jmp_to_event_11"], identifier="suite_threshold_3"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_708_jmp_to_event_13"], identifier="suite_threshold_4"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_708_jmp_to_event_15"], identifier="suite_threshold_5"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 200, ["EVENT_708_jmp_to_event_17"], identifier="suite_threshold_6"),
	Return(),
	JmpToEvent(E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_708_jmp_to_event_7"),
	Return(),
	JmpToEvent(E0179_NPC_QUEST_2_CONTAINER, identifier="EVENT_708_jmp_to_event_9"),
	Return(),
	JmpToEvent(E0180_NPC_QUEST_3_CONTAINER, identifier="EVENT_708_jmp_to_event_11"),
	Return(),
	JmpToEvent(E0181_NPC_QUEST_4_CONTAINER, identifier="EVENT_708_jmp_to_event_13"),
	Return(),
	JmpToEvent(E0182_NPC_QUEST_5_CONTAINER, identifier="EVENT_708_jmp_to_event_15"),
	Return(),
	JmpToEvent(E0183_NPC_QUEST_6_CONTAINER, identifier="EVENT_708_jmp_to_event_17"),
	Return()
])
