# E0167_BOSS_GRANT_STAR_PIECE
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
	ClearBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	ClearBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT_2),
	Inc(BOSS_VICTORY_COUNTER),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_167_ret_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 103, ["EVENT_167_ret_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_167_ret_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 159, ["EVENT_167_jmp_to_event_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 173, ["EVENT_167_ret_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_167_ret_49"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 202, ["EVENT_167_ret_50"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 205, ["EVENT_167_ret_51"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 206, ["EVENT_167_ret_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 223, ["EVENT_167_ret_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_167_jmp_to_event_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 254, ["EVENT_167_ret_55"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_167_ret_56"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 266, ["EVENT_167_ret_57"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 268, ["EVENT_167_ret_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 271, ["EVENT_167_jmp_to_event_59"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 302, ["EVENT_167_ret_60"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 316, ["EVENT_167_jmp_to_event_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 326, ["EVENT_167_jmp_to_event_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 351, ["EVENT_167_ret_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_167_ret_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 393, ["EVENT_167_jmp_to_event_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 409, ["EVENT_167_ret_66"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 438, ["EVENT_167_ret_67"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 461, ["EVENT_167_ret_68"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 469, ["EVENT_167_ret_69"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 470, ["EVENT_167_ret_70"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 471, ["EVENT_167_ret_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 472, ["EVENT_167_ret_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 496, ["EVENT_167_ret_73"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 512, ["EVENT_167_ret_74"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_167_ret_75"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 514, ["EVENT_167_ret_76"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 515, ["EVENT_167_ret_77"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 516, ["EVENT_167_ret_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 517, ["EVENT_167_ret_79"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 518, ["EVENT_167_ret_80"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 519, ["EVENT_167_ret_81"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 520, ["EVENT_167_ret_82"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 521, ["EVENT_167_ret_83"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 522, ["EVENT_167_ret_84"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 523, ["EVENT_167_ret_85"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 524, ["EVENT_167_ret_86_monstro_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 525, ["EVENT_167_ret_87_dojo_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 526, ["EVENT_167_ret_88_ship_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 527, ["EVENT_167_ret_89_mines_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 528, ["EVENT_167_ret_90_tower_postgame"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 529, ["EVENT_167_ret_91_chapel_postgame"]),
	Return(),
	Return(identifier="EVENT_167_ret_44"),
	Return(identifier="EVENT_167_ret_45"),
	Return(identifier="EVENT_167_ret_46"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_47"),
	Return(identifier="EVENT_167_ret_48"),
	Return(identifier="EVENT_167_ret_49"),
	Return(identifier="EVENT_167_ret_50"),
	Return(identifier="EVENT_167_ret_51"),
	Return(identifier="EVENT_167_ret_52"),
	Return(identifier="EVENT_167_ret_53"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_54"),
	Return(identifier="EVENT_167_ret_55"),
	Return(identifier="EVENT_167_ret_56"),
	Return(identifier="EVENT_167_ret_57"),
	Return(identifier="EVENT_167_ret_58"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_59"),
	Return(identifier="EVENT_167_ret_60"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_61"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_62"),
	Return(identifier="EVENT_167_ret_63"),
	Return(identifier="EVENT_167_ret_64"),
	JmpToEvent(E3092_STAR_PIECE_GRANT, identifier="EVENT_167_jmp_to_event_65"),
	Return(identifier="EVENT_167_ret_66"),
	Return(identifier="EVENT_167_ret_67"),
	Return(identifier="EVENT_167_ret_68"),
	Return(identifier="EVENT_167_ret_69"),
	Return(identifier="EVENT_167_ret_70"),
	Return(identifier="EVENT_167_ret_71"),
	Return(identifier="EVENT_167_ret_72"),
	Return(identifier="EVENT_167_ret_73"),
	Return(identifier="EVENT_167_ret_74"),
	Return(identifier="EVENT_167_ret_75"),
	Return(identifier="EVENT_167_ret_76"),
	Return(identifier="EVENT_167_ret_77"),
	Return(identifier="EVENT_167_ret_78"),
	Return(identifier="EVENT_167_ret_79"),
	Return(identifier="EVENT_167_ret_80"),
	Return(identifier="EVENT_167_ret_81"),
	Return(identifier="EVENT_167_ret_82"),
	Return(identifier="EVENT_167_ret_83"),
	Return(identifier="EVENT_167_ret_84"),
	Return(identifier="EVENT_167_ret_85"),
	Return(identifier="EVENT_167_ret_86_monstro_postgame"),
	Return(identifier="EVENT_167_ret_87_dojo_postgame"),
	Return(identifier="EVENT_167_ret_88_ship_postgame"),	
	Return(identifier="EVENT_167_ret_89_mines_postgame"),	
	Return(identifier="EVENT_167_ret_90_tower_postgame"),
	Return(identifier="EVENT_167_ret_91_chapel_postgame"),
])
