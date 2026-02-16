# E3330_VOLCANO_1ST_BOSS_ROOM_LOADER
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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToObjectXY(MARIO)
	]),
	Set70107015ToObjectXYZ(target=NPC_0, bit_7=True),
	CopyVarToVar(from_var=X_COORD_1, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7026),
	CopyVarToVar(from_var=Z_COORD_1, to_var=TEMP_7028),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702A),
	RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
	ApplyTileModToLevel(use_alternate=True, room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, mod_id=2),
	RunEventAsSubroutine(E0840_VOLCANO_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["EVENT_3330_ret_16"]),
	RunBackgroundEvent(event_id=E3346_VOLCANO_1ST_BOSS_SCREEN_TINT, return_on_level_exit=True, bit_6=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(5),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNortheastSteps(3)
	]),
	RunEventAtReturn(E3331_VOLCANO_1ST_BOSS_FIGHT),
	Return(identifier="EVENT_3330_ret_16")
])
