# E3610_KEEP_INVISIBLE_FLOOR_COINS
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
	JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3610_jmp_to_event_4"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 30, ["EVENT_3610_jmp_to_event_5"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3610_jmp_to_event_6"]),
	JmpToEvent(E1842_KEEP_INVISIBLE_FLOOR_COIN_1),
	JmpToEvent(E1881_KEEP_INVISIBLE_FLOOR_COIN_2, identifier="EVENT_3610_jmp_to_event_4"),
	JmpToEvent(E1882_KEEP_INVISIBLE_FLOOR_COIN_3, identifier="EVENT_3610_jmp_to_event_5"),
	JmpToEvent(E1929_KEEP_INVISIBLE_FLOOR_COIN_4, identifier="EVENT_3610_jmp_to_event_6")
])
