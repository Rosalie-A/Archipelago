# E1891_ABYSS_BIG_CONVEYOR_ROOM_LOADER
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
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetBit(ABYSS_TRAMPOLINE_DIRECTIONAL_BIT),
	ApplyTileModToLevel(use_alternate=False, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	ApplySolidityModToLevel(permanent=False, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	JmpIfBitClear(ABYSS_FINAL_ROOM_TRAMPOLINE, ["EVENT_1891_fade_in_from_black_async_7"]),
	JmpToSubroutine(["EVENT_1897_fade_in_from_black_sync_7"]),
	Jmp(["EVENT_1891_run_background_event_8"]),
	FadeInFromBlack(sync=False, identifier="EVENT_1891_fade_in_from_black_async_7"),
	RunBackgroundEvent(event_id=E1900_ABYSS_BIG_CONVEYOR_ROOM_FALL, return_on_level_exit=True, identifier="EVENT_1891_run_background_event_8"),
	Return()
])
