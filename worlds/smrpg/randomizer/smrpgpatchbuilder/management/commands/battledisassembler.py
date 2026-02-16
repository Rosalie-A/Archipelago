"""Based on patcdr's original battle disassembler"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import shortify, writeline
from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_5",
    "UNKNOWN_6",
    "UNKNOWN_7",
    "UNKNOWN_8",
    "UNKNOWN_9",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "SLOT_1",
    "SLOT_2",
    "SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_EXCLUDING_SELF",
    "RANDOM_ALLY_EXCLUDING_SELF_OPPONENT_IF_SOLO",
    "ALL_ALLIES_AND_SELF",
    "RANDOM_ALLY_OR_SELF",
    "UNKNOWN_32",
    "UNKNOWN_33",
    "UNKNOWN_34",
    "ALL_OPPONENTS",
    "AT_LEAST_ONE_OPPONENT",
    "RANDOM_OPPONENT",
    "UNKNOWN_38",
    "AT_LEAST_ONE_ALLY",
    "MONSTER_1_CALL",
    "MONSTER_2_CALL",
    "MONSTER_3_CALL",
    "MONSTER_4_CALL",
    "MONSTER_5_CALL",
    "MONSTER_6_CALL",
    "MONSTER_7_CALL",
    "MONSTER_8_CALL",
]

COMMANDS = ["COMMAND_ATTACK", "COMMAND_SPECIAL", "COMMAND_ITEM"]

battle_lengths = [
    1,  # 00
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 10
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 20
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 30
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 40
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 50
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 60
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 70
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 80
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 90
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # a0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # b0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # c0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # d0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,  # e0
    0,
    2,
    2,
    0,
    2,
    3,
    4,
    2,
    0,
    4,
    3,
    1,
    2,
    0,
    2,
    4,  # f0
    2,
    3,
    3,
    4,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    4,
    1,
    1,
    1,
]

def tokenize(rom, start):
    dex = start
    ff_seen = False
    acc = []
    while True:
        cmd = rom[dex]
        if cmd == 0xFF:
            if ff_seen:
                break
            ff_seen = True
        l = battle_lengths[cmd]
        acc.append((rom[dex : dex + l], dex))
        dex += l
    return acc

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):
        varnames = load_arrays_from_input_files()
        classnames = load_class_names_from_config()

        VARIABLES = varnames["battle_vars"]
        ITEMS = classnames["all_items"]
        BATTLE_EVENTS = varnames["events"]
        SPELLS = [""] * 252
        SPELLS[251] = "DoNothing"
        for i, a in enumerate(classnames["all_spells"]):
            SPELLS[i] = a
        ATTACKS = [""] * 252
        ATTACKS[251] = "DoNothing"
        for i, a in enumerate(classnames["monster_attacks"]):
            ATTACKS[i] = a
        ENEMIES = classnames["enemies"]

        def pythonize(command):
            opcode = command[0]
            args = {}
            cls = None
            include_argnames = True

            match opcode:
                case 0xE0:
                    cls = "Attack"
                    args["attack_1"] = ATTACKS[command[1]]
                    args["attack_2"] = ATTACKS[command[2]]
                    args["attack_3"] = ATTACKS[command[3]]
                    include_argnames = False
                case 0xE2:
                    cls = "SetTarget"
                    args["target"] = TARGETS[command[1]]
                    include_argnames = False
                case 0xE3:
                    cls = "RunBattleDialog"
                    args["dialog_id"] = str(command[1])
                    include_argnames = False
                case 0xE5:
                    cls = "RunBattleEvent"
                    assert 0 <= command[1] <= 102
                    args["event_id"] = BATTLE_EVENTS[command[1]]
                    include_argnames = False
                case 0xE6:
                    match command[1]:
                        case 0x00:
                            cls = "IncreaseVarBy1"
                        case 0x01:
                            cls = "DecreaseVarBy1"
                        case _:
                            raise Exception("invalid byte")
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    include_argnames = False
                case 0xE7:
                    match command[1]:
                        case 0x00:
                            cls = "SetVarBits"
                        case 0x01:
                            cls = "ClearVarBits"
                        case _:
                            raise Exception("invalid byte")
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    bits = []
                    for i in range(0, 8):
                        comp = 1 << i
                        if command[3] & comp == comp:
                            bits.append(i)
                    args["bits"] = "%r" % bits
                    include_argnames = False
                case 0xE8:
                    cls = "ClearVar"
                    args["variable"] = VARIABLES[command[1] & 0x0F]
                    include_argnames = False
                case 0xEA:
                    match command[1]:
                        case 0x00:
                            cls = "RemoveTarget"
                        case 0x01:
                            cls = "CallTarget"
                        case _:
                            raise Exception("invalid byte")
                    args["target"] = TARGETS[command[3]]
                    include_argnames = False
                case 0xEB:
                    match command[1]:
                        case 0x00:
                            cls = "MakeInvulnerable"
                        case 0x01:
                            cls = "MakeVulnerable"
                        case _:
                            raise Exception("invalid byte")
                    args["target"] = TARGETS[command[2]]
                    include_argnames = False
                case 0xEC:
                    cls = "ExitBattle"
                case 0xED:
                    cls = "Set7EE005ToRandomNumber"
                    args["upper_bound"] = str(command[1])
                case 0xEF:
                    cls = "CastSpell"
                    args["spell_1"] = SPELLS[command[1]]
                    include_argnames = False
                case 0xF0:
                    cls = "CastSpell"
                    args["spell_1"] = SPELLS[command[1]]
                    args["spell_2"] = SPELLS[command[2]]
                    args["spell_3"] = SPELLS[command[3]]
                    include_argnames = False
                case 0xF1:
                    cls = "RunObjectSequence"
                    args["animation_id"] = str(command[1])
                    include_argnames = False
                case 0xF2:
                    match command[1]:
                        case 0x00:
                            cls = "SetUntargetable"
                        case 0x01:
                            cls = "SetTargetable"
                        case _:
                            raise Exception("invalid byte")
                    if command[2] == 0:
                        args["target"] = TARGETS[0x1B]
                    else:
                        args["target"] = TARGETS[command[2] + 0x12]
                    include_argnames = False
                case 0xF3:
                    match command[1]:
                        case 0x00:
                            cls = "EnableCommand"
                        case 0x01:
                            cls = "DisableCommand"
                        case _:
                            raise Exception("invalid byte")
                    commands_set = []
                    if command[2] & 0x01 == 0x01:
                        commands_set.append("COMMAND_ATTACK")
                    if command[2] & 0x02 == 0x02:
                        commands_set.append("COMMAND_SPECIAL")
                    if command[2] & 0x04 == 0x04:
                        commands_set.append("COMMAND_ITEM")
                    args["commands"] = "[%s]" % ", ".join(commands_set)
                    include_argnames = False
                case 0xF4:
                    match command[1]:
                        case 0x00:
                            cls = "RemoveAllInventory"
                        case 0x01:
                            cls = "RestoreInventory"
                        case _:
                            raise Exception("invalid byte")
                case 0xFB:
                    cls = "DoNothing"
                case 0xFC:
                    match command[1]:
                        case 0x01:
                            cls = "IfTargetedByCommand"
                            include_argnames = False
                            if command[2] == command[3]:
                                args["commands"] = "[%s]" % COMMANDS[command[2] - 2]
                            else:
                                args["commands"] = "[%s]" % ", ".join(
                                    COMMANDS[command[2] - 2], COMMANDS[command[3] - 2]
                                )
                        case 0x02:
                            cls = "IfTargetedBySpell"
                            include_argnames = False
                            nums = []
                            for a in command[2:]:
                                nums.append(a)
                            if nums[0] == nums[1]:
                                args["spells"] = "[%s]" % SPELLS[nums[0]]
                            else:
                                args["spells"] = "[%s]" % ", ".join(
                                    SPELLS[nums[0]], SPELLS[nums[1]]
                                )
                        case 0x03:
                            cls = "IfTargetedByItem"
                            include_argnames = False
                            nums = []
                            for a in command[2:]:
                                nums.append(a)
                            if nums[0] == nums[1]:
                                args["items"] = "[%s]" % ITEMS[nums[0]]
                            else:
                                args["items"] = "[%s]" % ", ".join(
                                    ITEMS[nums[0]], ITEMS[nums[1]]
                                )
                        case 0x04:
                            cls = "IfTargetedByElement"
                            include_argnames = False
                            elements = []
                            if command[2] & 0x10 == 0x10:
                                elements.append("Element.ICE")
                            if command[2] & 0x20 == 0x20:
                                elements.append("Element.THUNDER")
                            if command[2] & 0x40 == 0x40:
                                elements.append("Element.FIRE")
                            if command[2] & 0x80 == 0x80:
                                elements.append("Element.Jump")
                            args["elements"] = "[%s]" % ", ".join(elements)
                        case 0x05:
                            cls = "IfTargetedByRegularAttack"
                        case 0x06:
                            cls = "IfTargetHPBelow"
                            include_argnames = False
                            args["target"] = TARGETS[command[2]]
                            args["threshold"] = str(command[3] * 16)
                        case 0x07:
                            cls = "IfHPBelow"
                            include_argnames = False
                            args["threshold"] = str(shortify(command, 2))
                        case 0x08:
                            cls = "IfTargetAfflictedBy"
                            include_argnames = False
                            elements = []
                            args["target"] = TARGETS[command[2]]
                            if command[3] & 0x01 == 0x01:
                                elements.append("Status.MUTE")
                            if command[3] & (1 << 1) == (1 << 1):
                                elements.append("Status.SLEEP")
                            if command[3] & (1 << 2) == (1 << 2):
                                elements.append("Status.POISON")
                            if command[3] & (1 << 3) == (1 << 3):
                                elements.append("Status.FEAR")
                            if command[3] & (1 << 4) == (1 << 4):
                                elements.append("Status.BERSERK")
                            if command[3] & (1 << 5) == (1 << 5):
                                elements.append("Status.MUSHROOM")
                            if command[3] & (1 << 6) == (1 << 6):
                                elements.append("Status.SCARECROW")
                            if command[3] & (1 << 7) == (1 << 7):
                                elements.append("Status.INVINCIBLE")
                            args["statuses"] = "[%s]" % ", ".join(elements)
                        case 0x09:
                            cls = "IfTargetNotAfflictedBy"
                            include_argnames = False
                            elements = []
                            args["target"] = TARGETS[command[2]]
                            if command[3] & 0x01 == 0x01:
                                elements.append("Status.MUTE")
                            if command[3] & (1 << 1) == (1 << 1):
                                elements.append("Status.SLEEP")
                            if command[3] & (1 << 2) == (1 << 2):
                                elements.append("Status.POISON")
                            if command[3] & (1 << 3) == (1 << 3):
                                elements.append("Status.FEAR")
                            if command[3] & (1 << 4) == (1 << 4):
                                elements.append("Status.BERSERK")
                            if command[3] & (1 << 5) == (1 << 5):
                                elements.append("Status.MUSHROOM")
                            if command[3] & (1 << 6) == (1 << 6):
                                elements.append("Status.SCARECROW")
                            if command[3] & (1 << 7) == (1 << 7):
                                elements.append("Status.INVINCIBLE")
                            args["statuses"] = "[%s]" % ", ".join(elements)
                        case 0x0A:
                            cls = "IfTurnCounterEquals"
                            include_argnames = False
                            args["phase"] = str(command[2])
                        case 0x0C:
                            cls = "IfVarLessThan"
                            include_argnames = False
                            args["variable"] = VARIABLES[command[2] & 0x0F]
                            args["threshold"] = str(command[3])
                        case 0x0D:
                            cls = "IfVarEqualOrGreaterThan"
                            include_argnames = False
                            args["variable"] = VARIABLES[command[2] & 0x0F]
                            args["threshold"] = str(command[3])
                        case 0x10:
                            match command[2]:
                                case 0x00:
                                    cls = "IfTargetAlive"
                                case 0x01:
                                    cls = "IfTargetKOed"
                            include_argnames = False
                            args["target"] = TARGETS[command[3]]
                        case 0x11:
                            cls = "IfVarBitsSet"
                            include_argnames = False
                            args["variable"] = VARIABLES[command[2] & 0x0F]
                            bits = []
                            for i in range(0, 8):
                                comp = 1 << i
                                if command[3] & comp == comp:
                                    bits.append(i)
                            args["bits"] = "%r" % bits
                        case 0x12:
                            cls = "IfVarBitsClear"
                            include_argnames = False
                            args["variable"] = VARIABLES[command[2] & 0x0F]
                            bits = []
                            for i in range(0, 8):
                                comp = 1 << i
                                if command[3] & comp == comp:
                                    bits.append(i)
                            args["bits"] = "%r" % bits
                        case 0x13:
                            cls = "IfCurrentlyInFormationID"
                            include_argnames = False
                            args["formation_id"] = str(command[2] + (command[3] << 8))
                        case 0x14:
                            cls = "IfLastMonsterStanding"
                        case _:
                            raise Exception("invalid byte")
                case 0xFD:
                    cls = "Wait1Turn"
                case 0xFE:
                    cls = "Wait1TurnandRestartScript"
                case 0xFF:
                    cls = "StartCounterCommands"
                case _:
                    if battle_lengths[opcode] == 1 and (opcode <= 128 or opcode == 251):
                        cls = "Attack"
                        args["attack_1"] = ATTACKS[opcode]
                        include_argnames = False
                    else:
                        cls = "UnknownCommand"
                        args["bytes"] = "%r" % command
                        include_argnames = False
            arg_strings = []
            for key in args:
                if include_argnames:
                    arg_strings.append("%s=%s" % (key, args[key]))
                else:
                    arg_strings.append(args[key])
            arg_string = ", ".join(arg_strings)
            output = "%s(%s%s)" % (cls, arg_string, "")
            return output

        output_path = "./src/disassembler_output/monster_ai"

        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(f"{output_path}/scripts", exist_ok=True)
        open(f"{output_path}/__init__.py", "w")
        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        start = 0x390000
        for monster_id in range(256):
            ptr_location = start + 0x30AA + monster_id * 2
            ptr = shortify(rom, ptr_location)
            script_location = start + ptr
            script = tokenize(rom, script_location)

            output = "# %i - %s" % (monster_id, ENEMIES[monster_id])
            output += "\n\nfrom smrpgpatchbuilder.datatypes.monster_scripts import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.monster_scripts.commands import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing"
            output += "\nfrom ...variables.battle_event_names import *"
            output += "\nfrom ...variables.battle_variable_names import *"
            output += "\nfrom ...items.items import *"
            output += "\nfrom ...spells.spells import *"
            output += "\nfrom ...enemies.enemies import *"
            output += "\nfrom ...enemy_attacks.attacks import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.monster_scripts.arguments import *"
            output += "\n\nscript = MonsterScript([\n\t"

            output += ",\n\t".join([pythonize(entry[0]) for entry in script])

            output += "\n])"
            file = open(f"{output_path}/scripts/script_{monster_id}.py", "w")
            file.write(output)
            file.close()
        open(f"{output_path}/scripts/__init__.py", "w")
        open(f"{output_path}/__init__.py", "w")
        module = open(f"{output_path}/monster_scripts.py", "w")
        writeline(
            module,
            f"from smrpgpatchbuilder.datatypes.monster_scripts.types import MonsterScriptBank",
        )
        for monster_id in range(256):
            writeline(
                module,
                f"from .scripts.script_{monster_id} import script as script_{monster_id}",
            )
        writeline(module, "monster_scripts = MonsterScriptBank([")
        for monster_id in range(256):
            writeline(module, f"\tscript_{monster_id},")
        writeline(module, "])")
        module.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled 256 monster AI scripts to ./src/disassembler_output/monster_ai/"
            )
        )
