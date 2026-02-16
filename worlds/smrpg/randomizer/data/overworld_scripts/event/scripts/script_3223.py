# E3223_SHIP_TROOPA_PUZZLE
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
	Pause(1, identifier="EVENT_3223_pause_0"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_3223_play_sound_12"]),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3223_pause_0"]),
	SetSyncActionScript(NPC_3, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
	JmpIfBitSet(SHIP_TROOPA_PRIZE, ["EVENT_3223_ret_11"]),
	SetVarToConst(X_COORD_1, 15),
	SetVarToConst(Y_COORD_1, 117),
	SetVarToConst(Z_COORD_1, 15),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1, identifier="EVENT_3223_pause_9"),
	JmpToEvent(E3384_SHIP_TROOPA_PRIZE_PACKET_GRANT),
	Return(identifier="EVENT_3223_ret_11"),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=6, identifier="EVENT_3223_play_sound_12"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_StartLoopNTimes(7),
		A_WalkSouthPixels(2),
		A_WalkNorthPixels(2),
		A_EndLoop()
	]),
	Return()
])
