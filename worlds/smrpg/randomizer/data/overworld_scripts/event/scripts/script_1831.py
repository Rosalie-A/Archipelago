# E1831_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_1
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
	Pause(1, identifier="EVENT_1831_pause_0"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1831_set_bit_3"]),
	Jmp(["EVENT_1831_pause_0"]),
	SetBit(TEMP_7043_2, identifier="EVENT_1831_set_bit_3"),
	ClearBit(TEMP_7043_1),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[LAYER_L3], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY]),
	Pause(6),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY]),
	ClearBit(TEMP_7043_2),
	Jmp(["EVENT_1831_pause_0"])
])
