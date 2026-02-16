# E1359_CURTAIN_GAME_ROOM_LOADER
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
	SetVarToConst(TEMP_7026, 0),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthPixels(22),
		A_WalkEastPixels(7),
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(5),
		A_WalkNorthwestPixels(4),
		A_FaceSoutheast(),
		A_SetPriority(3),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_WalkEastPixels(8),
		A_WalkNorthPixels(8)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=2),
	JmpIfBitSet(FAST_TRAVEL_ENABLED, ["EVENT_1359_jmp_if_bit_set_12"]),
	JmpIfBitClear(TOWER_BOSS_2_DEFEATED, ["EVENT_1359_jmp_if_bit_set_12"]),
	SummonObjectToCurrentLevel(NPC_8),
	SummonObjectToCurrentLevel(NPC_9),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkWestPixels(8),
		A_WalkSouthPixels(8)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_WalkWestPixels(8),
		A_WalkSouthPixels(8)
	]),
	JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_1359_apply_tile_mod_17"], identifier="EVENT_1359_jmp_if_bit_set_12"),
	JmpIfBitSet(TOWER_BOSS_1_DEFEATED, ["EVENT_1359_apply_solidity_mod_28"]),
	RunEventAsSubroutine(E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=35, identifier="EVENT_1359_apply_tile_mod_17"),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=43),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=47),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=3, y=21, z=0, direction=EAST)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=1),
	JmpIfBitClear(UNKNOWN_7054_4, ["EVENT_1359_fade_in_from_black_async_26"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=33),
	Jmp(["EVENT_1359_fade_in_from_black_async_26"]),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=2, identifier="EVENT_1359_apply_solidity_mod_28"),
	RunEventAsSubroutine(E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_1359_fade_in_from_black_async_26"),
    JmpIfBitSet(POSTGAME_TOWER_COMPLETED, ["curtain_room_end"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["curtain_room_end"]),
    SummonObjectToCurrentLevel(NPC_10),
	FadeInFromBlack(sync=False, identifier="curtain_room_end"),
	Return()
])
