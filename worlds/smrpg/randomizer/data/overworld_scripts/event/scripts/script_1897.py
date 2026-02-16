# E1897_ABYSS_UPPER_MACHINE_YARID_ROOM_LOADER
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
	SetBit(ABYSS_TWO_CHEST_ROOM_DIRECTIONAL_BIT),
	JmpIfBitSet(UNKNOWN_DIRECTIONAL_BIT_2, ["EVENT_1897_action_queue_3"]),
	ApplySolidityModToLevel(permanent=True, room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS, mod_id=0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(4),
		A_WalkSouthPixels(8),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_7=True)
	], identifier="EVENT_1897_action_queue_3"),
	JmpIfBitSet(ABYSS_FINAL_ROOM_TRAMPOLINE, ["EVENT_1897_fade_in_from_black_sync_7"]),
	FadeInFromBlack(sync=False),
	Return(),
	FadeInFromBlack(sync=True, identifier="EVENT_1897_fade_in_from_black_sync_7"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferXYZFSteps(x=0, y=255, z=30, direction=NORTHEAST),
		A_JumpToHeight(height=112, silent=True),
		A_Walk1StepSouth(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_1897_action_queue_8_SUBSCRIPT_pause_7"),
		A_JmpIfMarioInAir(["EVENT_1897_action_queue_8_SUBSCRIPT_pause_7"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	ClearBit(ABYSS_FINAL_ROOM_TRAMPOLINE),
	Return()
])
