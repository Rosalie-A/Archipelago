# E1644_MOLEVILLE_OCCUPIED_EXTERIOR_LOADER
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
	FadeOutMusicToVolume(duration=1, volume=127),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_1644_enter_area_7"]),
	JmpIfBitSet(MOLE_DESCENDED, ["EVENT_1644_jmp_6"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=20, y=45, z=24, direction=EAST),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
	Jmp(["EVENT_1644_fade_in_from_black_async_10"], identifier="EVENT_1644_jmp_6"),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTHWEST, x=17, y=44, z=4, identifier="EVENT_1644_enter_area_7"),
	JmpIfBitClear(TEMP_7042_1, ["EVENT_1644_fade_in_from_black_async_10"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=0),
	FadeInFromBlack(sync=False, identifier="EVENT_1644_fade_in_from_black_async_10"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1644_ret_15"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1644_ret_15"]),
	RunEventAsSubroutine(E3897_MOLEVILLE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1644_ret_15")
])
