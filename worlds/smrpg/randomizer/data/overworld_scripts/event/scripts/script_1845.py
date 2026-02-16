# E1845_CLOUD_BOSS
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
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1845_disable_trigger_3"]),
	RunEventAsSubroutine(E0255_EXP_STAR_HIT),
	Jmp(["EVENT_1845_jmp_if_bit_set_10"]),
	DisableObjectTrigger(MEM_70A8, identifier="EVENT_1845_disable_trigger_3"),
	ClearBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	SetVarToConst(PRIMARY_TEMP_7000, 519),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	JmpIfBitSet(LANDS_END_CLOUD_STAR_PIECE, ["EVENT_1845_ret_14"], identifier="EVENT_1845_jmp_if_bit_set_10"),
	SetBit(LANDS_END_CLOUD_STAR_PIECE),
	RunEventAsSubroutine(E1210_CLOUD_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 519),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(identifier="EVENT_1845_ret_14")
])
