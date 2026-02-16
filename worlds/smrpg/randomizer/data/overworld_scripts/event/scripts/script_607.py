# E0607_LOCKED_DOOR
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 409, ["EVENT_607_store_item_amount_7000_4"]),
	RunDialog(dialog_id=DI2811_ITS_LOCKED, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return(),
	StoreItemAmountTo7000(CastleKey2Item, identifier="EVENT_607_store_item_amount_7000_4"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_607_play_sound_8"]),
	RunDialog(dialog_id=DI2811_ITS_LOCKED, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return(),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_607_play_sound_8"),
	Pause(8),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	Pause(8),
	ApplySolidityModToLevel(permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=1),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_7, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
	RemoveOneOfItemFromInventory(CastleKey2Item),
	Return()
])
