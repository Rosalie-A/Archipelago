# E1688_TEMPLE_FORTUNE_HEADS_ROOM_LOADER
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
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1688_remove_from_level_6"]),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1688_remove_from_level_6"]),
	JmpIfBitSet(BELOME_FORTUNE_1, ["EVENT_1688_remove_from_level_6"]),
	SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
	Jmp(["EVENT_1688_mem_7000_and_const_7"]),
	RemoveObjectFromSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, identifier="EVENT_1688_remove_from_level_6"),
	Mem7000AndConst(0x0003, identifier="EVENT_1688_mem_7000_and_const_7"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000C),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AllBitsClear(bits=[4], destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_16"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=32),
	SetBit(BELOME_HEAD_1),
	JmpIf7000AllBitsClear(bits=[5], destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_19"], identifier="EVENT_1688_jmp_if_7000_all_bits_clear_16"),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=33),
	SetBit(BELOME_HEAD_2),
	JmpIf7000AllBitsClear(bits=[6], destinations=["EVENT_1688_jmp_if_bit_clear_22"], identifier="EVENT_1688_jmp_if_7000_all_bits_clear_19"),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=34),
	SetBit(BELOME_HEAD_3),
	JmpIfBitClear(UNKNOWN_BELOME_FORTUNE, ["EVENT_1688_jmp_to_event_27"], identifier="EVENT_1688_jmp_if_bit_clear_22"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1688_action_queue_23_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1688_action_queue_23_SUBSCRIPT_pause_8"]),
		A_WalkNorthPixels(8)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1688_action_queue_24_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_1688_action_queue_24_SUBSCRIPT_pause_8"]),
		A_WalkNorthPixels(8)
	]),
	JmpIfBitClear(UNKNOWN_BELOME_TEMPLE, ["EVENT_1688_jmp_to_event_27"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_IncPaletteRowBy(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(10)
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1688_jmp_to_event_27")
])
