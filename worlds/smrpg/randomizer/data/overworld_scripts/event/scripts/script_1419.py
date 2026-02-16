# E1419_MUSHROOM_WAY_1_EXIT_TO_WORLD_MAP
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	SummonObjectToSpecificLevel(NPC_2, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_3, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_4, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_5, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_6, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_7, R203_MUSHROOM_WAY_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_3, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_4, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_5, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_6, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_9, R204_MUSHROOM_WAY_AREA_02),
	ExitToWorldMap(area=OW09_MUSHROOM_WAY, bit_6=True, bit_7=True),
	Return()
])
