# E0357_EXP_STAR_MUSIC_EXPERIMENT
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 224, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 225, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 226, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 227, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 228, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 229, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 230, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 231, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 233, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 235, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 236, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 256, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 35, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 36, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 37, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 38, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 39, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 40, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 42, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 43, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 48, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 193, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 194, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 195, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 196, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 197, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 198, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 200, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 201, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 258, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 259, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 26, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 160, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 161, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 162, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 163, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 164, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 165, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 166, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 167, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 168, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 169, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 170, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 171, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 172, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 173, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 175, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 176, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 177, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 178, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 179, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 180, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 181, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 182, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 183, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 184, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 185, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 186, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 187, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 188, ["EVENT_357_play_music_current_volume_72"]),
	Return(),
	PlayMusicAtCurrentVolume(M0008_INVINCIBLESTAR, identifier="EVENT_357_play_music_current_volume_72"),
	Return()
])
