# E0406_YOUNGER_BROTHER
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
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_406_pause_action_script_9"]),
	PauseActionScript(NPC_0),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=0, silent=True)
	]),
	Pause(1, identifier="EVENT_406_pause_3"),
	JmpIfObjectInAir(NPC_0, ["EVENT_406_pause_3"]),
	RunDialog(dialog_id=DI0693_JUMPING_KID_DURING_OCCUPATION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(NPC_0, A0022_SLOW_REPEATED_JUMPING),
	Return(),
	PauseActionScript(NPC_0, identifier="EVENT_406_pause_action_script_9"),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=0, silent=True)
	]),
	Pause(1, identifier="EVENT_406_pause_11"),
	JmpIfObjectInAir(NPC_0, ["EVENT_406_pause_11"]),
	RunDialog(dialog_id=DI0694_JUMPING_KID_DURING_OCCUPATION_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
	Return()
])
