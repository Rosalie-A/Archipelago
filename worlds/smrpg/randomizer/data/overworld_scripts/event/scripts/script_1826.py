# E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER
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
	SetVarToConst(ROSE_WAY_7038, 4224),
	SetVarToConst(ROSE_WAY_703A, 14720),
	SetVarToConst(ROSE_WAY_703C, 512),
	RunBackgroundEvent(event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E1831_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_1, return_on_level_exit=True, bit_6=True),
	RunBackgroundEvent(event_id=E1832_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_2, return_on_level_exit=True, run_as_second_script=True),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1826_play_sound_9"]),
	ClearBit(TEMP_7095_4),
	PlaySound(sound=SO011_WHOOSH_AWAY, channel=6, identifier="EVENT_1826_play_sound_9"),
	SetSyncActionScript(NPC_1, A0822_KEEP_JUMPING_TERRAPIN_INIT),
	SetSyncActionScript(NPC_2, A0822_KEEP_JUMPING_TERRAPIN_INIT),
	SetSyncActionScript(NPC_3, A0822_KEEP_JUMPING_TERRAPIN_INIT),
	JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES)
])
