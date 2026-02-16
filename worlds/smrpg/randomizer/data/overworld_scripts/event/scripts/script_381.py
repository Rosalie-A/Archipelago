# E0381_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_FIGHT
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
	JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_6),
	SetBit(TEMP_7043_5),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=12, y=95),
		A_WalkSoutheastPixels(8),
		A_FaceNorthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_0, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	RememberLastObject(),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_1, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	SetBit(TEMP_7043_5),
	Pause(30),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06`\xff')),
		A_WalkSoutheastPixels(11),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(4),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06`\xff')),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_WalkNorthwestPixels(11),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(4),
		A_BPL262728()
	]),
	RememberLastObject(),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	RemoveObjectFromSpecificLevel(NPC_0, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_1, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	JmpIfObjectNotInSpecificLevel(NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, ["EVENT_381_jmp_if_object_in_level_33"]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectInSpecificLevel(NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_381_jmp_if_object_in_level_33"),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(8)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, mod_id=0),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Walk1StepNortheast(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceEast(),
		A_Pause(30),
		A_FaceSouth()
	]),
	RememberLastObject(),
	Return()
])
