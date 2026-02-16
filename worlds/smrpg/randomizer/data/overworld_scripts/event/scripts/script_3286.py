# E3286_SHIP_INTERACT_WITH_BOSS_AFTER_WINNING
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
	JmpIfMarioOnAnObjectOrNot(['EVENT_3286_enable_controls_until_return_6', 'EVENT_3286_enable_controls_until_return_6']),
	JmpIfBitClear(JOHNNY_POSITION, ["EVENT_3286_run_dialog_4"]),
	RunDialog(dialog_id=DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI1780_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3286_run_dialog_4"),
	Return(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3286_enable_controls_until_return_6"),
	StartLoopNTimes(59),
	Pause(1),
	JmpIfMarioInAir(["EVENT_3286_ret_13"]),
	EndLoop(),
	EnableControlsUntilReturn([]),
	RunDialog(dialog_id=DI1781_SHIP_BOSS_JUMP_ON_HEAD, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(identifier="EVENT_3286_ret_13")
])
