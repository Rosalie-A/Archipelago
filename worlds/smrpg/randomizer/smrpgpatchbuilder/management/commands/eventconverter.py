from django.core.management.base import BaseCommand
import sys, os, shutil

from smrpgpatchbuilder.utils.disassembler_common import (
    writeline,
)
from .legacy.eventdisassembler import Command as EventDisassemblerCommand
from .legacy.objectsequencedisassembler import Command as AnimationDisassemblerCommand

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *

from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config, load_flags_from_input_files, load_variables_from_input_files

DIRECTIONS = [
    "EAST",
    "SOUTHEAST",
    "SOUTH",
    "SOUTHWEST",
    "WEST",
    "NORTHWEST",
    "NORTH",
    "NORTHEAST",
]

AREA_OBJECTS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "DUMMY_0X05",
    "DUMMY_0X06",
    "DUMMY_0X07",
    "CHARACTER_IN_SLOT_1",
    "CHARACTER_IN_SLOT_2",
    "CHARACTER_IN_SLOT_3",
    "DUMMY_0X0B",
    "SCREEN_FOCUS",
    "LAYER_1",
    "LAYER_2",
    "LAYER_3",
    "MEM_70A8",
    "MEM_70A9",
    "MEM_70AA",
    "MEM_70AB",
    "NPC_0",
    "NPC_1",
    "NPC_2",
    "NPC_3",
    "NPC_4",
    "NPC_5",
    "NPC_6",
    "NPC_7",
    "NPC_8",
    "NPC_9",
    "NPC_10",
    "NPC_11",
    "NPC_12",
    "NPC_13",
    "NPC_14",
    "NPC_15",
    "NPC_16",
    "NPC_17",
    "NPC_18",
    "NPC_19",
    "NPC_20",
    "NPC_21",
    "NPC_22",
    "NPC_23",
    "NPC_24",
    "NPC_25",
    "NPC_26",
    "NPC_27",
]

INTRO_TEXT = [
    "SUPER_MARIO",
    "PRINCESS_TOADSTOOL",
    "KING_BOWSER",
    "MALLOW",
    "GENO",
    "IN",
]

CONTROLLER_INPUTS = ["LEFT", "RIGHT", "DOWN", "UP", "X", "A", "Y", "B"]

COLOURS = ["BLACK", "BLUE", "RED", "PINK", "GREEN", "AQUA", "YELLOW", "WHITE"]

PALETTE_TYPES = [
    "NOTHING",
    None,
    None,
    None,
    None,
    None,
    "GLOW",
    None,
    None,
    None,
    None,
    None,
    "SET_TO",
    None,
    "FADE_TO",
]

SCRIPT_TYPE_EVENT = "event"
SCRIPT_TYPE_ACTION = "action"

LAYER_TYPES = [
    "LAYER_L1",
    "LAYER_L2",
    "LAYER_L3",
    "LAYER_L4",
    "NPC_SPRITES",
    "BACKGROUND",
    "HALF_INTENSITY",
    "MINUS_SUB",
]

TUTORIALS = [
    "TU00_HOW_TO_EQUIP",
    "TU01_HOW_TO_USE_ITEMS",
    "TU02_HOW_TO_SWITCH",
    "TU02_HOW_TO_PLAY_BEETLEMANIA"
]

SCENES = [
    "SC00_OPEN_GAME_SELECT_MENU",
    "SC01_OPEN_OVERWORLD_MENU",
    "SC02_OPEN_LOCATION",
    "SC03_OPEN_SHOP_MENU",
    "SC04_OPEN_SAVE_GAME_MENU",
    "SC05_OPEN_ITEMS_MAXED_OUT_MENU",
    "SC06_UNKNOWN",
    "SC07_RUN_MENU_TUTORIAL",
    "SC08_ADD_STAR_PIECE",
    "SC09_RUN_MOLEVILLE_MOUNTAIN",
    "SC10_UNKNOWN",
    "SC11_RUN_MOLEVILLE_MOUNTAIN_INTRO",
    "SC12_UNKNOWN",
    "SC13_RUN_STAR_PIECE_END_SEQUENCE",
    "SC14_RUN_GARDEN_INTRO_SEQUENCE",
    "SC15_ENTER_GATE_TO_SMITHY_FACTORY",
    "SC16_RUN_WORLD_MAP_EVENT_SEQUENCE",
]

sys.stdout.reconfigure(encoding="utf-8")

searchable_vars = globals()

actions_jumped_to = []
events_jumped_to = []

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):
        varnames = load_arrays_from_input_files()
        classnames = load_class_names_from_config()
        vars_lookup = load_variables_from_input_files()
        flags_lookup = load_flags_from_input_files()

        def convert_event_script_command(cmd, valid_identifiers):
            use_identifier: bool = cmd["identifier"] in valid_identifiers
            args = {}
            cls = None
            cmdargs = []
            include_argnames = True

            if "args" in cmd:
                cmdargs = cmd["args"]

            if cmd["command"] in [
                "action_queue",
                "start_embedded_action_script",
                "non_embedded_action_queue",
            ]:
                contents = convert_script(
                    cmd["subscript"], valid_identifiers, convert_action_script_command
                )
                contents = ",\n\t\t".join(contents)
                contents = "[\n\t\t%s\n\t]" % contents
                if cmd["command"] == "action_queue":
                    if cmdargs[1]:
                        cls = "ActionQueueAsync"
                    else:
                        cls = "ActionQueueSync"  # why did i have these backwards lol
                    args["target"] = AREA_OBJECTS[cmdargs[0]]
                elif cmd["command"] == "start_embedded_action_script":
                    if cmdargs[1]:
                        cls = "StartAsyncEmbeddedActionScript"
                    else:
                        cls = "StartSyncEmbeddedActionScript"
                    args["target"] = AREA_OBJECTS[cmdargs[0]]
                    args["prefix"] = f"0x{cmdargs[2]:02X}"
                elif cmd["command"] == "non_embedded_action_queue":
                    cls = "NonEmbeddedActionQueue"
                    args["required_offset"] = f"0x{cmd["internal_offset"]:02X}"
                args["subscript"] = contents
            elif cmd["command"] in ["set_action_script", "set_temp_action_script"]:
                if cmd["command"] == "set_action_script":
                    if cmdargs[1]:
                        cls = "SetSyncActionScript"
                    else:
                        cls = "SetAsyncActionScript"
                elif cmd["command"] == "set_temp_action_script":
                    if cmdargs[1]:
                        cls = "SetTempSyncActionScript"
                    else:
                        cls = "SetTempAsyncActionScript"
                include_argnames = False
                args["target"] = AREA_OBJECTS[cmdargs[0]]
                args["action_script_id"] = varnames["action_scripts"][cmdargs[2]]
            elif cmd["command"] in [
                "unsync_action_script",
                "summon_to_current_level_at_marios_coords",
                "summon_to_current_level",
                "remove_from_current_level",
                "pause_action_script",
                "resume_action_script",
                "enable_trigger",
                "disable_trigger",
                "stop_embedded_action_script",
                "reset_coords",
            ]:
                include_argnames = False
                if cmd["command"] == "unsync_action_script":
                    cls = "UnsyncActionScript"
                elif cmd["command"] == "summon_to_current_level_at_marios_coords":
                    cls = "SummonObjectToCurrentLevelAtMariosCoords"
                elif cmd["command"] == "summon_to_current_level":
                    cls = "SummonObjectToCurrentLevel"
                elif cmd["command"] == "remove_from_current_level":
                    cls = "RemoveObjectFromCurrentLevel"
                elif cmd["command"] == "pause_action_script":
                    cls = "PauseActionScript"
                elif cmd["command"] == "resume_action_script":
                    cls = "ResumeActionScript"
                elif cmd["command"] == "enable_trigger":
                    cls = "EnableObjectTrigger"
                elif cmd["command"] == "disable_trigger":
                    cls = "DisableObjectTrigger"
                elif cmd["command"] == "stop_embedded_action_script":
                    cls = "StopEmbeddedActionScript"
                elif cmd["command"] == "reset_coords":
                    cls = "ResetCoords"
                args["target"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "add_const_to_var":
                cls = "AddConstToVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["value"] = str(cmdargs[1])
            elif cmd["command"] == "inc":
                cls = "Inc"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "add_coins" or cmd["command"] == "add_frog_coins":
                if cmd["command"] == "add_coins":
                    cls = "AddCoins"
                elif cmd["command"] == "add_frog_coins":
                    cls = "AddFrogCoins"
                include_argnames = False
                if cmdargs[0] == 0x7000:
                    args["amount"] = vars_lookup.get(cmdargs[0])
                else:
                    args["amount"] = str(cmdargs[0])
            elif cmd["command"] == "add_7000_to_current_FP":
                cls = "Add7000ToCurrentFP"
            elif cmd["command"] == "add_7000_to_max_FP":
                cls = "Add7000ToMaxFP"
            elif cmd["command"] == "add_var_to_7000":
                cls = "AddVarTo7000"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "adjust_music_tempo":
                args["duration"] = str(cmdargs[2])
                if cmdargs[1] >= 0x80:
                    cls = "SpeedUpMusicTempoBy"
                    args["change"] = str((0x100 - cmdargs[1]) & 0xFF)
                else:
                    cls = "SlowDownMusicTempoBy"
                    args["change"] = str(cmdargs[1])
            elif cmd["command"] == "adjust_music_pitch":
                args["duration"] = str(cmdargs[2])
                if cmdargs[1] >= 0x80:
                    cls = "IncreaseMusicPitchBy"
                    args["change"] = str((0x100 - cmdargs[1]) & 0xFF)
                else:
                    cls = "ReduceMusicPitchBy"
                    args["change"] = str(cmdargs[1])
            elif cmd["command"] == "append_to_dialog_at_7000":
                cls = "AppendDialogAt7000ToCurrentDialog"
                args["closable"] = "True" if 5 in cmdargs[0] else "False"
                args["sync"] = "False" if 7 in cmdargs[0] else "True"
            elif cmd["command"] == "apply_tile_mod" or cmd["command"] == "apply_solidity_mod":
                if cmd["command"] == "apply_tile_mod":
                    cls = "ApplyTileModToLevel"
                    args["use_alternate"] = "True" if 15 in cmdargs[2] else "False"
                elif cmd["command"] == "apply_solidity_mod":
                    cls = "ApplySolidityModToLevel"
                    args["permanent"] = "True" if 15 in cmdargs[2] else "False"
                args["room_id"] = varnames["rooms"][cmdargs[0]]
                args["mod_id"] = str(cmdargs[1])
            elif cmd["command"] == "circle_mask_expand_from_screen_center":
                cls = "CircleMaskExpandFromScreenCenter"
            elif (
                cmd["command"] == "circle_mask_nonstatic"
                or cmd["command"] == "circle_mask_static"
            ):
                cls = "CircleMaskShrinkToObject"
                args["target"] = AREA_OBJECTS[cmdargs[0]]
                args["width"] = str(cmdargs[1])
                args["speed"] = str(cmdargs[2])
                args["static"] = (
                    "False" if cmd["command"] == "circle_mask_nonstatic" else "True"
                )
            elif cmd["command"] == "circle_mask_shrink_to_screen_center":
                cls = "CircleMaskShrinkToScreenCenter"
            elif (
                cmd["command"]
                == "clear_7016_to_7018_and_isolate_701A_high_byte_if_7018_bit_0_set"
            ):
                cls = "Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set"
            elif cmd["command"] == "clear_bit":
                cls = "ClearBit"
                include_argnames = False
                args["flag"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
            elif cmd["command"] == "close_dialog":
                cls = "CloseDialog"
            elif cmd["command"] == "create_packet_at_npc_coords":
                cls = "CreatePacketAtObjectCoords"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["target_npc"] = AREA_OBJECTS[cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "create_packet_at_7010":
                cls = "CreatePacketAt7010"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "create_packet_at_7010_with_event":
                cls = "CreatePacketAt7010WithEvent"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["event_id"] = varnames["event_scripts"][cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "deactivate_sound_channels":
                cls = "DeactivateSoundChannels"
                include_argnames = False
                bits = cmdargs[0]
                args["bits"] = "set(%r)" % bits
            elif cmd["command"] == "dec":
                cls = "Dec"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif (
                cmd["command"] == "dec_var_from_7000"
                or cmd["command"] == "dec_short_mem_from_7000"
            ):
                cls = "DecVarFrom7000"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "dec_coins":
                cls = "Dec7000FromCoins"
            elif cmd["command"] == "dec_7000_from_current_FP":
                cls = "Dec7000FromCurrentFP"
            elif cmd["command"] == "dec_7000_from_current_HP":
                cls = "Dec7000FromCurrentHP"
                include_argnames = False
                args["character"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "dec_7000_from_frog_coins":
                cls = "Dec7000FromFrogCoins"
            elif cmd["command"] == "display_intro_title":
                cls = "DisplayIntroTitleText"
                args["text"] = INTRO_TEXT[cmdargs[1]]
                args["y"] = str(cmdargs[0])
            elif (
                cmd["command"] == "enable_controls"
                or cmd["command"] == "enable_controls_until_return"
            ):
                if cmd["command"] == "enable_controls":
                    cls = "EnableControls"
                elif cmd["command"] == "enable_controls_until_return":
                    cls = "EnableControlsUntilReturn"
                dirs = []
                for f in cmdargs[0]:
                    dirs.append(CONTROLLER_INPUTS[f])
                include_argnames = False
                args["enabled_buttons"] = "[%s]" % (", ".join(dirs))
            elif cmd["command"] in [
                "summon_to_level",
                "remove_from_level",
                "enable_trigger_in_level",
                "disable_trigger_in_level",
            ]:
                if cmd["command"] == "summon_to_level":
                    cls = "SummonObjectToSpecificLevel"
                elif cmd["command"] == "remove_from_level":
                    cls = "RemoveObjectFromSpecificLevel"
                elif cmd["command"] == "enable_trigger_in_level":
                    cls = "EnableObjectTriggerInSpecificLevel"
                elif cmd["command"] == "disable_trigger_in_level":
                    cls = "DisableObjectTriggerInSpecificLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["level_id"] = varnames["rooms"][cmdargs[1]]
            elif cmd["command"] == "end_all":
                cls = "ReturnAll"
            elif cmd["command"] == "end_loop":
                cls = "EndLoop"
            elif cmd["command"] == "enable_trigger_at_70A8":
                cls = "EnableTriggerOfObjectAt70A8InCurrentLevel"
            elif cmd["command"] == "disable_trigger_at_70A8":
                cls = "DisableTriggerOfObjectAt70A8InCurrentLevel"
            elif cmd["command"] == "enter_area":
                cls = "EnterArea"
                args["room_id"] = varnames["rooms"][cmdargs[0]]
                args["face_direction"] = DIRECTIONS[cmdargs[1]]
                args["x"] = str(cmdargs[2])
                args["y"] = str(cmdargs[3] & 127)
                args["z"] = str(cmdargs[4])
                if 31 in cmdargs[5]:
                    args["z_add_half_unit"] = "True"
                if 11 in cmdargs[5]:
                    args["show_banner"] = "True"
                if 15 in cmdargs[5]:
                    args["run_entrance_event"] = "True"
            elif cmd["command"] == "equip_item_to_character":
                cls = "EquipItemToCharacter"
                args["item"] = classnames["all_items"][cmdargs[1]]
                args["character"] = AREA_OBJECTS[cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "exor_crashes_into_keep":
                cls = "ExorCrashesIntoKeep"
            elif cmd["command"] in [
                "fade_in_from_black_sync",
                "fade_in_from_black_async",
                "fade_in_from_black_sync_duration",
                "fade_in_from_black_async_duration",
            ]:
                cls = "FadeInFromBlack"
                if cmd["command"] in [
                    "fade_in_from_black_async",
                    "fade_in_from_black_async_duration",
                ]:
                    args["sync"] = "False"
                else:
                    args["sync"] = "True"
                if cmd["command"] in [
                    "fade_in_from_black_sync_duration",
                    "fade_in_from_black_async_duration",
                ]:
                    args["duration"] = cmdargs[0]
            elif cmd["command"] == "fade_in_from_colour_duration":
                cls = "FadeInFromColour"
                args["duration"] = cmdargs[0]
                args["colour"] = COLOURS[cmdargs[1]]
            elif cmd["command"] == "fade_in_music":
                cls = "FadeInMusic"
                args["music_id"] = varnames["music"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "fade_out_music":
                cls = "FadeOutMusic"
            elif cmd["command"] == "fade_out_music_FDA3":
                cls = "FadeOutMusicFDA3"
            elif cmd["command"] == "fade_out_music_to_volume":
                cls = "FadeOutMusicToVolume"
                args["duration"] = cmdargs[0]
                args["volume"] = cmdargs[1]
            elif cmd["command"] == "fade_out_sound_to_volume":
                cls = "FadeOutSoundToVolume"
                args["duration"] = cmdargs[0]
                args["volume"] = cmdargs[1]
            elif cmd["command"] in [
                "fade_out_to_black_sync",
                "fade_out_to_black_async",
                "fade_out_to_black_sync_duration",
                "fade_out_to_black_async_duration",
            ]:
                cls = "FadeOutToBlack"
                if cmd["command"] in [
                    "fade_out_to_black_async",
                    "fade_out_to_black_async_duration",
                ]:
                    args["sync"] = "False"
                else:
                    args["sync"] = "True"
                if cmd["command"] in [
                    "fade_out_to_black_sync_duration",
                    "fade_out_to_black_async_duration",
                ]:
                    args["duration"] = str(cmdargs[0])
            elif cmd["command"] == "fade_out_to_colour_duration":
                cls = "FadeOutToColour"
                args["duration"] = str(cmdargs[0])
                args["colour"] = COLOURS[cmdargs[1]]
            elif cmd["command"] == "freeze_all_npcs_until_return":
                cls = "FreezeAllNPCsUntilReturn"
            elif cmd["command"] == "freeze_camera":
                cls = "FreezeCamera"
            elif cmd["command"] == "generate_random_num_from_range_var":
                cls = "GenerateRandomNumFromRangeVar"
                args["address"] = vars_lookup.get(cmdargs[0])
                include_argnames = False
            elif cmd["command"] == "if_0210_bits_012_clear_do_not_jump":
                cls = "If0210Bits012ClearDoNotJump"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "inc_exp_by_packet":
                cls = "IncEXPByPacket"
            elif cmd["command"] == "initiate_battle_mask":
                cls = "InitiateBattleMask"
            elif cmd["command"] == "jmp":
                cls = "Jmp"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_fork_mario_on_object":
                cls = "JmpIfMarioOnAnObjectOrNot"
                include_argnames = False
                args["destinations"] = "%r" % cmdargs
            elif cmd["command"] == "jmp_if_316D_is_3":
                cls = "JmpIf316DIs3"
                args["destinations"] = '["%s"]' % cmdargs[0]
                include_argnames = False
            elif cmd["command"] in ["jmp_if_7000_all_bits_clear", "jmp_if_7000_any_bits_set"]:
                if cmd["command"] == "jmp_if_7000_all_bits_clear":
                    cls = "JmpIf7000AllBitsClear"
                elif cmd["command"] == "jmp_if_7000_any_bits_set":
                    cls = "JmpIf7000AnyBitsSet"
                bits = cmdargs[0]
                args["bits"] = "%r" % bits
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "jmp_if_audio_memory_at_least":
                cls = "JmpIfAudioMemoryIsAtLeast"
                args["threshold"] = str(cmdargs[0])
                args["destinations"] = '["%s"]' % cmdargs[1]
                include_argnames = False
            elif cmd["command"] == "jmp_if_audio_memory_equals":
                cls = "JmpIfAudioMemoryEquals"
                args["value"] = cmdargs[0]
                args["destinations"] = '["%s"]' % cmdargs[1]
                include_argnames = False
            elif cmd["command"] == "jmp_if_bit_clear":
                cls = "JmpIfBitClear"
                include_argnames = False
                args["bit"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_bit_set":
                cls = "JmpIfBitSet"
                include_argnames = False
                args["bit"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_comparison_result_is_greater_or_equal":
                cls = "JmpIfComparisonResultIsGreaterOrEqual"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_comparison_result_is_lesser":
                cls = "JmpIfComparisonResultIsLesser"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_dialog_option_b":
                cls = "JmpIfDialogOptionBSelected"
                args["destinations"] = '["%s"]' % cmdargs[0]
                include_argnames = False
            elif cmd["command"] == "jmp_if_dialog_option_b_or_c":
                cls = "JmpIfDialogOptionBOrCSelected"
                include_argnames = False
                args["destinations"] = "%r" % cmdargs
            elif cmd["command"] == "jmp_if_loaded_memory_is_0":
                cls = "JmpIfLoadedMemoryIs0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_not_0":
                cls = "JmpIfLoadedMemoryIsNot0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_below_0":
                cls = "JmpIfLoadedMemoryIsBelow0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_above_or_equal_0":
                cls = "JmpIfLoadedMemoryIsAboveOrEqual0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_mario_in_air":
                cls = "JmpIfMarioInAir"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_mario_on_object":
                cls = "JmpIfMarioOnObject"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "jmp_if_mem_704x_at_7000_bit_set":
                cls = "JmpIfMem704XAt7000BitSet"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_mem_704x_at_7000_bit_clear":
                cls = "JmpIfMem704XAt7000BitClear"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_object_in_air":
                cls = "JmpIfObjectInAir"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] in ["jmp_if_object_in_level", "jmp_if_object_not_in_level"]:
                if cmd["command"] == "jmp_if_object_in_level":
                    cls = "JmpIfObjectInSpecificLevel"
                elif cmd["command"] == "jmp_if_object_not_in_level":
                    cls = "JmpIfObjectNotInSpecificLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["level_id"] = varnames["rooms"][cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] in [
                "jmp_if_object_trigger_enabled",
                "jmp_if_object_trigger_disabled",
            ]:
                if cmd["command"] == "jmp_if_object_trigger_enabled":
                    cls = "JmpIfObjectTriggerEnabledInSpecificLevel"
                elif cmd["command"] == "jmp_if_object_trigger_disabled":
                    cls = "JmpIfObjectTriggerDisabledInSpecificLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["level_id"] = varnames["rooms"][cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_object_underwater":
                cls = "JmpIfObjectIsUnderwater"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "jmp_if_objects_action_script_running":
                cls = "JmpIfObjectActionScriptIsRunning"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] in [
                "jmp_if_objects_less_than_xy_steps_apart",
                "jmp_if_objects_less_than_xy_steps_apart_same_z_coord",
            ]:
                if cmd["command"] == "jmp_if_objects_less_than_xy_steps_apart":
                    cls = "JmpIfObjectsAreLessThanXYStepsApart"
                elif cmd["command"] == "jmp_if_objects_less_than_xy_steps_apart_same_z_coord":
                    cls = "JmpIfObjectsAreLessThanXYStepsApartSameZCoord"
                include_argnames = False
                args["object_1"] = AREA_OBJECTS[cmdargs[0]]
                args["object_2"] = AREA_OBJECTS[cmdargs[1]]
                args["x"] = str(cmdargs[2])
                args["y"] = str(cmdargs[3])
                args["destinations"] = '["%s"]' % cmdargs[4]
            elif cmd["command"] == "jmp_if_present_in_current_level":
                cls = "JmpIfObjectInCurrentLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "jmp_if_random_above_128":
                cls = "JmpIfRandom1of2"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_random_above_66":
                cls = "JmpIfRandom2of3"
                include_argnames = False
                args["destinations"] = "%r" % cmdargs
            elif cmd["command"] == "jmp_if_var_equals_const":
                cls = "JmpIfVarEqualsConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif (
                cmd["command"] == "jmp_if_var_not_equals_const"
                or cmd["command"] == "jmp_if_var_not_equals_short"
            ):
                cls = "JmpIfVarNotEqualsConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_to_event":
                cls = "JmpToEvent"
                include_argnames = False
                args["destination"] = varnames["event_scripts"][cmdargs[0]]
            elif cmd["command"] == "jmp_to_start_of_this_script":
                cls = "JmpToStartOfThisScript"
            elif cmd["command"] == "jmp_to_start_of_this_script_FA":
                cls = "JmpToStartOfThisScriptFA"
            elif cmd["command"] == "jmp_to_subroutine":
                cls = "JmpToSubroutine"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "join_party":
                cls = "CharacterJoinsParty"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "leave_party":
                cls = "CharacterLeavesParty"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "reactivate_trigger_if_mario_on_top_of_object":
                cls = "ReactivateObject70A8TriggerIfMarioOnTopOfIt"
            elif cmd["command"] == "mario_glows":
                cls = "MarioGlows"
            elif cmd["command"] == "set_mem_704x_at_7000_bit":
                cls = "SetMem704XAt7000Bit"
            elif cmd["command"] == "clear_mem_704x_at_7000_bit":
                cls = "ClearMem704XAt7000Bit"
            elif cmd["command"] in [
                "mem_7000_xor_const",
                "mem_7000_or_const",
                "mem_7000_and_const",
            ]:
                if cmd["command"] == "mem_7000_and_const":
                    cls = "Mem7000AndConst"
                elif cmd["command"] == "mem_7000_or_const":
                    cls = "Mem7000OrConst"
                elif cmd["command"] == "mem_7000_xor_const":
                    cls = "Mem7000XorConst"
                include_argnames = False
                args["value"] = f"0x{cmdargs[0]:04X}"
            elif cmd["command"] in ["mem_7000_or_var", "mem_7000_and_var"]:
                if cmd["command"] == "mem_7000_and_var":
                    cls = "Mem7000AndVar"
                elif cmd["command"] == "mem_7000_or_var":
                    cls = "Mem7000OrVar"
                elif cmd["command"] == "mem_7000_xor_var":
                    cls = "Mem7000XorVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "mem_7000_shift_left":
                cls = "VarShiftLeft"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["shift"] = str(cmdargs[1])
            elif cmd["command"] == "move_7010_7015_to_7016_701B":
                cls = "Move70107015To7016701B"
            elif cmd["command"] == "move_7016_701B_to_7010_7015":
                cls = "Move7016701BTo70107015"
            elif cmd["command"] == "compare_var_to_const":
                cls = "CompareVarToConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
            elif cmd["command"] == "compare_7000_to_var":
                cls = "Compare7000ToVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "move_script_to_main_thread":
                cls = "MoveScriptToMainThread"
            elif cmd["command"] == "move_script_to_background_thread_1":
                cls = "MoveScriptToBackgroundThread1"
            elif cmd["command"] == "move_script_to_background_thread_2":
                cls = "MoveScriptToBackgroundThread2"
            elif (
                cmd["command"]
                == "multiply_and_add_mem_3148_store_to_offset_7FB000_plus_outputx2"
            ):
                cls = "MultiplyAndAddMem3148StoreToOffset7fB000PlusOutputX2"
                args["adding"] = str(cmdargs[0])
                args["multiplying"] = str(cmdargs[1])
            elif cmd["command"] == "open_location":
                cls = "ExitToWorldMap"
                args["area"] = varnames["areas"][cmdargs[0]]
                if 5 in cmdargs[1]:
                    args["bit_5"] = "True"
                if 6 in cmdargs[1]:
                    args["bit_6"] = "True"
                if 7 in cmdargs[1]:
                    args["bit_7"] = "True"
            elif cmd["command"] == "open_menu_or_run_event_sequence":
                cls = "RunMenuOrEventSequence"
                include_argnames = False
                args["scene"] = SCENES[cmdargs[0]]
            elif cmd["command"] == "open_save_menu":
                cls = "OpenSaveMenu"
            elif cmd["command"] == "open_shop":
                cls = "OpenShop"
                include_argnames = False
                args["shop_id"] = varnames["shops"][cmdargs[0]]
            elif cmd["command"] == "palette_set":
                cls = "PaletteSet"
                args["palette_set"] = str(cmdargs[0])
                args["row"] = str(cmdargs[1])
                if 0 in cmdargs[2]:
                    args["bit_0"] = "True"
                if 1 in cmdargs[2]:
                    args["bit_1"] = "True"
                if 2 in cmdargs[2]:
                    args["bit_2"] = "True"
                if 3 in cmdargs[2]:
                    args["bit_3"] = "True"
            elif cmd["command"] == "palette_set_morphs":
                cls = "PaletteSetMorphs"
                args["palette_type"] = PALETTE_TYPES[cmdargs[0]]
                args["duration"] = str(cmdargs[1])
                args["palette_set"] = str(cmdargs[2])
                args["row"] = str(cmdargs[3])
            elif cmd["command"] == "pause":
                cls = "Pause"
                include_argnames = False
                args["length"] = str(cmdargs[0])
            elif cmd["command"] == "pause_script_if_menu_open":
                cls = "PauseScriptIfMenuOpen"
            elif cmd["command"] == "pause_script_until_effect_done":
                cls = "PauseScriptUntilEffectDone"
            elif cmd["command"] == "pause_script_resume_on_next_dialog_page_a":
                cls = "PauseScriptResumeOnNextDialogPageA"
            elif cmd["command"] == "pause_script_resume_on_next_dialog_page_b":
                cls = "PauseScriptResumeOnNextDialogPageB"
            elif cmd["command"] == "pixelate_layers":
                cls = "PixelateLayers"
                layers = []
                for n in cmdargs[0]:
                    layers.append(LAYER_TYPES[n])
                args["layers"] = "[%s]" % ", ".join(layers)
                args["pixel_size"] = str(cmdargs[1])
                args["duration"] = str(cmdargs[2] & 0x3F)
                args["bit_6"] = "True" if cmdargs[2] & 0x40 != 0 else "False"
                args["bit_7"] = "True" if cmdargs[2] & 0x80 != 0 else "False"
            elif cmd["command"] == "play_music":
                cls = "PlayMusic"
                args["music_id"] = varnames["music"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "play_music_default_volume":
                cls = "PlayMusicAtDefaultVolume"
                args["music_id"] = varnames["music"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "play_music_current_volume":
                cls = "PlayMusicAtCurrentVolume"
                args["music_id"] = varnames["music"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "play_sound":
                cls = "PlaySound"
                args["sound"] = varnames["overworld_sfx"][cmdargs[0]]
                args["channel"] = str(cmdargs[1])
            elif cmd["command"] in ["play_sound_balance", "play_sound_balance_FD9D"]:
                if cmd["command"] == "play_sound_balance":
                    cls = "PlaySoundBalance"
                else:
                    cls = "PlaySoundBalanceFD9D"
                args["sound"] = varnames["overworld_sfx"][cmdargs[0]]
                args["balance"] = str(cmdargs[1])
            elif cmd["command"] == "priority_set":
                cls = "PrioritySet"
                mainscreen = []
                for n in cmdargs[0]:
                    mainscreen.append(LAYER_TYPES[n])
                subscreen = []
                for n in cmdargs[1]:
                    subscreen.append(LAYER_TYPES[n])
                colour_math = []
                for n in cmdargs[2]:
                    colour_math.append(LAYER_TYPES[n])
                args["mainscreen"] = "[%s]" % ", ".join(mainscreen)
                args["subscreen"] = "[%s]" % ", ".join(subscreen)
                args["colour_math"] = "[%s]" % ", ".join(colour_math)
            elif cmd["command"] == "put_70A7_equips_inventory":
                cls = "Store70A7ToEquipsInventory"
            elif cmd["command"] == "put_inventory":
                cls = "AddToInventory"
                include_argnames = False
                if cmdargs[0] == 0x70A7:
                    args["item"] = vars_lookup.get(0x70A7)
                else:
                    args["item"] = classnames["all_items"][cmdargs[0]]
            elif cmd["command"] == "read_from_address":
                cls = "ReadFromAddress"
                include_argnames = False
                args["address"] = f"0x{cmdargs[0]:04X}"
            elif cmd["command"] == "remember_last_object":
                cls = "RememberLastObject"
            elif cmd["command"] == "remove_object_at_70A8_from_current_level":
                cls = "RemoveObjectAt70A8FromCurrentLevel"
            elif cmd["command"] == "remove_one_from_inventory":
                cls = "RemoveOneOfItemFromInventory"
                include_argnames = False
                args["item"] = classnames["all_items"][cmdargs[0]]
            elif cmd["command"] == "reset_and_choose_game":
                cls = "ResetAndChooseGame"
            elif cmd["command"] == "reset_game":
                cls = "ResetGame"
            elif cmd["command"] == "reset_priority_set":
                cls = "ResetPrioritySet"
            elif cmd["command"] == "restore_all_fp":
                cls = "RestoreAllFP"
            elif cmd["command"] == "restore_all_hp":
                cls = "RestoreAllHP"
            elif cmd["command"] == "resume_background_event":
                cls = "ResumeBackgroundEvent"
                include_argnames = False
                args["timer_var"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "ret":
                cls = "Return"
            elif cmd["command"] == "run_background_event":
                cls = "RunBackgroundEvent"
                args["event_id"] = varnames["event_scripts"][cmdargs[0]]
                if 13 in cmdargs[1]:
                    args["return_on_level_exit"] = "True"
                if 14 in cmdargs[1]:
                    args["bit_6"] = "True"
                if 15 in cmdargs[1]:
                    args["run_as_second_script"] = "True"
            elif cmd["command"] in [
                "run_background_event_with_pause",
                "run_background_event_with_pause_return_on_exit",
            ]:
                if cmd["command"] == "run_background_event_with_pause":
                    cls = "RunBackgroundEventWithPause"
                else:
                    cls = "RunBackgroundEventWithPauseReturnOnExit"
                args["event_id"] = varnames["event_scripts"][cmdargs[0]]
                args["timer_var"] = vars_lookup.get(cmdargs[1])
                if 12 in cmdargs[2]:
                    args["bit_4"] = "True"
                if 13 in cmdargs[2]:
                    args["bit_5"] = "True"
            elif cmd["command"] == "run_dialog":
                cls = "RunDialog"
                if cmdargs[0] == 0x7000:
                    args["dialog_id"] = vars_lookup.get(0x7000)
                else:
                    args["dialog_id"] = varnames["dialogs"][cmdargs[0]]
                args["above_object"] = AREA_OBJECTS[cmdargs[1]]
                args["closable"] = "True" if 5 in cmdargs[2] else "False"
                args["sync"] = "False" if 7 in cmdargs[2] else "True"
                args["multiline"] = "True" if 14 in cmdargs[2] else "False"
                args["use_background"] = "True" if 15 in cmdargs[2] else "False"
                if 6 in cmdargs[2]:
                    args["bit_6"] = "True"
            elif cmd["command"] == "run_dialog_duration":
                cls = "RunDialogForDuration"
                args["dialog_id"] = varnames["dialogs"][cmdargs[0]]
                args["duration"] = str(cmdargs[1])
                args["sync"] = "False" if 7 in cmdargs[2] else "True"
            elif cmd["command"] == "run_ending_credits":
                cls = "RunEndingCredits"
            elif cmd["command"] == "run_event_at_return":
                cls = "RunEventAtReturn"
                args["event_id"] = varnames["event_scripts"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "run_event_as_subroutine":
                cls = "RunEventAsSubroutine"
                args["event_id"] = varnames["event_scripts"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "run_event_sequence":
                cls = "RunEventSequence"
                args["scene"] = SCENES[cmdargs[0]]
                args["value"] = str(cmdargs[1])
            elif cmd["command"] == "run_levelup_bonus_sequence":
                cls = "RunLevelupBonusSequence"
            elif cmd["command"] == "run_menu_tutorial":
                cls = "RunMenuTutorial"
                args["tutorial"] = TUTORIALS[cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "run_moleville_mountain_intro_sequence":
                cls = "RunMolevilleMountainIntroSequence"
            elif cmd["command"] == "run_moleville_mountain_sequence":
                cls = "RunMolevilleMountainSequence"
            elif cmd["command"] == "run_star_piece_sequence":
                cls = "RunStarPieceSequence"
                args["star"] = str(cmdargs[0])
                include_argnames = False
            elif cmd["command"] == "screen_flashes_with_colour":
                cls = "ScreenFlashesWithColour"
                include_argnames = False
                args["colour"] = COLOURS[cmdargs[0]]
            elif cmd["command"] == "set_var_to_const":
                cls = "SetVarToConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
            elif cmd["command"] == "set_7000_to_7F_mem_var":
                cls = "Set7000To7FMemVar"
                include_argnames = False
                args["address"] = f"0x{cmdargs[0]:04X}"
            elif cmd["command"] == "set_bit":
                cls = "SetBit"
                include_argnames = False
                args["flag"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
            elif cmd["command"] == "set_bit_3":
                cls = "MarioStopsGlowing"
            elif cmd["command"] == "set_bit_3_offset":
                cls = "Set0158Bit3Offset"
                include_argnames = False
                args["address"] = f"0x{cmdargs[0]:04X}"
            elif cmd["command"] in ["set_bit_7_offset", "clear_bit_7_offset"]:
                if cmd["command"] == "set_bit_7_offset":
                    cls = "Set0158Bit7Offset"
                else:
                    cls = "Clear0158Bit7Offset"
                include_argnames = False
                args["address"] = f"0x{cmdargs[0]:04X}"
                if 7 in cmdargs[1]:
                    args["bit_7"] = "True"
            elif cmd["command"] == "set_var_to_random":
                cls = "SetVarToRandom"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["value"] = str(cmdargs[1])
            elif cmd["command"] == "set_7000_to_current_level":
                cls = "Set7000ToCurrentLevel"
            elif cmd["command"] == "set_7000_to_object_coord":
                cls = "Set7000ToObjectCoord"
                args["target_npc"] = AREA_OBJECTS[cmdargs[0]]
                coord = cmdargs[1]
                if coord == 0:
                    args["coord"] = "COORD_X"
                elif coord == 1:
                    args["coord"] = "COORD_Y"
                elif coord == 2:
                    args["coord"] = "COORD_Z"
                elif coord == 5:
                    args["coord"] = "COORD_F"
                if len(cmdargs) > 3 and cmdargs[3] > 0:
                    args["isometric"] = True
                else:
                    args["pixel"] = True
                if len(cmdargs[2]) > 0:
                    args["bit_7"] = "True"
            elif cmd["command"] == "set_7000_to_pressed_button":
                cls = "Set7000ToPressedButton"
            elif cmd["command"] == "set_7000_to_tapped_button":
                cls = "Set7000ToTappedButton"
            elif cmd["command"] == "set_7010_to_object_xyz":
                try:
                    cls = "Set70107015ToObjectXYZ"
                    args["target"] = AREA_OBJECTS[cmdargs[0] & 0x3F]
                    if cmdargs[0] & 0x40 == 0x40:
                        args["bit_6"] = "True"
                    if cmdargs[0] & 0x80 == 0x80:
                        args["bit_7"] = "True"
                except:
                    cls = "UnknownCommand"
                    args["args"] = "%r" % bytearray([0xC7, cmdargs[0]])
            elif cmd["command"] == "set_7016_to_object_xyz":
                try:
                    cls = "Set7016701BToObjectXYZ"
                    args["target"] = AREA_OBJECTS[cmdargs[0] & 0x3F]
                    if cmdargs[0] & 0x40 == 0x40:
                        args["bit_6"] = "True"
                    if cmdargs[0] & 0x80 == 0x80:
                        args["bit_7"] = "True"
                except:
                    cls = "UnknownCommand"
                    args["args"] = "%r" % bytearray([0xC8, cmdargs[0]])
            elif cmd["command"] == "set_experience_packet_7000":
                cls = "SetEXPPacketTo7000"
            elif cmd["command"] == "set_object_memory_to":
                cls = "SetObjectMemoryToVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "copy_var_to_var":
                cls = "CopyVarToVar"
                args["from_var"] = vars_lookup.get(cmdargs[0])
                args["to_var"] = vars_lookup.get(cmdargs[1])
            elif cmd["command"] == "set_7000_to_member_in_slot":
                cls = "Set7000ToIDOfMemberInSlot"
                args["slot"] = str(cmdargs[0])
                include_argnames = False
            elif cmd["command"] == "set_7000_to_party_capacity":
                cls = "Set7000ToPartySize"
            elif cmd["command"] == "slow_down_music":
                cls = "SlowDownMusic"
            elif cmd["command"] == "speed_up_music_to_normal":
                cls = "SpeedUpMusicToDefault"
            elif cmd["command"] == "star_mask_expand_from_screen_center":
                cls = "StarMaskExpandFromScreenCenter"
            elif cmd["command"] == "star_mask_shrink_to_screen_center":
                cls = "StarMaskShrinkToScreenCenter"
            elif cmd["command"] == "start_battle":
                cls = "StartBattleAtBattlefield"
                include_argnames = False
                args["pack_id"] = varnames["packs"][cmdargs[0]]
                args["battlefield"] = varnames["battlefields"][cmdargs[1]]
            elif cmd["command"] == "stop_all_background_events":
                cls = "StopAllBackgroundEvents"
            elif cmd["command"] == "store_bytes_to_0335_0556":
                cls = "StoreBytesTo0335And0556"
                args["value_1"] = str(cmdargs[0])
                args["value_2"] = str(cmdargs[1])
            elif cmd["command"] == "store_00_to_0248":
                cls = "Store00To0248"
            elif cmd["command"] == "store_00_to_0334":
                cls = "Store00To0334"
            elif cmd["command"] == "store_01_to_0248":
                cls = "Store01To0248"
            elif cmd["command"] == "store_01_to_0335":
                cls = "Store01To0335"
            elif cmd["command"] == "store_02_to_0248":
                cls = "Store02To0248"
            elif cmd["command"] == "store_FF_to_0335":
                cls = "StoreFFTo0335"
            elif cmd["command"] == "store_7000_minecart_timer":
                cls = "Set7000ToMinecartTimer"
            elif cmd["command"] == "store_set_bits":
                cls = "StoreSetBits"
                args["bit"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
                include_argnames = False
            elif cmd["command"] == "start_battle_700E":
                cls = "StartBattleWithPackAt700E"
            elif cmd["command"] == "start_loop_n_times":
                cls = "StartLoopNTimes"
                include_argnames = False
                args["count"] = str(cmdargs[0])
            elif cmd["command"] == "start_loop_n_frames":
                cls = "StartLoopNFrames"
                include_argnames = False
                args["length"] = str(cmdargs[0])
            elif cmd["command"] == "stop_music_FD9F":
                cls = "StopMusicFD9F"
            elif cmd["command"] == "stop_music_FDA0":
                cls = "StopMusicFDA0"
            elif cmd["command"] == "stop_music_FDA1":
                cls = "StopMusicFDA1"
            elif cmd["command"] == "stop_music_FDA2":
                cls = "StopMusicFDA2"
            elif cmd["command"] == "stop_music_FDA6":
                cls = "StopMusicFDA6"
            elif cmd["command"] == "stop_music":
                cls = "StopMusic"
            elif cmd["command"] == "stop_sound":
                cls = "StopSound"
            elif cmd["command"] == "store_7000_item_quantity_to_70A7":
                cls = "StoreItemAt70A7QuantityTo7000"
            elif cmd["command"] == "store_character_equipment_7000":
                cls = "StoreCharacterEquipmentTo7000"
                args["character"] = AREA_OBJECTS[cmdargs[0]]
                args["equip_slot"] = classnames["all_items"][cmdargs[1]]
                include_argnames = False
            elif cmd["command"] == "store_current_FP_7000":
                cls = "StoreCurrentFPTo7000"
            elif cmd["command"] == "store_empty_inventory_slot_count_7000":
                cls = "StoreEmptyItemInventorySlotCountTo7000"
            elif cmd["command"] == "store_coin_amount_7000":
                cls = "StoreCoinCountTo7000"
            elif cmd["command"] == "store_item_amount_7000":
                cls = "StoreItemAmountTo7000"
                args["item"] = classnames["all_items"][cmdargs[0]]
                include_argnames = False
            elif cmd["command"] == "store_frog_coin_amount_7000":
                cls = "StoreFrogCoinCountTo7000"
            elif cmd["command"] == "stop_background_event":
                cls = "StopBackgroundEvent"
                include_argnames = False
                args["timer_var"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "summon_object_at_70A8_to_current_level":
                cls = "SummonObjectAt70A8ToCurrentLevel"
            elif cmd["command"] == "swap_vars":
                cls = "SwapVars"
                include_argnames = False
                args["memory_a"] = vars_lookup.get(cmdargs[1])
                args["memory_b"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "tint_layers":
                cls = "TintLayers"
                layers = []
                for n in cmdargs[4]:
                    layers.append(LAYER_TYPES[n])
                args["layers"] = "[%s]" % ", ".join(layers)
                args["red"] = str(cmdargs[0])
                args["green"] = str(cmdargs[1])
                args["blue"] = str(cmdargs[2])
                args["speed"] = str(cmdargs[3])
                if 7 in cmdargs[5]:
                    args["bit_15"] = "True"
            elif cmd["command"] == "unfreeze_all_npcs":
                cls = "UnfreezeAllNPCs"
            elif cmd["command"] == "unfreeze_camera":
                cls = "UnfreezeCamera"
            elif cmd["command"] == "unsync_dialog":
                cls = "UnsyncDialog"
            elif cmd["command"] == "xor_3105_with_01" or cmd["command"] == "return_fd":
                cls = "ReturnFD"
            elif cmd["command"] == "db":
                cls = "UnknownCommand"
                include_argnames = False
                args["args"] = "%r" % bytearray(cmdargs)
            else:
                raise Exception("%s not found" % cmd["command"])

            return cls, args, use_identifier, include_argnames

        def convert_action_script_command(cmd, valid_identifiers):
            use_identifier: bool = cmd["identifier"] in valid_identifiers
            args = {}
            cls = None
            cmdargs = []
            include_argnames = True

            if "args" in cmd:
                cmdargs = cmd["args"]

            if cmd["command"] == "visibility_on":
                cls = "A_VisibilityOn"
            elif cmd["command"] == "visibility_off":
                cls = "A_VisibilityOff"
            elif cmd["command"] == "sequence_playback_on":
                cls = "A_SequencePlaybackOn"
            elif cmd["command"] == "sequence_playback_off":
                cls = "A_SequencePlaybackOff"
            elif cmd["command"] == "sequence_looping_on":
                cls = "A_SequenceLoopingOn"
            elif cmd["command"] == "sequence_looping_off":
                cls = "A_SequenceLoopingOff"
            elif cmd["command"] == "fixed_f_coord_on":
                cls = "A_FixedFCoordOn"
            elif cmd["command"] == "fixed_f_coord_off":
                cls = "A_FixedFCoordOff"
            elif cmd["command"] == "set_sprite_sequence":
                cls = "A_SetSpriteSequence"
                args["index"] = str(cmdargs[0])
                if cmdargs[1] > 0:
                    args["sprite_offset"] = str(cmdargs[1])
                flags = cmdargs[2]
                if 3 in flags:
                    args["is_mold"] = "True"
                if 6 in flags:
                    args["is_sequence"] = "True"
                looping_off = 4 in flags
                if (not looping_off) or not (3 in flags and 6 not in flags):
                    args["looping"] = "False" if looping_off else "True"
                if 15 in flags:
                    args["mirror_sprite"] = "True"
            elif cmd["command"] == "reset_properties":
                cls = "A_ResetProperties"
            elif cmd["command"] in [
                "overwrite_solidity",
                "set_solidity_bits",
                "clear_solidity_bits",
                "set_movement_bits",
            ]:
                if cmd["command"] == "overwrite_solidity":
                    cls = "A_OverwriteSolidity"
                elif cmd["command"] == "set_solidity_bits":
                    cls = "A_SetSolidityBits"
                elif cmd["command"] == "clear_solidity_bits":
                    cls = "A_ClearSolidityBits"
                elif cmd["command"] == "set_movement_bits":
                    cls = "A_SetMovementsBits"
                flags = cmdargs[0]
                if 0 in flags:
                    args["bit_0"] = "True"
                if 1 in flags:
                    args["cant_walk_under"] = "True"
                if 2 in flags:
                    args["cant_pass_walls"] = "True"
                if 3 in flags:
                    args["cant_jump_through"] = "True"
                if 4 in flags:
                    args["bit_4"] = "True"
                if 5 in flags:
                    args["cant_pass_npcs"] = "True"
                if 6 in flags:
                    args["cant_walk_through"] = "True"
                if 7 in flags:
                    args["bit_7"] = "True"
            elif cmd["command"] == "set_palette_row":
                cls = "A_SetPaletteRow"
                args["row"] = str(cmdargs[0] & 0xF)
                upper = (cmdargs[0] & 0xF0) >> 4
                if upper != 0:
                    args["upper"] = str(upper)
            elif cmd["command"] == "inc_palette_row_by":
                cls = "A_IncPaletteRowBy"
                include_argnames = False
                args["rows"] = str(cmdargs[0] & 0x0F)
                upper = (cmdargs[0] & 0xF0) >> 4
                if upper != 0:
                    args["upper"] = str(upper)
            elif cmd["command"] == "set_animation_speed":
                include_argnames = False
                speed = cmdargs[0]
                if speed == 0:
                    args["speed"] = "NORMAL"
                elif speed == 1:
                    args["speed"] = "FAST"
                elif speed == 2:
                    args["speed"] = "FASTER"
                elif speed == 3:
                    args["speed"] = "VERY_FAST"
                elif speed == 4:
                    args["speed"] = "FASTEST"
                elif speed == 5:
                    args["speed"] = "SLOW"
                elif speed == 6:
                    args["speed"] = "VERY_SLOW"
                else:
                    raise Exception("illegal speed")
                flags = cmdargs[1]
                if 0 in flags and 1 not in flags:
                    cls = "A_SetWalkingSpeed"
                elif 1 in flags and 0 not in flags:
                    cls = "A_SetSequenceSpeed"
                elif 0 in flags and 1 in flags:
                    cls = "A_SetAllSpeeds"
                else:
                    raise Exception("%s %r speed has no type" % (cmd["identifier"], flags))
            elif cmd["command"] == "set_object_memory_bits":
                cls = "A_SetObjectMemoryBits"
                args["arg_1"] = f"0x{cmdargs[0]:02X}"
                bits = cmdargs[1]
                args["bits"] = "%r" % bits
            elif cmd["command"] == "set_vram_priority":
                cls = "A_SetVRAMPriority"
                priority = cmdargs[0]
                include_argnames = False
                if priority == 0:
                    args["priority"] = "MARIO_OVERLAPS_ON_ALL_SIDES"
                elif priority == 1:
                    args["priority"] = "NORMAL_PRIORITY"
                elif priority == 2:
                    args["priority"] = "OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES"
                elif priority == 3:
                    args["priority"] = "PRIORITY_3"
            elif cmd["command"] == "bpl_26_27_28":
                cls = "A_BPL262728"
            elif cmd["command"] == "bmi_26_27_28":
                cls = "A_BMI262728"
            elif cmd["command"] == "embedded_animation_routine":
                cls = "A_EmbeddedAnimationRoutine"
                include_argnames = False
                args["args"] = "%r" % bytearray(cmdargs)
            elif cmd["command"] == "bpl_26_27":
                cls = "A_BPL2627"
            elif (
                cmd["command"] == "jmp_if_object_within_range"
                or cmd["command"] == "jmp_if_object_within_range_same_z"
            ):
                if cmd["command"] == "jmp_if_object_within_range":
                    cls = "A_JmpIfObjectWithinRange"
                elif cmd["command"] == "jmp_if_object_within_range_same_z":
                    cls = "A_JmpIfObjectWithinRangeSameZ"
                args["comparing_npc"] = AREA_OBJECTS[cmdargs[0]]
                args["usually"] = str(cmdargs[1])
                args["tiles"] = str(cmdargs[2])
                args["destinations"] = '["%s"]' % cmdargs[3]
            elif cmd["command"] == "unknown_jmp_3C":
                cls = "A_UnknownJmp3C"
                include_argnames = False
                args["arg1"] = f"0x{cmdargs[0]:02X}"
                args["arg2"] = f"0x{cmdargs[1]:02X}"
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_mario_in_air":
                cls = "A_JmpIfMarioInAir"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "create_packet_at_npc_coords":
                cls = "A_CreatePacketAtObjectCoords"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["target_npc"] = AREA_OBJECTS[cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "create_packet_at_7010":
                cls = "A_CreatePacketAt7010"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "walk_1_step_east":
                cls = "A_Walk1StepEast"
            elif cmd["command"] == "walk_1_step_southeast":
                cls = "A_Walk1StepSoutheast"
            elif cmd["command"] == "walk_1_step_south":
                cls = "A_Walk1StepSouth"
            elif cmd["command"] == "walk_1_step_southwest":
                cls = "A_Walk1StepSouthwest"
            elif cmd["command"] == "walk_1_step_west":
                cls = "A_Walk1StepWest"
            elif cmd["command"] == "walk_1_step_northwest":
                cls = "A_Walk1StepNorthwest"
            elif cmd["command"] == "walk_1_step_north":
                cls = "A_Walk1StepNorth"
            elif cmd["command"] == "walk_1_step_northeast":
                cls = "A_Walk1StepNortheast"
            elif cmd["command"] == "walk_1_step_f_direction":
                cls = "A_Walk1StepFDirection"
            elif cmd["command"] == "add_z_coord_1_step":
                cls = "A_AddZCoord1Step"
            elif cmd["command"] == "dec_z_coord_1_step":
                cls = "A_DecZCoord1Step"
            elif cmd["command"] == "shift_east_steps":
                cls = "A_WalkEastSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_southeast_steps":
                cls = "A_WalkSoutheastSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_south_steps":
                cls = "A_WalkSouthSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_southwest_steps":
                cls = "A_WalkSouthwestSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_west_steps":
                cls = "A_WalkWestSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_northwest_steps":
                cls = "A_WalkNorthwestSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_north_steps":
                cls = "A_WalkNorthSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_northeast_steps":
                cls = "A_WalkNortheastSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_f_direction_steps":
                cls = "A_WalkFDirectionSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_z_20_steps":
                cls = "A_WalkF20Steps"
            elif cmd["command"] == "shift_z_up_steps":
                cls = "A_ShiftZUpSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_z_down_steps":
                cls = "A_ShiftZDownSteps"
                include_argnames = False
                args["steps"] = str(cmdargs[0])
            elif cmd["command"] == "shift_z_up_20_steps":
                cls = "A_ShiftZUp20Steps"
            elif cmd["command"] == "shift_z_down_20_steps":
                cls = "A_ShiftZDown20Steps"
            elif cmd["command"] == "shift_east_pixels":
                cls = "A_WalkEastPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_southeast_pixels":
                cls = "A_WalkSoutheastPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_south_pixels":
                cls = "A_WalkSouthPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_southwest_pixels":
                cls = "A_WalkSouthwestPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_west_pixels":
                cls = "A_WalkWestPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_northwest_pixels":
                cls = "A_WalkNorthwestPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_north_pixels":
                cls = "A_WalkNorthPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_northeast_pixels":
                cls = "A_WalkNortheastPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_f_direction_pixels":
                cls = "A_WalkFDirectionPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "walk_f_direction_16_pixels":
                cls = "A_WalkFDirection16Pixels"
            elif cmd["command"] == "shift_z_up_pixels":
                cls = "A_ShiftZUpPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "shift_z_down_pixels":
                cls = "A_ShiftZDownPixels"
                include_argnames = False
                args["pixels"] = str(cmdargs[0])
            elif cmd["command"] == "face_east":
                cls = "A_FaceEast"
            elif cmd["command"] == "face_east_7C":
                cls = "A_FaceEast7C"
            elif cmd["command"] == "face_southeast":
                cls = "A_FaceSoutheast"
            elif cmd["command"] == "face_south":
                cls = "A_FaceSouth"
            elif cmd["command"] == "face_southwest":
                cls = "A_FaceSouthwest"
            elif cmd["command"] == "face_southwest_7D":
                cls = "A_FaceSouthwest7D"
                args["arg"] = f"0x{cmdargs[0]:02X}"
            elif cmd["command"] == "face_west":
                cls = "A_FaceWest"
            elif cmd["command"] == "face_northwest":
                cls = "A_FaceNorthwest"
            elif cmd["command"] == "face_north":
                cls = "A_FaceNorth"
            elif cmd["command"] == "face_northeast":
                cls = "A_FaceNortheast"
            elif cmd["command"] == "face_mario":
                cls = "A_FaceMario"
            elif cmd["command"] == "turn_clockwise_45_degrees":
                cls = "A_TurnClockwise45Degrees"
            elif cmd["command"] == "turn_random_direction":
                cls = "A_TurnRandomDirection"
            elif cmd["command"] == "turn_clockwise_45_degrees_n_times":
                cls = "A_TurnClockwise45DegreesNTimes"
                include_argnames = False
                args["count"] = str(cmdargs[0])
            elif (
                cmd["command"] == "jump_to_height_silent" or cmd["command"] == "jump_to_height"
            ):
                cls = "A_JumpToHeight"
                args["height"] = str(cmdargs[0])
                if cmd["command"] == "jump_to_height_silent":
                    args["silent"] = "True"
                else:
                    include_argnames = False
            elif cmd["command"] in [
                "walk_to_xy_coords",
                "walk_xy_steps",
                "shift_to_xy_coords",
                "shift_xy_steps",
                "shift_xy_pixels",
            ]:
                if cmd["command"] == "walk_to_xy_coords":
                    cls = "A_WalkToXYCoords"
                elif cmd["command"] == "walk_xy_steps":
                    cls = "A_WalkXYSteps"
                elif cmd["command"] == "shift_to_xy_coords":
                    cls = "A_ShiftToXYCoords"
                elif cmd["command"] == "shift_xy_steps":
                    cls = "A_ShiftXYSteps"
                elif cmd["command"] == "shift_xy_pixels":
                    cls = "A_ShiftXYPixels"
                args["x"] = str(cmdargs[0])
                args["y"] = str(cmdargs[1])
            elif cmd["command"] == "maximize_sequence_speed":
                cls = "A_MaximizeSequenceSpeed"
            elif cmd["command"] == "maximize_sequence_speed_86":
                cls = "A_MaximizeSequenceSpeed86"
            elif cmd["command"] == "transfer_to_object_xy":
                cls = "A_TransferToObjectXY"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "run_away_shift":
                cls = "A_RunAwayShift"
            elif cmd["command"] == "transfer_to_7016_7018":
                cls = "A_TransferTo70167018"
            elif cmd["command"] == "walk_to_7016_7018":
                cls = "A_WalkTo70167018"
            elif (
                cmd["command"] == "bounce_to_xy_with_height"
                or cmd["command"] == "bounce_xy_steps_with_height"
            ):
                if cmd["command"] == "bounce_to_xy_with_height":
                    cls = "A_BounceToXYWithHeight"
                elif cmd["command"] == "bounce_xy_steps_with_height":
                    cls = "A_BounceXYStepsWithHeight"
                args["x"] = str(cmdargs[0])
                args["y"] = str(cmdargs[1])
                args["height"] = str(cmdargs[2])
            elif cmd["command"] in [
                "transfer_to_xyzf",
                "transfer_xyzf_steps",
                "transfer_xyzf_pixels",
            ]:
                if cmd["command"] == "transfer_to_xyzf":
                    cls = "A_TransferToXYZF"
                elif cmd["command"] == "transfer_xyzf_steps":
                    cls = "A_TransferXYZFSteps"
                elif cmd["command"] == "transfer_xyzf_pixels":
                    cls = "A_TransferXYZFPixels"
                args["x"] = str(cmdargs[0])
                args["y"] = str(cmdargs[1])
                args["z"] = str(cmdargs[2])
                args["direction"] = DIRECTIONS[cmdargs[3]]
            elif cmd["command"] == "transfer_to_object_xyz":
                cls = "A_TransferToObjectXYZ"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
            elif cmd["command"] == "walk_to_7016_7018_701A":
                cls = "A_WalkTo70167018701A"
            elif cmd["command"] == "transfer_to_7016_7018_701A":
                cls = "A_TransferTo70167018701A"
            elif cmd["command"] == "stop_sound":
                cls = "A_StopSound"
            elif cmd["command"] == "play_sound":
                cls = "A_PlaySound"
                args["sound"] = varnames["overworld_sfx"][cmdargs[0]]
                args["channel"] = str(cmdargs[1])
            elif cmd["command"] == "play_sound_balance":
                cls = "A_PlaySoundBalance"
                args["sound"] = varnames["overworld_sfx"][cmdargs[0]]
                args["balance"] = str(cmdargs[1])
            elif cmd["command"] == "fade_out_sound_to_volume":
                cls = "A_FadeOutSoundToVolume"
                args["duration"] = str(cmdargs[0])
                args["volume"] = str(cmdargs[1])
            elif cmd["command"] == "set_bit":
                cls = "A_SetBit"
                include_argnames = False
                args["flag"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
            elif cmd["command"] == "set_mem_704x_at_700C_bit":
                cls = "A_SetMem704XAt700CBit"
            elif cmd["command"] == "clear_bit":
                cls = "A_ClearBit"
                include_argnames = False
                args["flag"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
            elif cmd["command"] == "clear_mem_704x_at_700C_bit":
                cls = "A_ClearMem704XAt700CBit"
            elif cmd["command"] == "set_var_to_const":
                cls = "A_SetVarToConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
            elif cmd["command"] == "add_const_to_var" or cmd["command"] == "add":
                cls = "A_AddConstToVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["value"] = str(cmdargs[1])
            elif cmd["command"] == "inc" or cmd["command"] == "inc_short":
                cls = "A_Inc"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "dec":
                cls = "A_Dec"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "copy_var_to_var":
                cls = "A_CopyVarToVar"
                args["from_var"] = vars_lookup.get(cmdargs[0])
                args["to_var"] = vars_lookup.get(cmdargs[1])
            elif cmd["command"] == "set_var_to_random":
                cls = "A_SetVarToRandom"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["value"] = str(cmdargs[1])
            elif (
                cmd["command"] == "add_var_to_700C" or cmd["command"] == "add_short_mem_to_700C"
            ):
                cls = "A_AddVarTo700C"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif (
                cmd["command"] == "dec_var_from_700C"
                or cmd["command"] == "dec_short_mem_from_700C"
            ):
                cls = "A_DecVarFrom700C"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "swap_vars":
                cls = "A_SwapVars"
                include_argnames = False
                args["memory_a"] = vars_lookup.get(cmdargs[1])
                args["memory_b"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "move_7010_7015_to_7016_701B":
                cls = "A_Move70107015To7016701B"
            elif cmd["command"] == "move_7016_701B_to_7010_7015":
                cls = "A_Move7016701BTo70107015"
            elif (
                cmd["command"] == "compare_var_to_const"
                or cmd["command"] == "mem_compare"
                or cmd["command"] == "mem_compare_val"
            ):
                cls = "A_CompareVarToConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
            elif cmd["command"] == "compare_700C_to_var":
                cls = "A_Compare700CToVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "set_700C_to_current_level":
                cls = "A_Set700CToCurrentLevel"
            elif cmd["command"] == "set_700C_to_object_coord":
                cls = "A_Set700CToObjectCoord"
                args["target_npc"] = AREA_OBJECTS[cmdargs[0]]
                coord = cmdargs[1]
                if coord == 0:
                    args["coord"] = "COORD_X"
                elif coord == 1:
                    args["coord"] = "COORD_Y"
                elif coord == 2:
                    args["coord"] = "COORD_Z"
                elif coord == 5:
                    args["coord"] = "COORD_F"
                if coord != 5:
                    if len(cmdargs) > 3 and cmdargs[3] > 0:
                        args["isometric"] = True
                    else:
                        args["pixel"] = True
                    if len(cmdargs[2]) > 0:
                        args["bit_7"] = "True"
            elif cmd["command"] == "set_700C_to_pressed_button":
                cls = "A_Set700CToPressedButton"
            elif cmd["command"] == "set_700C_to_tapped_button":
                cls = "A_Set700CToTappedButton"
            elif cmd["command"] == "jmp_to_script":
                cls = "A_JmpToScript"
                include_argnames = False
                args["destination"] = varnames["action_scripts"][cmdargs[0]]
            elif cmd["command"] == "jmp":
                cls = "A_Jmp"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_to_subroutine":
                cls = "A_JmpToSubroutine"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "start_loop_n_times":
                cls = "A_StartLoopNTimes"
                include_argnames = False
                args["count"] = str(cmdargs[0])
            elif cmd["command"] == "start_loop_n_frames":
                cls = "A_StartLoopNFrames"
                include_argnames = False
                args["length"] = str(cmdargs[0])
            elif cmd["command"] == "load_mem":
                cls = "A_LoadMemory"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "end_loop":
                cls = "A_EndLoop"
            elif cmd["command"] == "jmp_if_bit_clear":
                cls = "A_JmpIfBitClear"
                include_argnames = False
                args["bit"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_bit_set":
                cls = "A_JmpIfBitSet"
                include_argnames = False
                args["bit"] = flags_lookup.get((cmdargs[0], cmdargs[1]))
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_mem_704x_at_700C_bit_set":
                cls = "A_JmpIfMem704XAt700CBitSet"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_mem_704x_at_700C_bit_clear":
                cls = "A_JmpIfMem704XAt700CBitClear"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_var_equals_const":
                cls = "A_JmpIfVarEqualsConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_if_var_not_equals_const":
                cls = "A_JmpIfVarNotEqualsConst"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                if cmdargs[0] == 0x70A7:
                    try:
                        args["value"] = classnames["all_items"][cmdargs[1]]
                    except:
                        args["value"] = str(cmdargs[1])
                else:
                    args["value"] = str(cmdargs[1])
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] in ["jmp_if_700C_all_bits_clear", "jmp_if_700C_any_bits_set"]:
                if cmd["command"] == "jmp_if_700C_all_bits_clear":
                    cls = "A_JmpIf700CAllBitsClear"
                elif cmd["command"] == "jmp_if_700C_any_bits_set":
                    cls = "A_JmpIf700CAnyBitsSet"
                bits = cmdargs[0]
                args["bits"] = "%r" % bits
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "jmp_if_random_above_128":
                cls = "A_JmpIfRandom1of2"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_random_above_66":
                cls = "A_JmpIfRandom2of3"
                include_argnames = False
                args["destinations"] = "%r" % cmdargs
            elif cmd["command"] == "jmp_if_loaded_memory_is_0":
                cls = "A_JmpIfLoadedMemoryIs0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_not_0":
                cls = "A_JmpIfLoadedMemoryIsNot0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_comparison_result_is_greater_or_equal":
                cls = "A_JmpIfComparisonResultIsGreaterOrEqual"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_comparison_result_is_lesser":
                cls = "A_JmpIfComparisonResultIsLesser"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_below_0":
                cls = "A_JmpIfLoadedMemoryIsBelow0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "jmp_if_loaded_memory_is_above_or_equal_0":
                cls = "A_JmpIfLoadedMemoryIsAboveOrEqual0"
                include_argnames = False
                args["destinations"] = '["%s"]' % cmdargs[0]
            elif cmd["command"] == "pause":
                cls = "A_Pause"
                include_argnames = False
                args["length"] = str(cmdargs[0])
            elif cmd["command"] in [
                "summon_to_level",
                "remove_from_level",
                "enable_trigger_in_level",
                "disable_trigger_in_level",
            ]:
                if cmd["command"] == "summon_to_level":
                    cls = "A_SummonObjectToSpecificLevel"
                elif cmd["command"] == "remove_from_level":
                    cls = "A_RemoveObjectFromSpecificLevel"
                elif cmd["command"] == "enable_trigger_in_level":
                    cls = "A_EnableObjectTriggerInSpecificLevel"
                elif cmd["command"] == "disable_trigger_in_level":
                    cls = "A_DisableObjectTriggerInSpecificLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["level_id"] = varnames["rooms"][cmdargs[1]]
            elif cmd["command"] == "summon_object_at_70A8_to_current_level":
                cls = "A_SummonObjectAt70A8ToCurrentLevel"
            elif cmd["command"] == "remove_object_at_70A8_from_current_level":
                cls = "A_RemoveObjectAt70A8FromCurrentLevel"
            elif cmd["command"] == "enable_trigger_at_70A8":
                cls = "A_EnableTriggerOfObjectAt70A8InCurrentLevel"
            elif cmd["command"] == "disable_trigger_at_70A8":
                cls = "A_DisableTriggerOfObjectAt70A8InCurrentLevel"
            elif cmd["command"] in ["jmp_if_object_in_level", "jmp_if_object_not_in_level"]:
                if cmd["command"] == "jmp_if_object_in_level":
                    cls = "A_JmpIfObjectInSpecificLevel"
                elif cmd["command"] == "jmp_if_object_not_in_level":
                    cls = "A_JmpIfObjectNotInSpecificLevel"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["level_id"] = varnames["rooms"][cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] == "jmp_to_start_of_this_script":
                cls = "A_JmpToStartOfThisScript"
            elif cmd["command"] == "jmp_to_start_of_this_script_FA":
                cls = "A_JmpToStartOfThisScriptFA"
            elif cmd["command"] == "ret":
                cls = "A_ReturnQueue"
            elif cmd["command"] == "end_all":
                cls = "A_ReturnAll"
            elif cmd["command"] == "shadow_on":
                cls = "A_ShadowOn"
            elif cmd["command"] == "shadow_off":
                cls = "A_ShadowOff"
            elif cmd["command"] == "floating_on":
                cls = "A_FloatingOn"
            elif cmd["command"] == "floating_off":
                cls = "A_FloatingOff"
            elif cmd["command"] in ["object_memory_set_bit", "object_memory_clear_bit"]:
                if cmd["command"] == "object_memory_set_bit":
                    cls = "A_ObjectMemorySetBit"
                elif cmd["command"] == "object_memory_clear_bit":
                    cls = "A_ObjectMemoryClearBit"
                args["arg_1"] = f"0x{cmdargs[0]:02X}"
                bits = cmdargs[1]
                args["bits"] = "%r" % bits
            elif cmd["command"] == "object_memory_modify_bits":
                cls = "A_ObjectMemoryModifyBits"
                args["arg_1"] = f"0x{cmdargs[0]:02X}"
                set_flags = cmdargs[1]
                if len(set_flags) > 0:
                    args["set_bits"] = "%r" % set_flags
                clear_bits = cmdargs[2]
                if len(clear_bits) > 0:
                    args["clear_bits"] = "%r" % clear_bits
            elif cmd["command"] == "set_priority":
                cls = "A_SetPriority"
                include_argnames = False
                args["priority"] = str(cmdargs[0])
            elif cmd["command"] == "jmp_if_object_in_air":
                cls = "A_JmpIfObjectInAir"
                include_argnames = False
                args["object"] = AREA_OBJECTS[cmdargs[0]]
                args["destinations"] = '["%s"]' % cmdargs[1]
            elif cmd["command"] == "create_packet_at_7010_with_event":
                cls = "A_CreatePacketAt7010WithEvent"
                args["packet"] = varnames["packets"][cmdargs[0]]
                args["event_id"] = varnames["event_scripts"][cmdargs[1]]
                args["destinations"] = '["%s"]' % cmdargs[2]
            elif cmd["command"] in [
                "mem_700C_xor_const",
                "mem_700C_or_const",
                "mem_700C_and_const",
            ]:
                if cmd["command"] == "mem_700C_and_const":
                    cls = "A_Mem700CAndConst"
                elif cmd["command"] == "mem_700C_or_const":
                    cls = "A_Mem700COrConst"
                elif cmd["command"] == "mem_700C_xor_const":
                    cls = "A_Mem700CXorConst"
                include_argnames = False
                args["value"] = f"0x{cmdargs[0]:04X}"
            elif cmd["command"] in ["mem_700C_or_var", "mem_700C_and_var"]:
                if cmd["command"] == "mem_700C_and_var":
                    cls = "A_Mem700CAndVar"
                elif cmd["command"] == "mem_700C_or_var":
                    cls = "A_Mem700COrVar"
                elif cmd["command"] == "mem_700C_xor_var":
                    cls = "A_Mem700CXorVar"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
            elif cmd["command"] == "mem_700C_shift_left":
                cls = "A_VarShiftLeft"
                include_argnames = False
                args["address"] = vars_lookup.get(cmdargs[0])
                args["shift"] = str(cmdargs[1])
            elif cmd["command"] == "db":
                cls = "A_UnknownCommand"
                include_argnames = False
                args["args"] = "%r" % bytearray(cmdargs)
            else:
                raise Exception("%s not found" % cmd["command"])

            return cls, args, use_identifier, include_argnames

        def convert_script(script, valid_identifiers, converter):
            new_script = []

            for cmd in script:
                identifier = ""
                cls, args, use_identifier, include_argnames = converter(cmd, valid_identifiers)

                if cls is not None:
                    arg_strings = []
                    for key in args:
                        if include_argnames:
                            arg_strings.append("%s=%s" % (key, args[key]))
                        else:
                            arg_strings.append(args[key])
                    arg_string = ", ".join(
                        [f"{w}" if not isinstance(w, str) else w for w in arg_strings]
                    )

                    if use_identifier:
                        if len(arg_string) > 0:
                            arg_string += ", "
                        identifier = 'identifier="%s"' % cmd["identifier"]

                    output = "%s(%s%s)" % (cls, arg_string, identifier)
                    new_script.append(output)

            return new_script

        def produce_action_script(index, script, valid_identifiers):
            output = "#%s" % varnames["action_scripts"][index]
            output += (
                "\n\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *"
            output += (
                "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *"

            output += "\nfrom ....variables.action_script_names import *"
            output += "\nfrom ....variables.event_script_names import *"
            output += "\nfrom ....variables.overworld_sfx_names import *"
            output += "\nfrom ....variables.room_names import *"
            output += "\nfrom ....variables.variable_names import *"
            output += "\nfrom ....packets import *"
            output += "\nfrom ....items import *"
            output += "\n\nscript = ActionScript([\n\t"

            contents = convert_script(script, valid_identifiers, convert_action_script_command)
            output += ",\n\t".join(contents)

            output += "\n])"

            return output

        def produce_event_script(index, script, valid_identifiers):
            output = "# %s" % varnames["event_scripts"][index]
            output += (
                "\n\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *"
            output += (
                "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *"
            output += (
                "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *"
            output += (
                "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *"
            output += (
                "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *"
            )
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *"
            output += "\nfrom ....variables.action_script_names import *"
            output += "\nfrom ....variables.battlefield_names import *"
            output += "\nfrom ....variables.dialog_names import *"
            output += "\nfrom ....variables.event_script_names import *"
            output += "\nfrom ....variables.music_names import *"
            output += "\nfrom ....variables.overworld_area_names import *"
            output += "\nfrom ....variables.overworld_sfx_names import *"
            output += "\nfrom ....variables.pack_names import *"
            output += "\nfrom ....variables.room_names import *"
            output += "\nfrom ....variables.shop_names import *"
            output += "\nfrom ....variables.variable_names import *"
            output += "\nfrom ....items import *"
            output += "\nfrom ....packets import *"
            output += "\n\nscript = EventScript([\n\t"

            contents = convert_script(script, valid_identifiers, convert_event_script_command)
            output += ",\n\t".join(contents)

            output += "\n])"

            return output

        ajt = []
        ejt = []

        disassembler = EventDisassemblerCommand()
        e_scripts = disassembler.handle(rom=options["rom"])
        disassembler2 = AnimationDisassemblerCommand()
        a_scripts = disassembler2.handle(rom=options["rom"])

        output_path = "./src/disassembler_output/overworld_scripts"
        event_path = f"{output_path}/event/scripts"
        action_path = f"{output_path}/animation/scripts"
        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(event_path, exist_ok=True)
        os.makedirs(action_path, exist_ok=True)

        for i, script_dict in enumerate(a_scripts):
            for cmd in script_dict:
                if "args" in cmd:
                    ajt.extend([a for a in cmd["args"] if isinstance(a, str)])
            actions_jumped_to.extend(list(set(ajt)))

        for i, script_dict in enumerate(e_scripts):
            for cmd in script_dict:
                if "args" in cmd:
                    ejt.extend([a for a in cmd["args"] if isinstance(a, str)])
                if "subscript" in cmd:
                    for ccmd in cmd["subscript"]:
                        if "args" in ccmd:
                            ejt.extend([a for a in ccmd["args"] if isinstance(a, str)])
            events_jumped_to.extend(list(set(ejt)))

        for i, script in enumerate(a_scripts):
            output = produce_action_script(i, script, actions_jumped_to)
            file = open(f"{action_path}/script_{i}.py", "w")
            writeline(file, output)
            file.close()

        open(f"{output_path}/animation/__init__.py", "w")
        open(f"{action_path}/__init__.py", "w")
        file = open(f"{output_path}/animation/actionqueues.py", "w")
        output = "from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import ActionScriptBank"
        for i, script in enumerate(a_scripts):
            output += f"\nfrom .scripts.script_{i} import script as script_{i}"
        output += "\n\nactions = ActionScriptBank([\n"
        for i, script in enumerate(a_scripts):
            output += f"\tscript_{i},\n"
        output += "])"
        writeline(file, output)
        file.close()

        open(f"{output_path}/event/__init__.py", "w")
        open(f"{event_path}/__init__.py", "w")
        for i, script in enumerate(e_scripts):
            output = produce_event_script(i, script, events_jumped_to)
            file = open(f"{event_path}/script_{i}.py", "w")
            writeline(file, output)
            file.close()

        file = open(f"{output_path}/event/events.py", "w")
        output = "from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScriptController, EventScriptBank"
        for i, script in enumerate(e_scripts):
            output += f"\nfrom .scripts.script_{i} import script as script_{i}"
        output += "\n\nevents = EventScriptController([\n"
        output += "\tEventScriptBank(pointer_table_start=0x1E0000, start=0x1E0C00, end=0x1F0000, scripts=[\n"
        for i in range(0, 1536):
            output += f"\t\tscript_{i},\n"
        output += "\t]),\n"

        output += "\tEventScriptBank(pointer_table_start=0x1F0000, start=0x1F0C00, end=0x200000, scripts=[\n"
        for i in range(1536, 3072):
            output += f"\t\tscript_{i},\n"
        output += "\t]),\n"

        output += "\tEventScriptBank(pointer_table_start=0x200000, start=0x200800, end=0x20E000, scripts=[\n"
        for i in range(3072, 4096):
            output += f"\t\tscript_{i},\n"
        output += "\t])\n"

        output += "])"
        writeline(file, output)
        file.close()
