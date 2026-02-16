# E0377_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_REPEATING_SHYSTERS_POSITION
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
	SetSyncActionScript(NPC_2, A0108_MK_HALL_REPEATING_HENCHMEN),
	PauseActionScript(NPC_0, identifier="EVENT_377_pause_action_script_1"),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_BPL262728()
	]),
	SetSyncActionScript(NPC_0, A0110_MK_HALL_REPEATING_HENCHMEN),
	Pause(150),
	PauseActionScript(NPC_1),
	StartAsyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_BPL262728()
	]),
	SetSyncActionScript(NPC_1, A0110_MK_HALL_REPEATING_HENCHMEN),
	Pause(150),
	Jmp(["EVENT_377_pause_action_script_1"])
])
