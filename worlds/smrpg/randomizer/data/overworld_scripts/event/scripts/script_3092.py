# E3092_STAR_PIECE_GRANT
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
	Pause(1, identifier="EVENT_3092_pause_0"),
	JmpIfMarioInAir(["EVENT_3092_pause_0"]),
	JmpIfBitSet(STAR_PIECE_MENU_UNLOCKED, ["EVENT_3092_jmp_if_var_equals_const_4"]),
	SetBit(STAR_PIECE_MENU_UNLOCKED),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 7, ["EVENT_3092_a"], identifier="EVENT_3092_jmp_if_var_equals_const_4"),
	Inc(STAR_PIECE_COUNTER),
	PlayMusicAtCurrentVolume(M0024_GOTASTARPIECE_PART2, identifier="EVENT_3092_a"),
	UnknownCommand(bytearray(b'\xfd\x8e\x80\x07\x01')),
	PauseScriptUntilEffectDone(),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 7, ["EVENT_3092_run_star_piece_sequence_29"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 6, ["EVENT_3092_run_star_piece_sequence_27"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 5, ["EVENT_3092_run_star_piece_sequence_25"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 4, ["EVENT_3092_run_star_piece_sequence_23"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 3, ["EVENT_3092_run_star_piece_sequence_21"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 2, ["EVENT_3092_run_star_piece_sequence_19"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 1, ["EVENT_3092_run_star_piece_sequence_17"]),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(1, identifier="EVENT_3092_run_star_piece_sequence_17"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(2, identifier="EVENT_3092_run_star_piece_sequence_19"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(3, identifier="EVENT_3092_run_star_piece_sequence_21"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(4, identifier="EVENT_3092_run_star_piece_sequence_23"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(5, identifier="EVENT_3092_run_star_piece_sequence_25"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(6, identifier="EVENT_3092_run_star_piece_sequence_27"),
	Jmp(["EVENT_3092_db_30"]),
	RunStarPieceSequence(7, identifier="EVENT_3092_run_star_piece_sequence_29"),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\x01'), identifier="EVENT_3092_db_30"),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E3101_STAR_PIECE_HUNT_END_GAME),
	Return(identifier="EVENT_3092_ret_33")
])
