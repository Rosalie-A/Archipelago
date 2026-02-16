# E0947_FROGFUCIUS_HINT_MAIN_CHECKS
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

script = EventScript([
	RunDialog(dialog_id=DI2730_FROGFUCIUS_OFFER_HINT, above_object=BOWSER, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_991_run_dialog_30"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_jmp_if_bit_clear_5"]),
	JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_947_jmp_if_bit_clear_5"]),
	JmpIfBitSet(BANDITS_WAY_LIBERATED, ["EVENT_991_run_dialog_4"]),
	JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_947_run_event_as_subroutine_7"], identifier="EVENT_947_jmp_if_bit_clear_5"),
	JmpIfBitClear(BANDITS_WAY_LIBERATED, ["EVENT_991_run_dialog_2"]),
	RunEventAsSubroutine(E0989_FROGFUCIUS_HINT_OPTIONAL_9, identifier="EVENT_947_run_event_as_subroutine_7"),
	JmpIfBitClear(SEWER_BOSS_DEFEATED, ["EVENT_991_run_dialog_34"]),
	JmpIfBitClear(MAP_FOREST_MAZE, ["EVENT_947_jmp_if_bit_clear_11"]),
	JmpIfBitClear(FOREST_LIBERATED, ["EVENT_991_run_dialog_36"]),
	JmpIfBitClear(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_947_jmp_if_bit_clear_17"], identifier="EVENT_947_jmp_if_bit_clear_11"),
	JmpIfBitClear(MINES_BOSS_1_DEFEATED, ["EVENT_991_run_dialog_16"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_947_jmp_if_bit_clear_17"]),
	JmpIfBitSet(MINES_BACK_OPENED, ["EVENT_991_run_dialog_16"]),
	StoreItemAmountTo7000(BambinoBombItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_16"]),
	JmpIfBitClear(TOWER_OPENED, ["EVENT_947_jmp_if_bit_set_21"], identifier="EVENT_947_jmp_if_bit_clear_17"),
	JmpIfBitClear(CURTAIN_MINIGAME_COMPLETED, ["EVENT_991_run_dialog_18"]),
	JmpIfObjectInSpecificLevel(NPC_7, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, ["EVENT_991_run_dialog_18"]),
	Jmp(["EVENT_947_jmp_if_bit_set_22"]),
	JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["EVENT_991_run_dialog_18"], identifier="EVENT_947_jmp_if_bit_set_21"),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_947_jmp_if_bit_clear_26"], identifier="EVENT_947_jmp_if_bit_set_22"),
	JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_947_run_event_as_subroutine_25"]),
	RunEventAsSubroutine(E0979_FROGFUCIUS_HINT_OPTIONAL_MARRYMORE),
	RunEventAsSubroutine(E0985_FROGFUCIUS_HINT_OPTIONAL_5, identifier="EVENT_947_run_event_as_subroutine_25"),
	JmpIfBitClear(STAR_HILL_CHECKED, ["EVENT_991_run_dialog_62"], identifier="EVENT_947_jmp_if_bit_clear_26"),
	JmpIfBitClear(MAP_SEA, ["EVENT_947_jmp_if_bit_set_31"]),
	JmpIfBitClear(SHIP_MIDBOSS_COMPLETED, ["EVENT_991_run_dialog_32"]),
	RunEventAsSubroutine(E0988_FROGFUCIUS_HINT_OPTIONAL_8, identifier="EVENT_947_run_event_as_subroutine_29"),
	JmpIfBitClear(SHIP_LIBERATED, ["EVENT_991_run_dialog_32"]),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_947_jmp_if_bit_clear_33"], identifier="EVENT_947_jmp_if_bit_set_31"),
	JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["EVENT_991_run_dialog_20"]),
	JmpIfBitClear(LANDS_END_CLOUD_STAR_PIECE, ["EVENT_991_run_dialog_40"], identifier="EVENT_947_jmp_if_bit_clear_33"),
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_947_jmp_if_bit_clear_36"]),
	JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_991_run_dialog_42"]),
	JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_if_bit_clear_47"], identifier="EVENT_947_jmp_if_bit_clear_36"),
	JmpIfBitClear(DOJO_BOSS_1_DEFEATED, ["EVENT_991_run_dialog_22"]),
	JmpIfBitClear(DOJO_BOSS_2_DEFEATED, ["EVENT_991_run_dialog_22"]),
	JmpIfBitClear(DOJO_BOSS_3_DEFEATED, ["EVENT_991_run_dialog_22"]),
	JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["EVENT_991_run_dialog_22"]),
	JmpIfBitSet(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_947_jmp_if_bit_clear_47"]),
	JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_947_jmp_if_bit_clear_47"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE, ["EVENT_991_run_dialog_22"]),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_22"]),
	RunEventAsSubroutine(E0986_FROGFUCIUS_HINT_OPTIONAL_6),
	JmpIfBitClear(BEAN_VALLEY_BOSS_DEFEATED, ["EVENT_991_run_dialog_24"], identifier="EVENT_947_jmp_if_bit_clear_47"),
	RunEventAsSubroutine(E0987_FROGFUCIUS_HINT_OPTIONAL_7),
	JmpIfObjectInSpecificLevel(NPC_1, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, ["EVENT_991_run_dialog_28"]),
	JmpIfBitClear(STATUE_KEEPER_STAR_PIECE, ["EVENT_991_run_dialog_26"]),
	StoreItemAmountTo7000(CastleKey1Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_28"]),
	JmpIfObjectInSpecificLevel(NPC_10, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_947_jmp_if_bit_clear_59"]),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_991_run_dialog_28"]),
	StoreItemAmountTo7000(CastleKey2Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_28"]),
	JmpIfObjectInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_947_jmp_if_bit_clear_59"]),
	JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_991_run_dialog_28"]),
	JmpIfBitClear(MAP_BARREL_VOLCANO, ["EVENT_947_jmp_if_bit_clear_61"], identifier="EVENT_947_jmp_if_bit_clear_59"),
	JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_991_run_dialog_46"]),
	JmpIfBitClear(MAP_VISTA_HILL, ["EVENT_947_run_event_as_subroutine_66"], identifier="EVENT_947_jmp_if_bit_clear_61"),
	JmpIfBitClear(BATTLE_DOOR_BOSS_BIT, ["EVENT_991_run_dialog_74"]),
	JmpIfBitClear(KEEP_BOSS_3_DEFEATED, ["EVENT_991_run_dialog_48"]),
	JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, ["EVENT_947_run_event_as_subroutine_66"]),
	JmpIfBitClear(INNER_FACTORY_ROOM_4_COMPLETED, ["EVENT_991_run_dialog_50"]),
	RunEventAsSubroutine(E0984_FROGFUCIUS_HINT_OPTIONAL_4, identifier="EVENT_947_run_event_as_subroutine_66"),
	JmpIfObjectNotInSpecificLevel(NPC_1, R189_MARIOS_PIPEHOUSE, ["EVENT_947_jmp_if_bit_clear_69"]),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_jmp_if_bit_clear_74"], identifier="EVENT_947_jmp_if_bit_clear_69"),
	StoreItemAmountTo7000(RareFrogCoinItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_947_jmp_73"]),
	Jmp(["EVENT_947_jmp_if_bit_clear_74"]),
	Jmp(["EVENT_991_run_dialog_4"], identifier="EVENT_947_jmp_73"),
	JmpIfBitClear(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_991_run_dialog_6"], identifier="EVENT_947_jmp_if_bit_clear_74"),
	JmpIfBitClear(SEWERS_FLIPPED_CHEST_OPENED, ["EVENT_991_run_dialog_34"]),
	JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_991_run_dialog_8"]),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_947_jmp_if_object_in_level_81"]),
	JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_991_run_dialog_8"]),
	JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_947_jmp_if_object_in_level_81"]),
	JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_991_run_dialog_8"]),
	JmpIfObjectInSpecificLevel(NPC_13, R084_ROSE_TOWN_OUTSIDE, ["EVENT_991_run_dialog_10"], identifier="EVENT_947_jmp_if_object_in_level_81"),
	JmpIfBitSet(PIPE_VAULT_GATED, ["EVENT_947_run_event_as_subroutine_84"]),
	JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["EVENT_991_run_dialog_12"]),
	RunEventAsSubroutine(E0990_FROGFUCIUS_HINT_OPTIONAL_10, identifier="EVENT_947_run_event_as_subroutine_84"),
	JmpIfBitClear(TOWER_BOSS_2_DEFEATED, ["EVENT_947_jmp_if_bit_clear_88"]),
	JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_947_jmp_if_bit_clear_88"]),
	Jmp(["EVENT_991_run_dialog_18"]),
	JmpIfBitClear(TOWER_OPENED, ["EVENT_947_jmp_if_bit_set_92"], identifier="EVENT_947_jmp_if_bit_clear_88"),
	JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["EVENT_991_run_dialog_18"]),
	JmpIfBitSet(PORTRAIT_GAME_COMPLETED, ["EVENT_947_jmp_if_bit_clear_93"]),
	Jmp(["EVENT_991_run_dialog_18"]),
	JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["EVENT_991_run_dialog_18"], identifier="EVENT_947_jmp_if_bit_set_92"),
	JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_if_object_in_level_96"], identifier="EVENT_947_jmp_if_bit_clear_93"),
	JmpIfObjectInSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["EVENT_991_run_dialog_22"]),
	JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["EVENT_991_run_dialog_22"]),
	JmpIfObjectInSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA, ["EVENT_991_run_dialog_24"], identifier="EVENT_947_jmp_if_object_in_level_96"),
	JmpIfBitClear(RED_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_991_run_dialog_28"]),
	StoreItemAmountTo7000(CastleKey1Item, identifier="EVENT_947_store_item_amount_7000_98"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_28"]),
	JmpIfObjectInSpecificLevel(NPC_10, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["postgame_progress_checker_2"]),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_991_run_dialog_28"]),
	StoreItemAmountTo7000(CastleKey2Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_28"]),
	JmpIfObjectInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["postgame_progress_checker_2"]),
	JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_991_run_dialog_28"]),
	JmpIfObjectInSpecificLevel(NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, ["EVENT_991_run_dialog_26"]),
    JmpIfObjectInSpecificLevel(NPC_3, R189_MARIOS_PIPEHOUSE, ["EVENT_947_jmp_if_bit_clear_911"], identifier="postgame_progress_checker_2"),
    JmpIfBitClear(VOUCHER_CHECK_DONE, ["EVENT_991_run_dialog_0"]),
    StoreItemAmountTo7000(StayVoucherItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_run_dialog_38"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_947_jmp_if_bit_clear_911"]),
	JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["hint_tower_postgame"]),
    JmpIfBitClear(MINES_POSTGAME_COMPLETED, ["EVENT_991_run_dialog_16"]),
    JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["hint_temple_postgame"], identifier="hint_tower_postgame"),
    JmpIfBitClear(POSTGAME_TOWER_COMPLETED, ["EVENT_991_run_dialog_18"]),
	JmpIfObjectInSpecificLevel(NPC_4, R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, ["hint_dojo_postgame"], identifier="hint_temple_postgame"),
    JmpIfBitClear(TEMPLE_POSTGAME_BOSS_DEFEATED, ["EVENT_991_run_dialog_42"]),
    JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["hint_culex_postgame"], identifier="hint_dojo_postgame"),
    JmpIfBitClear(DOJO_POSTGAME_COMPLETED, ["EVENT_991_run_dialog_22"]),
    JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["hint_chapel_postgame"], identifier="hint_culex_postgame"),
    StoreItemAmountTo7000(ExtraShinyStoneItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["hint_chapel_postgame"]),
    JmpIfBitClear(CULEX_POSTGAME_COMPLETED, ["EVENT_991_run_dialog_22"]),
    JmpIfBitClear(MARRYMORE_LIBERATED, ["hint_ship_postgame"], identifier="hint_chapel_postgame"),
    JmpIfBitClear(POSTGAME_CHAPEL_COMPLETE, ["EVENT_991_run_dialog_38"]),
    JmpIfBitClear(SHIP_LIBERATED, ["EVENT_947_jmp_if_bit_clear_911"], identifier="hint_ship_postgame"),
    JmpIfBitClear(POSTGAME_SHIP_COMPLETED, ["EVENT_991_run_dialog_32"]),
    JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_to_event_107"], identifier="EVENT_947_jmp_if_bit_clear_911"),
	JmpIfBitClear(INVISIBLE_FLAG_1_FOUND, ["EVENT_991_run_dialog_INVISIBLE"]),
    JmpIfBitClear(INVISIBLE_FLAG_2_FOUND, ["EVENT_991_run_dialog_INVISIBLE"]),
    JmpIfBitClear(INVISIBLE_FLAG_3_FOUND, ["EVENT_991_run_dialog_INVISIBLE"]),
	JmpToEvent(E0948_FROGFUCIUS_HINT_EXPANSION, identifier="EVENT_947_jmp_to_event_107")
])
