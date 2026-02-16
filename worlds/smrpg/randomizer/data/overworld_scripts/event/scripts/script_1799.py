# E1799_TEMPLE_FINAL_FORTUNE_SCROLL
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
	PlaySound(sound=SO084_SMOKED, channel=6),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	StartLoopNTimes(2),
	Pause(1, identifier="EVENT_1799_pause_4"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1799_pause_4"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	EndLoop(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	JmpIfBitSet(TEMPLE_BOSS_ACCESS_FORTUNE, ["EVENT_1799_run_dialog_13"]),
	RunDialog(dialog_id=DI1238_TEMPLE_TREASURY_FORTUNE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI1230_TEMPLE_BOSS_FORTUNE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1799_run_dialog_13"),
	Return()
])
