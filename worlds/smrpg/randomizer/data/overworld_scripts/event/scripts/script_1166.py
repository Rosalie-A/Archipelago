# E1166_SHED_KEY_DOOR
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
	JmpIfBitClear(SEASIDE_BOSS_SET, ["EVENT_1166_ret_5"]),
	SetVarToConst(ITEM_ID, ShedKeyItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1166_pause_6"]),
	RunDialog(dialog_id=DI2802_NEED_THE_SHED_KEY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return(identifier="EVENT_1166_ret_5"),
	Pause(5, identifier="EVENT_1166_pause_6"),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	ApplySolidityModToLevel(permanent=True, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=0),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromSpecificLevel(NPC_6, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	Pause(5),
	Return()
])
