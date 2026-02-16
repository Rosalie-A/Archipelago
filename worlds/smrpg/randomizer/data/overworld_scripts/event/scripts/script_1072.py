# E1072_MELODY_BAY_LOADER
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
	PlayMusicAtDefaultVolume(M0017_TADPOLEPOND),
	DeactivateSoundChannels({0, 1, 2, 3}),
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1072_action_queue_18"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SequenceLoopingOn(),
		A_WalkSouthwestPixels(6)
	]),
	JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1072_clear_bit_14"]),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1072_set_bit_9"]),
	JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1072_clear_bit_14"]),
	JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_1072_set_bit_9"]),
	Jmp(["EVENT_1072_clear_bit_14"]),
	SetBit(TOADOFSKY_REMOVED, identifier="EVENT_1072_set_bit_9"),
	RemoveObjectFromCurrentLevel(NPC_8),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
	FadeInFromBlack(sync=False),
	Return(),
	ClearBit(TOADOFSKY_REMOVED, identifier="EVENT_1072_clear_bit_14"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShiftToXYCoords(x=15, y=27),
		A_WalkSoutheastPixels(6),
		A_WalkSouthwestPixels(6),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW),
		A_FaceSouthwest()
	], identifier="EVENT_1072_action_queue_18"),
	ClearBit(TOADOFSKY_REMOVED),
	DeactivateSoundChannels({0, 1, 2, 3}),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
	FadeInFromBlack(sync=False),
	Return(),
	ClearBit(TEMP_7043_0, identifier="EVENT_1072_clear_bit_24"),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1072_ret_36"]),
	RunEventAsSubroutine(E3893_TADPOLE_POND_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1072_ret_36")
])
