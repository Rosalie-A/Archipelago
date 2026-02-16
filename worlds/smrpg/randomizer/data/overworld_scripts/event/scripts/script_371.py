# E0371_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_LOADER
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
	RunBackgroundEvent(event_id=E0377_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_REPEATING_SHYSTERS_POSITION, return_on_level_exit=True, bit_6=True),
    RunBackgroundEvent(event_id=E0329_KINGDOM_MAIN_HALL_FLIP_UPPER, return_on_level_exit=True),
	RunEventAsSubroutine(E0765_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_SHUFFLED_NPC_ANIMATION_LOADER),
	ClearBit(TEMP_7042_7),
	ClearBit(TEMP_7042_6),
	FadeInFromBlack(sync=False),
	Return()
])
