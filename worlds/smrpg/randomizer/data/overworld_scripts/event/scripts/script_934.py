# E0934_PROGRESSIVE_FIREWORK_CHEST_PACKET
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

script = EventScript([
	RunEventAsSubroutine(E0033_OPEN_CHEST),
    StoreItemAmountTo7000(ShinyStoneItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["chest_carbo_cookie"]),
    StoreItemAmountTo7000(FireworksItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["chest_shiny_stone"]),
	CreatePacketAt7010(packet=P005_BRIEF_POOF_BAG, destinations=["EVENT_943_ret_3"]),
    JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_943_ret_3"),
	CreatePacketAt7010(packet=P093_CRYSTAL_CHEST, destinations=["EVENT_943_ret_4"], identifier="chest_shiny_stone"),
    JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_943_ret_4"),
	CreatePacketAt7010(packet=P073_COOKIE_CHEST, destinations=["EVENT_943_ret_5"], identifier="chest_carbo_cookie"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_943_ret_5"),
	Return()
])
