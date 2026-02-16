# E2245_SETS_MUSHROOM_BOY_SHOP_STATE
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
	JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_2245_jmp_if_bit_set_3"]),
	EnterArea(room_id=R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE, face_direction=NORTHEAST, x=24, y=40, z=0, run_entrance_event=True),
	Return(),
	JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_2245_enter_area_6"], identifier="EVENT_2245_jmp_if_bit_set_3"),
	EnterArea(room_id=R312_SEASIDE_TOWN_MUSHROOM_BOYS_SHOP, face_direction=NORTHEAST, x=24, y=40, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R312_SEASIDE_TOWN_MUSHROOM_BOYS_SHOP, face_direction=NORTHEAST, x=24, y=40, z=0, show_banner=True, run_entrance_event=True, identifier="EVENT_2245_enter_area_6"),
	Return()
])
