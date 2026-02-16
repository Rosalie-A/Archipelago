# E0320_MUSHROOM_KINGDOM_MAIN_HALL_LOADER
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
	Set0158Bit7Offset(0x015C),
	Set0158Bit7Offset(0x015E),
	ClearBit(TEMP_7042_7),
	ClearBit(TEMP_7042_6),
    JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_320_fade_in_from_black_async"]),
    JmpIfObjectNotInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_320_fade_in_from_black_async"]),
    SummonObjectToCurrentLevel(NPC_4),
    SetSyncActionScript(NPC_4, A0111_MK_HALL_REPEATING_HENCHMEN_STARTING),
    SummonObjectToCurrentLevel(NPC_5),
    SetSyncActionScript(NPC_5, A0112_MK_HALL_TOAD),
	FadeInFromBlack(sync=False, identifier="EVENT_320_fade_in_from_black_async"),
    RunBackgroundEvent(event_id=E0324_KINGDOM_MAIN_HALL_FLIP_VERANDA, return_on_level_exit=True),
	Return()
])
