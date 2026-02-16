# E3477_KINGDOM_HALLWAY_CHEST
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
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_3477_jmp_if_bit_set_4"]),
	DisableObjectTriggerInSpecificLevel(NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	DisableObjectTriggerInSpecificLevel(NPC_6, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3477_jmp_to_event_9"], identifier="EVENT_3477_jmp_if_bit_set_4"),
	SetBit(TEMP_7042_0),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownSteps(2),
		A_ClearBit(TEMP_7042_0)
	]),
	UnfreezeCamera(),
	JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_3477_jmp_to_event_9")
])
