# E3152_ROSE_WAY_FIVE_CHESTS
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
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3152_set_bit_6"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3152_set_bit_8"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3152_set_bit_10"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3152_set_bit_12"]),
	SetBit(TEMP_7043_0),
	JmpToEvent(E0172_CHEST_1_CONTAINER),
	SetBit(TEMP_7043_1, identifier="EVENT_3152_set_bit_6"),
	JmpToEvent(E0173_CHEST_2_CONTAINER),
	SetBit(TEMP_7043_2, identifier="EVENT_3152_set_bit_8"),
	JmpToEvent(E0174_CHEST_3_CONTAINER),
	SetBit(TEMP_7043_3, identifier="EVENT_3152_set_bit_10"),
	JmpToEvent(E0175_CHEST_4_CONTAINER),
	SetBit(TEMP_7043_4, identifier="EVENT_3152_set_bit_12"),
	JmpToEvent(E0176_CHEST_5_CONTAINER)
])
