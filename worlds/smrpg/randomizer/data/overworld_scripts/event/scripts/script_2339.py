# E2339_TOWER_FIRST_STAIRCASE_CONTROLS_NPC_BEHIND_CURTAIN
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
	JmpIfBitSet(TOWER_BOSS_SPOTTED_BEHIND_1ST_CURTAIN, ["EVENT_2339_ret_6"]),
	SetBit(TOWER_BOSS_SPOTTED_BEHIND_1ST_CURTAIN),
	SummonObjectToSpecificLevel(NPC_4, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS),
	SummonObjectToSpecificLevel(NPC_5, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS),
	RemoveObjectFromSpecificLevel(NPC_6, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS),
	SetSyncActionScript(NPC_6, A0702_TOWER_FIRST_STAIRCASE_BOSS),
	Return(identifier="EVENT_2339_ret_6")
])
