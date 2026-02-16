# E3376_KEEP_6_DOOR_LOBBY_LOADER
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
	SpeedUpMusicToDefault(),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_5"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=0),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_copy_var_to_var_8"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_5"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=1),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3376_copy_var_to_var_8"),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_12"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=2),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_copy_var_to_var_15"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_12"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=3),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=3),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3376_copy_var_to_var_15"),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_19"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=4),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_jmp_if_bit_set_22"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_19"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=5),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=5),
	JmpIfBitSet(UNKNOWN_BOWSERS_KEEP_707F_0, ["EVENT_3356_clear_bit_5"], identifier="EVENT_3376_jmp_if_bit_set_22"),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	SetVarToConst(KEEP_DOOR_LIVES, 10, identifier="EVENT_3376_set_var_to_const_25"),
	Mem7000AndConst(0x0007),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=KEEP_DOORS_EXIT_TYPE_2),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3376_jmp_to_event_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_3376_jmp_to_event_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_3376_jmp_to_event_40"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3376_jmp_to_event_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3376_jmp_to_event_42"]),
	JmpToEvent(E1957_KEEP_DOOR_5_CONTAINER),
	JmpToEvent(E1959_KEEP_DOOR_4_CONTAINER, identifier="EVENT_3376_jmp_to_event_38"),
	JmpToEvent(E1961_KEEP_DOOR_6_CONTAINER, identifier="EVENT_3376_jmp_to_event_39"),
	JmpToEvent(E1963_KEEP_DOOR_3_CONTAINER, identifier="EVENT_3376_jmp_to_event_40"),
	JmpToEvent(E1965_KEEP_DOOR_1_CONTAINER, identifier="EVENT_3376_jmp_to_event_41"),
	JmpToEvent(E1967_KEEP_DOOR_2_CONTAINER, identifier="EVENT_3376_jmp_to_event_42")
])
