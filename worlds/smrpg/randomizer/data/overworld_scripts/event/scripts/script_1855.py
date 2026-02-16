# E1855_KEEP_DONKEY_ROOM_BARREL
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
	SetBit(TEMP_7043_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_PlaySound(sound=SO105_SURPRISE, channel=4),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True),
		A_FloatingOn(),
		A_Walk1StepSouth(identifier="EVENT_1855_action_queue_1_SUBSCRIPT_walk_1_step_south_7"),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
		A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_1855_action_queue_1_SUBSCRIPT_walk_1_step_south_7"]),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(1, identifier="EVENT_1855_action_queue_1_SUBSCRIPT_pause_13"),
		A_JmpIfMarioInAir(["EVENT_1855_action_queue_1_SUBSCRIPT_pause_13"])
	]),
	Jmp(["EVENT_1830_store_coin_amount_7000_10"])
])
