# E3224_SHIP_PASSWORD_ROOM_LOADER
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
	SummonObjectToCurrentLevel(NPC_0),
	SummonObjectToCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_4),
	SummonObjectToCurrentLevel(NPC_5),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	ResumeActionScript(NPC_2),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ResumeActionScript(NPC_5),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	SetVarToConst(TEMP_702E, 0),
	SetVarToConst(TEMP_70AC, 0),
	RunEventAsSubroutine(E0800_SHIP_PASSWORD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitClear(TEMP_7042_6, ["EVENT_3224_run_event_as_subroutine_25"]),
	ApplySolidityModToLevel(permanent=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=32),
	SetBit(TEMP_7043_0),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3224_run_event_as_subroutine_25"),
	RunBackgroundEvent(event_id=E3225_SHIP_PASSWORD_BOX_DIALOG, return_on_level_exit=True),
	Return()
])
