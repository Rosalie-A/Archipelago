# E3497_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ITEM_GRANTER
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
	Pause(1, identifier="EVENT_3497_pause_0"),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_3497_pause_0"]),
	SetSyncActionScript(NPC_1, A0043_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
	JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_3497_pause_8"]),
	Pause(1, identifier="EVENT_3497_pause_4"),
	JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_3497_run_event_as_subroutine_7"]),
	Jmp(["EVENT_3497_pause_4"]),
	RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT, identifier="EVENT_3497_run_event_as_subroutine_7"),
	Pause(1, identifier="EVENT_3497_pause_8"),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3497_pause_8"]),
	SetSyncActionScript(NPC_5, A0042_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_RIGHT_GOOMBA),
	Pause(20),
	SetSyncActionScript(NPC_6, A0041_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_LEFT_GOOMBA),
	Return()
])
