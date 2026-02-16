# E3154_RESUMMON_ROSE_WAY_NPCS
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
	ClearBit(TEMP_707C_1),
	SummonObjectToSpecificLevel(NPC_13, R079_ROSE_WAY_MAIN_AREA),
	SummonObjectToSpecificLevel(NPC_14, R079_ROSE_WAY_MAIN_AREA),
	SummonObjectToSpecificLevel(NPC_15, R079_ROSE_WAY_MAIN_AREA),
	SummonObjectToSpecificLevel(NPC_16, R079_ROSE_WAY_MAIN_AREA),
	SummonObjectToSpecificLevel(NPC_3, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS),
	SummonObjectToSpecificLevel(NPC_4, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS),
	SummonObjectToSpecificLevel(NPC_1, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_2, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_3, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_4, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_5, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_6, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_10, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	SummonObjectToSpecificLevel(NPC_11, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	ExitToWorldMap(area=OW17_ROSE_WAY, bit_6=True, bit_7=True),
	Return()
])
