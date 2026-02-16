# E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT
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
	SummonObjectToSpecificLevel(NPC_0, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_1, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_3, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_4, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_5, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
	SummonObjectToSpecificLevel(NPC_1, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE),
	SummonObjectToSpecificLevel(NPC_2, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE),
	SummonObjectToSpecificLevel(NPC_3, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE),
	SummonObjectToSpecificLevel(NPC_4, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE),
	SummonObjectToSpecificLevel(NPC_2, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_3, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_4, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_5, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_1, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_2, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_3, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_4, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_5, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	SummonObjectToSpecificLevel(NPC_6, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM),
	ExitToWorldMap(area=OW04_BOWSERS_KEEP, bit_6=True, bit_7=True),
	Return()
])
