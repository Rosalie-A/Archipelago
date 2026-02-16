# E1669_NIMBUS_FINAL_HALLWAY_MINIBOSS_COLLISION
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
	FreezeAllNPCsUntilReturn(),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1669_set_var_to_const_4"]),
	SetBit(DODO_PRESENT_IN_NIMBUS_HALL),
	JmpToEvent(E0255_EXP_STAR_HIT),
	SetVarToConst(PRIMARY_TEMP_7000, 520, identifier="EVENT_1669_set_var_to_const_4"),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	ClearBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1),
		A_JumpToHeight(height=0, silent=True)
	]),
	SetVarToConst(TEMP_70AB, 22),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	UnfreezeAllNPCs(),
	JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_1669_ret_19"]),
	SetBit(STATUE_KEEPER_STAR_PIECE),
	RunEventAsSubroutine(E1230_STATUE_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 520),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(identifier="EVENT_1669_ret_19")
])
