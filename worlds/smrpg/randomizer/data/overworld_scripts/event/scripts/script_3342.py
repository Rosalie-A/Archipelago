# E3342_VOLCANO_5TH_BOSS_PATH_ROOM_LOADER
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
	JmpIfBitSet(VOLCANO_STAIRCASE_ANIMATION_COMPLETED, ["EVENT_3342_run_event_as_subroutine_3"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFSteps(x=0, y=0, z=8, direction=EAST)
	]),
	RunEventAsSubroutine(E0843_VOLCANO_POST_BOSS_ROOM_WITH_ENEMY_WARPS_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3342_run_event_as_subroutine_3"),
	JmpIfBitSet(VOLCANO_STAIRCASE_ANIMATION_COMPLETED, ["EVENT_3342_ret_6"]),
	RunBackgroundEvent(event_id=E3345_VOLCANO_CHASE_SEQEUNCE, return_on_level_exit=True),
	Return(identifier="EVENT_3342_ret_6")
])
