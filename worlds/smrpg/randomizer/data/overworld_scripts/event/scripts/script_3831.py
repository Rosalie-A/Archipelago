# E3831_MUSHROOM_KINGDOM_SHOP_CELLAR_MOD
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
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_apply_tile_mod_4"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_apply_tile_mod_6"], identifier="EVENT_3831_jmp_if_object_trigger_disabled_1"),
	FadeInFromBlack(sync=False, identifier="EVENT_3831_fade_in_from_black_async_2"),
	Return(),
	ApplyTileModToLevel(use_alternate=True, room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, mod_id=0, identifier="EVENT_3831_apply_tile_mod_4"),
	Jmp(["EVENT_3831_jmp_if_object_trigger_disabled_1"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, mod_id=1, identifier="EVENT_3831_apply_tile_mod_6"),
	Jmp(["EVENT_3831_fade_in_from_black_async_2"])
])
