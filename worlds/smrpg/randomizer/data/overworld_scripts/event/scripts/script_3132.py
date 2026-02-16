# E3132_MOLEVILLE_MINERS_SONG
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
	SetVarToConst(PRIMARY_TEMP_7000, 1607),
	StartLoopNTimes(7),
	RunDialog(dialog_id=PRIMARY_TEMP_7000, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(10),
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True)
	]),
	Inc(PRIMARY_TEMP_7000),
	EndLoop(),
	RunDialog(dialog_id=DI1615_MOLEVILLE_BLUES_8, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
