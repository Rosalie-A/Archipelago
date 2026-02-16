# E1762_LANDS_END_STAGE_2_WHIRLPOOL_3
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
	JmpIfObjectNotInSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04, ["EVENT_1762_run_event_as_subroutine_3"]),
	SetVarToConst(ACTIVE_NPC, 23),
	Jmp(["EVENT_1886_jmp_if_bit_set_4"]),
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL, identifier="EVENT_1762_run_event_as_subroutine_3"),
	EnterArea(room_id=R403_LANDS_END_DESERT_AREA_05, face_direction=SOUTH, x=27, y=60, z=0),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	SetVarToConst(ACTIVE_NPC, 20),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE)
])
