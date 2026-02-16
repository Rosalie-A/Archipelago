# E1116_JUICE_BAR
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
	SetVarToConst(ITEM_ID, SopranoCardItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_jmp_to_event_10"]),
	SetVarToConst(ITEM_ID, TenorCardItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_jmp_to_event_11"]),
	SetVarToConst(ITEM_ID, AltoCardItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_jmp_to_event_12"]),
	JmpToEvent(E1179_JUICE_BAR_NO_CARD),
	JmpToEvent(E1182_JUICE_BAR_SOPRANO_CARD, identifier="EVENT_1116_jmp_to_event_10"),
	JmpToEvent(E1181_JUICE_BAR_TENOR_CARD, identifier="EVENT_1116_jmp_to_event_11"),
	JmpToEvent(E1180_JUICE_BAR_ALTO_CARD, identifier="EVENT_1116_jmp_to_event_12")
])
