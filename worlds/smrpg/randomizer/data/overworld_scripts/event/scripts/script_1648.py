# E1648_MINECART_ENDING
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 24),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1648_set_bit_15"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1648_fade_in_from_black_sync_9"]),
	FadeInFromBlack(sync=False),
	StartLoopNTimes(249),
	PlaySound(sound=SO001_MENU_SELECT, channel=6),
	Pause(4),
	EndLoop(),
	Return(),
	FadeInFromBlack(sync=True, identifier="EVENT_1648_fade_in_from_black_sync_9"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=192, silent=True),
		A_Walk1StepSouth(),
		A_FloatingOn()
	]),
	Pause(1, identifier="EVENT_1648_pause_11"),
	JmpIfMarioInAir(["EVENT_1648_pause_11"]),
	PlaySound(sound=SO058_INSERT, channel=6),
	Return(),
	SetBit(MINECART_CRASH_CUTSCENE_CLEARED, identifier="EVENT_1648_set_bit_15"),
	JmpIfBitSet(OPTIONAL_MINECART_CLEARED, ["EVENT_1648_clear_bit_18"]),
	JmpToEvent(E1651_MARIO_CRASH_THRU_MOLEVILLE_ROOF),
	ClearBit(PAID_FOR_MINECART, identifier="EVENT_1648_clear_bit_18"),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTHWEST, x=28, y=39, z=4, run_entrance_event=True),
	Return()
])
