# E1683_TEMPLE_EXIT_WARP_TRAMPOLINE
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
	JmpIfBitClear(TRAMPOLINE_SHAMAN_PAID, ["EVENT_1682_copy_var_to_var_0"]),
	JmpIfBitSet(TEMP_7076_0, ["EVENT_1583_action_queue_6"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=NORTH, x=7, y=118, z=0),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_JumpToHeight(height=144, silent=True),
		A_Walk1StepNorth(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_1683_action_queue_5_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_1683_action_queue_5_SUBSCRIPT_pause_6"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER)
])
