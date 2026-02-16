# E2496_START_GAME
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

from ....spells.spells import *
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
	SummonObjectToSpecificLevel(NPC_0, R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN),
	ApplyTileModToLevel(use_alternate=True, room_id=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=2),
	ApplyTileModToLevel(use_alternate=True, room_id=R226_FOREST_MAZE_AREA_02, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R433_SMITHY_FACTORY_AREA_01_DUMMY, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R442_SMITHY_FACTORY_AREA_11_CONVEYOR_BELTS_SPAWNING_DRILL_BITS_AND_MACKS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 8),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_MARIOS_PAD),
	SetBit(MAP_DIRECTIONAL_MARIOS_PAD_MUSHROOM_WAY),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_WAY_MUSHROOM_KINGDOM),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_KERO_SEWERS),
	SetBit(MAP_DIRECTIONAL_KERO_SEWERS_MIDAS_RIVER),
	SetBit(MAP_DIRECTIONAL_MIDAS_RIVER_TADPOLE_POND),
	SetBit(MAP_DIRECTIONAL_TADPOLE_POND_ROSE_WAY),
	SetBit(MAP_DIRECTIONAL_ROSE_WAY_ROSE_TOWN),
	SetBit(MAP_DIRECTIONAL_ROSE_TOWN_PIPE_VAULT_MOLEVILLE),
	SetBit(MAP_DIRECTIONAL_MOLEVILLE_BOOSTER_PASS),
	SetBit(MAP_DIRECTIONAL_BOOSTER_PASS_BOOSTER_TOWER),
	SetBit(MAP_DIRECTIONAL_BOOSTER_TOWER_BOOSTER_HILL),
	SetBit(MAP_DIRECTIONAL_MARRYMORE_STAR_HILL),
	SetBit(MAP_DIRECTIONAL_STAR_HILL_SEASIDE_TOWN),
	SetBit(MAP_DIRECTIONAL_SEASIDE_TOWN_LANDS_END),
	SetBit(MAP_DIRECTIONAL_LANDS_END_BEAN_VALLEY),
	SetBit(MAP_DIRECTIONAL_BEAN_VALLEY_NIMBUS_LAND),
	SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BOWSERS_KEEP),
	SetBit(MAP_DIRECTIONAL_VISTA_HILL_MARIOS_PAD),
	SetBit(MAP_DIRECTIONAL_BOOSTER_HILL_MARRYMORE),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL),
	SetBit(UNKNOWN_7065_5),
	SetBit(UNKNOWN_7065_6),
	SetBit(UNKNOWN_7065_7),
	SetBit(UNKNOWN_7066_1),
	SetBit(MAP_ROSE_TOWN),
	SetBit(MAP_PIPE_VAULT),
	SetBit(MAP_MOLEVILLE),
	SetBit(MAP_BOOSTER_PASS),
	SetBit(MAP_BOOSTER_TOWER),
	SetBit(MAP_MARRYMORE),
	SetBit(MAP_STAR_HILL),
	SetBit(MAP_SEASIDE_TOWN),
	SetBit(MAP_LANDS_END),
	SetBit(MAP_BEAN_VALLEY),
	SetBit(MAP_NIMBUS_LAND),
	SetBit(MAP_BOOSTER_HILL),
	SetBit(TEMP_7044_6),
	SetBit(TEMP_7049_2),
	SetBit(PROGRESSIVE_FIREWORKS_ENABLED),
	SetBit(UNKNOWN_ROSE_TOWN_7060_7),
	SetBit(MAP_MENU_UNLOCKED),
	SetBit(MARRYMORE_UNKNOWN_7063_2),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	AddToInventory(WasteBasketItem),
	RestoreAllHP(),
	RestoreAllFP(),
	ClearBit(EXP_STAR_BIT_1),
	ClearBit(EXP_STAR_BIT_2),
	ClearBit(EXP_STAR_BIT_3),
	ClearBit(EXP_STAR_BIT_4),
	SetVarToConst(COIN_COUNTER_1, 0),
	SetVarToConst(COIN_COUNTER_2, 0),
	SetVarToConst(COIN_COUNTER_3, 0),
	SetVarToConst(COIN_COUNTER_4, 0),
	SetVarToConst(COIN_COUNTER_5, 0),
	SetVarToConst(COIN_COUNTER_6, 0),
	StopMusicFDA2(),
	SetBit(GARRO_SEQUENCE_COMPLETED),
	ClearBit(PROGRESSIVE_STAR_EXP_ENABLED),
	ApplyTileModToLevel(use_alternate=True, room_id=R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, mod_id=0),
	ClearBit(UNKNOWN_STAR_PIECE),
	SetBit(UNKNOWN_7053_0),
	SetBit(MAP_MARIOS_PAD),
	SetBit(MAP_MUSHROOM_WAY),
	SetBit(MAP_MUSHROOM_KINGDOM),
	ClearBit(MINES_HENCHMAN_LEFT_DEFEATED),
	ClearBit(MINES_HENCHMAN_RIGHT_DEFEATED),
	CharacterJoinsParty(DUMMY_0X05),
	CharacterLeavesParty(MARIO),
	RunEventAsSubroutine(E1220_STARTING_CHARACTER_1),
	CharacterLeavesParty(DUMMY_0X05),
	RunEventAsSubroutine(E1221_STARTING_CHARACTER_2),
	RunEventAsSubroutine(E1222_STARTING_CHARACTER_3),
	RunEventAsSubroutine(E1223_STARTING_CHARACTER_4),
	RunEventAsSubroutine(E1224_STARTING_CHARACTER_5),
    RunEventAsSubroutine(E3840_STARTER_DEBUG_ITEMS),
    RunEventAsSubroutine(E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsLesser(["EVENT_2496_j"]),
	SetBit(SWITCH_MENU_UNLOCKED),
	EnterArea(room_id=R189_MARIOS_PIPEHOUSE, face_direction=SOUTHEAST, x=3, y=13, z=0, identifier="EVENT_2496_j"),
	JmpToEvent(E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING)
])
