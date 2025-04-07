from typing import Dict, Any

from .Options import *

minsanity = {
    "goal": Goal.option_chaos_chao,
    "max_emblem_cap": MaximumEmblemCap.range_start,

    "keysanity": False,
    "whistlesanity": Whistlesanity.option_none,
    "beetlesanity": False,
    "omosanity": False,
    "animalsanity": False,
    "itemboxsanity": ItemBoxsanity.option_none,
    "bigsanity": False,
    "kart_race_checks": KartRaceChecks.option_none,

    "junk_fill_percentage": 0,

    "sonic_mission_count": BaseMissionCount.range_start,
    "sonic_mission_2": False,
    "sonic_mission_3": False,
    "sonic_mission_4": False,
    "sonic_mission_5": False,

    "shadow_mission_count": BaseMissionCount.range_start,
    "shadow_mission_2": False,
    "shadow_mission_3": False,
    "shadow_mission_4": False,
    "shadow_mission_5": False,

    "tails_mission_count": BaseMissionCount.range_start,
    "tails_mission_2": False,
    "tails_mission_3": False,
    "tails_mission_4": False,
    "tails_mission_5": False,

    "eggman_mission_count": BaseMissionCount.range_start,
    "eggman_mission_2": False,
    "eggman_mission_3": False,
    "eggman_mission_4": False,
    "eggman_mission_5": False,

    "knuckles_mission_count": BaseMissionCount.range_start,
    "knuckles_mission_2": False,
    "knuckles_mission_3": False,
    "knuckles_mission_4": False,
    "knuckles_mission_5": False,

    "rouge_mission_count": BaseMissionCount.range_start,
    "rouge_mission_2": False,
    "rouge_mission_3": False,
    "rouge_mission_4": False,
    "rouge_mission_5": False,

    "kart_mission_count": BaseMissionCount.range_start,
    "kart_mission_2": False,
    "kart_mission_3": False,
    "kart_mission_4": False,
    "kart_mission_5": False,

    "cannons_core_mission_count": BaseMissionCount.range_start,
    "cannons_core_mission_2": False,
    "cannons_core_mission_3": False,
    "cannons_core_mission_4": False,
    "cannons_core_mission_5": False,
}

chao_centric = {
    "goal": Goal.option_chaos_chao,

    "keysanity": False,
    "whistlesanity": Whistlesanity.option_none,
    "beetlesanity": False,
    "omosanity": False,
    "animalsanity": False,
    "itemboxsanity": ItemBoxsanity.option_none,
    "bigsanity": False,
    "kart_race_checks": KartRaceChecks.option_none,

    "black_market_slots": BlackMarketSlots.range_end,
    "black_market_unlock_costs": BlackMarketUnlockCosts.option_high,
    "chao_race_difficulty": ChaoRaceDifficulty.option_expert,
    "chao_karate_difficulty": ChaoKarateDifficulty.option_super,
    "chao_stadium_checks": ChaoStadiumChecks.option_all,
    "chao_animal_parts": True,
    "chao_stats": ChaoStats.range_end,
    "chao_stats_frequency": 1,
    "chao_stats_stamina": True,
    "chao_stats_hidden": True,
    "chao_kindergarten": ChaoKindergarten.option_full,

    "junk_fill_percentage": 50,

    "sonic_mission_count": BaseMissionCount.range_start,
    "sonic_mission_2": False,
    "sonic_mission_3": False,
    "sonic_mission_4": False,
    "sonic_mission_5": False,

    "shadow_mission_count": BaseMissionCount.range_start,
    "shadow_mission_2": False,
    "shadow_mission_3": False,
    "shadow_mission_4": False,
    "shadow_mission_5": False,

    "tails_mission_count": BaseMissionCount.range_start,
    "tails_mission_2": False,
    "tails_mission_3": False,
    "tails_mission_4": False,
    "tails_mission_5": False,

    "eggman_mission_count": BaseMissionCount.range_start,
    "eggman_mission_2": False,
    "eggman_mission_3": False,
    "eggman_mission_4": False,
    "eggman_mission_5": False,

    "knuckles_mission_count": BaseMissionCount.range_start,
    "knuckles_mission_2": False,
    "knuckles_mission_3": False,
    "knuckles_mission_4": False,
    "knuckles_mission_5": False,

    "rouge_mission_count": BaseMissionCount.range_start,
    "rouge_mission_2": False,
    "rouge_mission_3": False,
    "rouge_mission_4": False,
    "rouge_mission_5": False,

    "kart_mission_count": BaseMissionCount.range_start,
    "kart_mission_2": False,
    "kart_mission_3": False,
    "kart_mission_4": False,
    "kart_mission_5": False,

    "cannons_core_mission_count": BaseMissionCount.range_start,
    "cannons_core_mission_2": False,
    "cannons_core_mission_3": False,
    "cannons_core_mission_4": False,
    "cannons_core_mission_5": False,
}

allsanity_no_chao = {
    "goal": Goal.option_cannons_core_boss_rush,
    "boss_rush_shuffle": BossRushShuffle.option_chaos,
    "minigame_madness_requirement": MinigameMadnessRequirement.range_end,
    "minigame_madness_minimum": MinigameMadnessMinimum.range_end,
    "max_emblem_cap": MaximumEmblemCap.range_end,

    "mission_shuffle": True,
    "required_cannons_core_missions": RequiredCannonsCoreMissions.option_all_active,
    "emblem_percentage_for_cannons_core": EmblemPercentageForCannonsCore.range_end,
    "number_of_level_gates": NumberOfLevelGates.range_end,
    "level_gate_costs": LevelGateCosts.option_high,

    "keysanity": True,
    "whistlesanity": Whistlesanity.option_both,
    "beetlesanity": True,
    "omosanity": True,
    "animalsanity": True,
    "itemboxsanity": ItemBoxsanity.option_all,
    "bigsanity": True,
    "kart_race_checks": KartRaceChecks.option_full,

    "junk_fill_percentage": 25,
    "trap_fill_percentage": 25,
    "omochao_trap_weight": BaseTrapWeight.option_high,
    "timestop_trap_weight": BaseTrapWeight.option_high,
    "confusion_trap_weight": BaseTrapWeight.option_high,
    "tiny_trap_weight": BaseTrapWeight.option_high,
    "gravity_trap_weight": BaseTrapWeight.option_high,
    "exposition_trap_weight": BaseTrapWeight.option_high,
    "ice_trap_weight": BaseTrapWeight.option_high,
    "slow_trap_weight": BaseTrapWeight.option_high,
    "cutscene_trap_weight": BaseTrapWeight.option_high,
    "reverse_trap_weight": BaseTrapWeight.option_high,
    "literature_trap_weight": BaseTrapWeight.option_high,
    "controller_drift_trap_weight": BaseTrapWeight.option_high,
    "poison_trap_weight": BaseTrapWeight.option_high,
    "bee_trap_weight": BaseTrapWeight.option_high,
    "pong_trap_weight": BaseTrapWeight.option_high,
    "breakout_trap_weight": BaseTrapWeight.option_high,
    "fishing_trap_weight": BaseTrapWeight.option_high,
    "trivia_trap_weight": BaseTrapWeight.option_high,
    "pokemon_trivia_trap_weight": BaseTrapWeight.option_high,
    "pokemon_count_trap_weight": BaseTrapWeight.option_high,
    "number_sequence_trap_weight": BaseTrapWeight.option_high,
    "light_up_path_trap_weight": BaseTrapWeight.option_high,
    "pinball_trap_weight": BaseTrapWeight.option_high,
    "math_quiz_trap_weight": BaseTrapWeight.option_high,
    "snake_trap_weight": BaseTrapWeight.option_high,
    "input_sequence_trap_weight": BaseTrapWeight.option_high,
    "minigame_trap_difficulty": MinigameTrapDifficulty.option_chaos,
    "big_fishing_difficulty": BigFishingDifficulty.option_chaos,

    "music_shuffle": MusicShuffle.option_full,
    "voice_shuffle": VoiceShuffle.option_shuffled,

    "sonic_mission_count": BaseMissionCount.range_end,
    "sonic_mission_2": True,
    "sonic_mission_3": True,
    "sonic_mission_4": True,
    "sonic_mission_5": True,

    "shadow_mission_count": BaseMissionCount.range_end,
    "shadow_mission_2": True,
    "shadow_mission_3": True,
    "shadow_mission_4": True,
    "shadow_mission_5": True,

    "tails_mission_count": BaseMissionCount.range_end,
    "tails_mission_2": True,
    "tails_mission_3": True,
    "tails_mission_4": True,
    "tails_mission_5": True,

    "eggman_mission_count": BaseMissionCount.range_end,
    "eggman_mission_2": True,
    "eggman_mission_3": True,
    "eggman_mission_4": True,
    "eggman_mission_5": True,

    "knuckles_mission_count": BaseMissionCount.range_end,
    "knuckles_mission_2": True,
    "knuckles_mission_3": True,
    "knuckles_mission_4": True,
    "knuckles_mission_5": True,

    "rouge_mission_count": BaseMissionCount.range_end,
    "rouge_mission_2": True,
    "rouge_mission_3": True,
    "rouge_mission_4": True,
    "rouge_mission_5": True,

    "kart_mission_count": BaseMissionCount.range_end,
    "kart_mission_2": True,
    "kart_mission_3": True,
    "kart_mission_4": True,
    "kart_mission_5": True,

    "cannons_core_mission_count": BaseMissionCount.range_end,
    "cannons_core_mission_2": True,
    "cannons_core_mission_3": True,
    "cannons_core_mission_4": True,
    "cannons_core_mission_5": True,
}

allsanity = {
    "goal": Goal.option_cannons_core_boss_rush,
    "boss_rush_shuffle": BossRushShuffle.option_chaos,
    "minigame_madness_requirement": MinigameMadnessRequirement.range_end,
    "minigame_madness_minimum": MinigameMadnessMinimum.range_end,
    "max_emblem_cap": MaximumEmblemCap.range_end,

    "mission_shuffle": True,
    "required_cannons_core_missions": RequiredCannonsCoreMissions.option_all_active,
    "emblem_percentage_for_cannons_core": EmblemPercentageForCannonsCore.range_end,
    "number_of_level_gates": NumberOfLevelGates.range_end,
    "level_gate_costs": LevelGateCosts.option_high,

    "keysanity": True,
    "whistlesanity": Whistlesanity.option_both,
    "beetlesanity": True,
    "omosanity": True,
    "animalsanity": True,
    "itemboxsanity": ItemBoxsanity.option_all,
    "bigsanity": True,
    "kart_race_checks": KartRaceChecks.option_full,

    "black_market_slots": BlackMarketSlots.range_end,
    "black_market_unlock_costs": BlackMarketUnlockCosts.option_high,
    "chao_race_difficulty": ChaoRaceDifficulty.option_expert,
    "chao_karate_difficulty": ChaoKarateDifficulty.option_super,
    "chao_stadium_checks": ChaoStadiumChecks.option_all,
    "chao_animal_parts": True,
    "chao_stats": ChaoStats.range_end,
    "chao_stats_frequency": 1,
    "chao_stats_stamina": True,
    "chao_stats_hidden": True,
    "chao_kindergarten": ChaoKindergarten.option_full,

    "junk_fill_percentage": 25,
    "trap_fill_percentage": 25,
    "omochao_trap_weight": BaseTrapWeight.option_high,
    "timestop_trap_weight": BaseTrapWeight.option_high,
    "confusion_trap_weight": BaseTrapWeight.option_high,
    "tiny_trap_weight": BaseTrapWeight.option_high,
    "gravity_trap_weight": BaseTrapWeight.option_high,
    "exposition_trap_weight": BaseTrapWeight.option_high,
    "ice_trap_weight": BaseTrapWeight.option_high,
    "slow_trap_weight": BaseTrapWeight.option_high,
    "cutscene_trap_weight": BaseTrapWeight.option_high,
    "reverse_trap_weight": BaseTrapWeight.option_high,
    "literature_trap_weight": BaseTrapWeight.option_high,
    "controller_drift_trap_weight": BaseTrapWeight.option_high,
    "poison_trap_weight": BaseTrapWeight.option_high,
    "bee_trap_weight": BaseTrapWeight.option_high,
    "pong_trap_weight": BaseTrapWeight.option_high,
    "breakout_trap_weight": BaseTrapWeight.option_high,
    "fishing_trap_weight": BaseTrapWeight.option_high,
    "trivia_trap_weight": BaseTrapWeight.option_high,
    "pokemon_trivia_trap_weight": BaseTrapWeight.option_high,
    "pokemon_count_trap_weight": BaseTrapWeight.option_high,
    "number_sequence_trap_weight": BaseTrapWeight.option_high,
    "light_up_path_trap_weight": BaseTrapWeight.option_high,
    "pinball_trap_weight": BaseTrapWeight.option_high,
    "math_quiz_trap_weight": BaseTrapWeight.option_high,
    "snake_trap_weight": BaseTrapWeight.option_high,
    "input_sequence_trap_weight": BaseTrapWeight.option_high,
    "minigame_trap_difficulty": MinigameTrapDifficulty.option_chaos,
    "big_fishing_difficulty": BigFishingDifficulty.option_chaos,

    "music_shuffle": MusicShuffle.option_full,
    "voice_shuffle": VoiceShuffle.option_shuffled,

    "sonic_mission_count": BaseMissionCount.range_end,
    "sonic_mission_2": True,
    "sonic_mission_3": True,
    "sonic_mission_4": True,
    "sonic_mission_5": True,

    "shadow_mission_count": BaseMissionCount.range_end,
    "shadow_mission_2": True,
    "shadow_mission_3": True,
    "shadow_mission_4": True,
    "shadow_mission_5": True,

    "tails_mission_count": BaseMissionCount.range_end,
    "tails_mission_2": True,
    "tails_mission_3": True,
    "tails_mission_4": True,
    "tails_mission_5": True,

    "eggman_mission_count": BaseMissionCount.range_end,
    "eggman_mission_2": True,
    "eggman_mission_3": True,
    "eggman_mission_4": True,
    "eggman_mission_5": True,

    "knuckles_mission_count": BaseMissionCount.range_end,
    "knuckles_mission_2": True,
    "knuckles_mission_3": True,
    "knuckles_mission_4": True,
    "knuckles_mission_5": True,

    "rouge_mission_count": BaseMissionCount.range_end,
    "rouge_mission_2": True,
    "rouge_mission_3": True,
    "rouge_mission_4": True,
    "rouge_mission_5": True,

    "kart_mission_count": BaseMissionCount.range_end,
    "kart_mission_2": True,
    "kart_mission_3": True,
    "kart_mission_4": True,
    "kart_mission_5": True,

    "cannons_core_mission_count": BaseMissionCount.range_end,
    "cannons_core_mission_2": True,
    "cannons_core_mission_3": True,
    "cannons_core_mission_4": True,
    "cannons_core_mission_5": True,
}

all_random = {
    "goal": "random",
    "boss_rush_shuffle": "random",
    "minigame_madness_requirement": "random",
    "minigame_madness_minimum": "random",
    "logic_difficulty": "random",
    "required_rank": "random",
    "max_emblem_cap": "random",
    "ring_loss": "random",

    "mission_shuffle": "random",
    "required_cannons_core_missions": "random",
    "emblem_percentage_for_cannons_core": "random",
    "number_of_level_gates": "random",
    "level_gate_distribution": "random",
    "level_gate_costs": "random",

    "keysanity": "random",
    "whistlesanity": "random",
    "beetlesanity": "random",
    "omosanity": "random",
    "animalsanity": "random",
    "itemboxsanity": "random",
    "bigsanity": "random",
    "kart_race_checks": "random",

    "black_market_slots": "random",
    "black_market_unlock_costs": "random",
    "black_market_price_multiplier": "random",
    "chao_race_difficulty": "random",
    "chao_karate_difficulty": "random",
    "chao_stadium_checks": "random",
    "chao_animal_parts": "random",
    "chao_stats": "random",
    "chao_stats_frequency": "random",
    "chao_stats_stamina": "random",
    "chao_stats_hidden": "random",
    "chao_kindergarten": "random",
    "shuffle_starting_chao_eggs": "random",
    "chao_entrance_randomization": "random",

    "junk_fill_percentage": "random",
    "trap_fill_percentage": "random",
    "omochao_trap_weight": "random",
    "timestop_trap_weight": "random",
    "confusion_trap_weight": "random",
    "tiny_trap_weight": "random",
    "gravity_trap_weight": "random",
    "exposition_trap_weight": "random",
    "ice_trap_weight": "random",
    "slow_trap_weight": "random",
    "cutscene_trap_weight": "random",
    "reverse_trap_weight": "random",
    "literature_trap_weight": "random",
    "controller_drift_trap_weight": "random",
    "poison_trap_weight": "random",
    "bee_trap_weight": "random",
    "pong_trap_weight": "random",
    "breakout_trap_weight": "random",
    "fishing_trap_weight": "random",
    "trivia_trap_weight": "random",
    "pokemon_trivia_trap_weight": "random",
    "pokemon_count_trap_weight": "random",
    "number_sequence_trap_weight": "random",
    "light_up_path_trap_weight": "random",
    "pinball_trap_weight": "random",
    "math_quiz_trap_weight": "random",
    "snake_trap_weight": "random",
    "input_sequence_trap_weight": "random",
    "minigame_trap_difficulty": "random",
    "big_fishing_difficulty": "random",

    "sadx_music": "random",
    "music_shuffle": "random",
    "voice_shuffle": "random",
    "narrator": "random",

    "sonic_mission_count": "random",
    "sonic_mission_2": "random",
    "sonic_mission_3": "random",
    "sonic_mission_4": "random",
    "sonic_mission_5": "random",

    "shadow_mission_count": "random",
    "shadow_mission_2": "random",
    "shadow_mission_3": "random",
    "shadow_mission_4": "random",
    "shadow_mission_5": "random",

    "tails_mission_count": "random",
    "tails_mission_2": "random",
    "tails_mission_3": "random",
    "tails_mission_4": "random",
    "tails_mission_5": "random",

    "eggman_mission_count": "random",
    "eggman_mission_2": "random",
    "eggman_mission_3": "random",
    "eggman_mission_4": "random",
    "eggman_mission_5": "random",

    "knuckles_mission_count": "random",
    "knuckles_mission_2": "random",
    "knuckles_mission_3": "random",
    "knuckles_mission_4": "random",
    "knuckles_mission_5": "random",

    "rouge_mission_count": "random",
    "rouge_mission_2": "random",
    "rouge_mission_3": "random",
    "rouge_mission_4": "random",
    "rouge_mission_5": "random",

    "kart_mission_count": "random",
    "kart_mission_2": "random",
    "kart_mission_3": "random",
    "kart_mission_4": "random",
    "kart_mission_5": "random",

    "cannons_core_mission_count": "random",
    "cannons_core_mission_2": "random",
    "cannons_core_mission_3": "random",
    "cannons_core_mission_4": "random",
    "cannons_core_mission_5": "random",

    "ring_link": "random",
    "trap_link": "random",
    "death_link": "random",
}

sa2b_options_presets: Dict[str, Dict[str, Any]] = {
    "Minsanity": minsanity,
    "Chao-centric": chao_centric,
    "Allsanity No Chao": allsanity_no_chao,
    "Allsanity": allsanity,
    "All Random": all_random,
}
