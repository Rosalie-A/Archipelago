# E3797_ENDING_CREDITS_ROOM_LOADER
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
	FadeOutMusicToVolume(duration=0, volume=1),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	SetBit(FACTORY_BOSS_DEFEATED),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	JmpIfBitSet(WIN_CONDITION_STAR_PIECES, ["EVENT_3797_jmp_if_bit_set_9"]),
	JmpIfBitSet(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_3797_jmp_if_bit_set_9"]),
	JmpToEvent(E3885_END_GAME),
	JmpIfBitSet(BUCKET_WARP_DIRECTIONAL_BIT, ["EVENT_3797_enter_area_15"], identifier="EVENT_3797_jmp_if_bit_set_9"),
	JmpIfBitSet(CASINO_WARP_DIRECTIONAL_BIT, ["EVENT_3797_clear_bit_17"]),
	ClearBit(BUCKET_WARP_DIRECTIONAL_BIT),
	ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTHEAST, x=7, y=82, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=3, y=62, z=1, run_entrance_event=True, identifier="EVENT_3797_enter_area_15"),
	Return(),
	ClearBit(BUCKET_WARP_DIRECTIONAL_BIT, identifier="EVENT_3797_clear_bit_17"),
	ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
	EnterArea(room_id=R092_GRATE_GUYS_CASINO_INSIDE_CASINO, face_direction=SOUTH, x=3, y=13, z=10, run_entrance_event=True),
	Return()
])
