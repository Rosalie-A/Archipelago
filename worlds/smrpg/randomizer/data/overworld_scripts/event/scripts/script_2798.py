# E2798_STAR_HILL_EXIT_TO_WORLD_MAP
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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2798_freeze_camera_2"]),
	Return(),
	FreezeCamera(identifier="EVENT_2798_freeze_camera_2"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_2798_action_queue_3_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_2798_action_queue_3_SUBSCRIPT_pause_0"]),
		A_OverwriteSolidity(),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	Pause(32),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=3),
	PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
	UnfreezeCamera(),
	Pause(32),
	FadeOutToBlack(sync=False, duration=16),
	ExitToWorldMap(area=OW31_STAR_HILL, bit_6=True, bit_7=True),
	Return()
])
