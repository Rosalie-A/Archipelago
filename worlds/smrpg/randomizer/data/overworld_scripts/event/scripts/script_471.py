# E0471_BOSHI
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
	PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_471_enable_controls_until_return_11"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_471_run_event_as_subroutine_14"]),
	JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_462_jmp_to_event_10"]),
	JmpIfBitSet(GOT_FREE_COOKIES, ["EVENT_471_run_event_as_subroutine_9"]),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
	RunDialog(dialog_id=DI0906_BOSHI_BEFORE_YOU_BEAT_HIM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_471_run_event_as_subroutine_9"),
	JmpToEvent(E0476_INITIATE_MUSHROOM_DERBY_FROM_TALKING_TO_BOSHI),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_471_enable_controls_until_return_11"),
	Pause(32),
	Return(),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_471_run_event_as_subroutine_14"),
	RunDialog(dialog_id=DI0946_LETS_RACE_AGAIN_SOMETIME, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI, identifier="EVENT_471_run_event_as_subroutine_18"),
	RunDialog(dialog_id=DI0909_THAT_CANT_HAPPEN_TWICE, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return()
])
