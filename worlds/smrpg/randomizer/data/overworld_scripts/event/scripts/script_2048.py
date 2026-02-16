# E2048_MONSTRO_TOWN_EXTERIOR_LOADER
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
	JmpIfBitSet(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, ["EVENT_2048_set_bit_6"], identifier="EVENT_2048_set_bit_0"),
	CopyVarToVar(from_var=MONSTRO_THWOMP_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2048_jmp_if_bit_clear_8"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_LoadMemory(PRIMARY_TEMP_7000),
		A_WalkSouthwestPixels(2),
		A_EndLoop()
	]),
	Jmp(["EVENT_2048_jmp_if_bit_clear_8"]),
	SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, identifier="EVENT_2048_set_bit_6"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=11, y=62, z=8, direction=EAST)
	]),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2048_fade_in_from_black_async_12"], identifier="EVENT_2048_jmp_if_bit_clear_8"),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	RunEventAsSubroutine(E2079_MONSTRO_TOWN_EXTERIOR_LOADER_FROM_SAVE_BOX),
	Jmp(["EVENT_2048_jmp_if_bit_clear_13"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2048_fade_in_from_black_async_12"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2048_jmp_to_event_18"], identifier="EVENT_2048_jmp_if_bit_clear_13"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2048_jmp_to_event_18"]),
	RunEventAsSubroutine(E3909_MONSTRO_STAR_PIECE_SIGNAL),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT, ["attempt_postgame_door_starpiece"]),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER, identifier="EVENT_2048_jmp_to_event_18"),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT_2, ["EVENT_2048_ret_19"], identifier="attempt_postgame_door_starpiece"),
    SetVarToConst(PRIMARY_TEMP_7000, 524),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2048_ret_19")
])
