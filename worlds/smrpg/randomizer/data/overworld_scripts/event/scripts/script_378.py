# E0378_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_SHYSTER_CHASING_TOAD
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
	SetBit(TEMP_707C_5),
	SetBit(TEMP_707C_7),
	SetBit(TEMP_707C_6),
	RunEventAsSubroutine(E0051_HENCHMAN_CONTAINER_1),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	StopAllBackgroundEvents(),
	PauseActionScript(NPC_5),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=4, y=25, z=4, direction=EAST),
		A_VisibilityOn(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=5, y=24, z=4, direction=EAST),
		A_FaceSouthwest()
	]),
	SetBit(TEMP_7049_6),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(2),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_5, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL),
    RemoveObjectFromSpecificLevel(NPC_4, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_5, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	Return()
])
