# E3080_COIN_CHEST_QUICK_HIT
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
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	RunEventAsSubroutine(E0033_OPEN_CHEST),
	PlaySound(sound=SO013_COIN, channel=6),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	AddCoins(PRIMARY_TEMP_7000),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_3080_pkt_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_3080_pkt_1"]),
	CreatePacketAt7010(packet=P091_CHEST_COIN_STILL, destinations=["EVENT_3080_pk_1"]),
	RunDialog(dialog_id=DI4050_GOT_X_COINS_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_3080_pk_1"),
	Return(),
	CreatePacketAt7010(packet=P090_SMALL_COIN_STILL, destinations=["EVENT_3080_pk_2"], identifier="EVENT_3080_pkt_1"),
    JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3080_pk_1"]),
	RunDialog(dialog_id=DI4047_GOT_A_COIN_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_3080_pk_2"),
	Return()
])
