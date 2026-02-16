# E0603_MARRYMORE_BELLHOP_LOBBY_WHILE_GUEST
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
	JmpIfBitSet(TEMP_704C_0, ["EVENT_603_run_dialog_13"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_603_run_dialog_6"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_603_run_dialog_15"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_321_inc_0"]),
	RunDialog(dialog_id=DI0979_INACTIVE_BELLHOP, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0992_GOOD_MORNING_FROM_BELLHOP, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_6"),
	RunDialog(dialog_id=DI0995_BELLHOP_GIFT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunEventAsSubroutine(E0635_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUNROUTINE_3),
	SetBit(TEMP_7043_1),
	SetSyncActionScript(NPC_5, A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK),
	Return(),
	RunDialog(dialog_id=DI1006_BELLHOP_WHILE_PLAYER_EMPLOYED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_13"),
	Return(),
	RunDialog(dialog_id=DI0969_MAKE_YOURSELF_AT_HOME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_15"),
	Return()
])
