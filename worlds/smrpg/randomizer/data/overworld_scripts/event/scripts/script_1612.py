# E1612_SUMMON_GECKITS_IN_CANNON_ROOM
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
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_11),
	RemoveObjectFromCurrentLevel(NPC_12),
	Pause(21),
	SetVarToConst(TEMP_70AB, 25),
	StartLoopNTimes(3),
	JmpIfObjectNotInSpecificLevel(MEM_70AB, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL, ["EVENT_1612_inc_13"]),
	SetSyncActionScript(MEM_70AB, A0126_CANNON_GECKIT),
	Inc(TEMP_70AB, identifier="EVENT_1612_inc_13"),
	EndLoop(),
	Pause(238),
	SetVarToConst(TEMP_70AB, 29),
	StartLoopNTimes(3),
	JmpIfObjectNotInSpecificLevel(MEM_70AB, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL, ["EVENT_1612_inc_20"]),
	SetSyncActionScript(MEM_70AB, A0126_CANNON_GECKIT),
	Inc(TEMP_70AB, identifier="EVENT_1612_inc_20"),
	EndLoop(),
	Return()
])
