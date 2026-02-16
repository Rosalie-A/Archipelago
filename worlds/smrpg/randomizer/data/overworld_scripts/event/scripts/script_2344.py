# E2344_TOWER_THWOMP_SEESAW_ROOM_LOADER
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
	SummonObjectToSpecificLevel(NPC_0, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
	SummonObjectToSpecificLevel(NPC_1, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
	SummonObjectToSpecificLevel(NPC_2, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(12),
		A_WalkSoutheastPixels(2),
		A_WalkNorthPixels(1),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownPixels(4),
		A_WalkNorthPixels(15),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(5),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_2344_freeze_camera_9"]),
	FadeInFromBlack(sync=False),
	Return(),
	FreezeCamera(identifier="EVENT_2344_freeze_camera_9"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftToXYCoords(x=4, y=110),
		A_ShiftZUpSteps(16)
	]),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_2344_action_queue_13_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2344_action_queue_13_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	UnfreezeCamera(),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
