# E1339_PORTRAIT_GAME_ROOM_LOADER
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
	ActionQueueSync(target=NPC_15, subscript=[
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_ShadowOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_WalkNorthwestPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	RunEventAsSubroutine(E0791_TOWER_ANCESTOR_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitSet(PORTRAIT_GAME_COMPLETED, ["EVENT_1339_set_bit_19"]),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=38),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=42),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=46),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=50),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=54),
	FadeInFromBlack(sync=False),
	Return(),
	SetBit(TEMP_7043_0, identifier="EVENT_1339_set_bit_19"),
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7043_2),
	SetBit(TEMP_7043_3),
	SetBit(TEMP_7043_4),
	SetBit(TEMP_7043_5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=36),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=40),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=44),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=52),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=56),
	FadeInFromBlack(sync=False),
	Return()
])
