# E3079_EXP_STAR_LEVELUP_SCREEN
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
	MoveScriptToMainThread(),
	ClearBit(TEMP_7076_0),
	SetBit(EXP_STAR_BIT_5),
	MarioStopsGlowing(),
	JmpIfBitClear(UNKNOWN_7064_4, ["EVENT_3079_enable_controls_7"]),
	RunLevelupBonusSequence(),
	FadeInFromBlack(sync=False),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3079_enable_controls_7"),
	JmpIfBitClear(DODO_PRESENT_IN_NIMBUS_HALL, ["EVENT_3079_jmp_to_event_15"]),
	ClearBit(DODO_PRESENT_IN_NIMBUS_HALL),
	JmpIfBitClear(ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_3079_jmp_to_event_15"]),
	JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_3079_jmp_to_event_15"]),
	SetBit(STATUE_KEEPER_STAR_PIECE),
	RunEventAsSubroutine(E1230_STATUE_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 520),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	JmpToEvent(E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE, identifier="EVENT_3079_jmp_to_event_15"),
	Return()
])
