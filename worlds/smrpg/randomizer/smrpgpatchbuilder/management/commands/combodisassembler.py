"""
Combined Django management command to run all disassemblers in sequence.

This command orchestrates the complete disassembly process by running multiple
disassemblers in the proper order to ensure dependencies are resolved.
"""

from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = "Run all disassemblers in proper sequence"

    def add_arguments(self, parser):
        parser.add_argument(
            "-r",
            "--rom",
            dest="rom",
            required=True,
            help="Path to a Mario RPG ROM file",
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]

        self.stdout.write(self.style.WARNING("=" * 80))
        self.stdout.write(self.style.WARNING("Starting combo disassembly process..."))
        self.stdout.write(self.style.WARNING("=" * 80))

        # ========== STAGE 1: Variable Parser ==========
        self.stdout.write(self.style.WARNING("\n[1/16] Running variableparser..."))
        try:
            from .variableparser import Command as VariableParserCommand
            cmd = VariableParserCommand()
            cmd.handle()
            self.stdout.write(self.style.SUCCESS("  ✓ variableparser completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ variableparser failed: {e}"))
            raise

        # ========== STAGE 2: Item Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[2/16] Running itemdisassembler..."))
        try:
            from .itemdisassembler import Command as ItemDisassemblerCommand
            cmd = ItemDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ itemdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ itemdisassembler failed: {e}"))
            raise

        # ========== STAGE 3: Enemy Attack Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[3/16] Running enemyattackdisassembler..."))
        try:
            from .enemyattackdisassembler import Command as EnemyAttackDisassemblerCommand
            cmd = EnemyAttackDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ enemyattackdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ enemyattackdisassembler failed: {e}"))
            raise

        # ========== STAGE 4: Spell Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[4/16] Running spelldisassembler..."))
        try:
            from .spelldisassembler import Command as SpellDisassemblerCommand
            cmd = SpellDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ spelldisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ spelldisassembler failed: {e}"))
            raise

        # ========== STAGE 5: Packet Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[5/16] Running packetdisassembler..."))
        try:
            from .packetdisassembler import Command as PacketDisassemblerCommand
            cmd = PacketDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ packetdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ packetdisassembler failed: {e}"))
            raise

        # ========== STAGE 6: Combined Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[6/16] Running combined_disassembler..."))
        try:
            from .combined_disassembler import Command as CombinedDisassemblerCommand
            cmd = CombinedDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ combined_disassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ combined_disassembler failed: {e}"))
            raise

        # ========== STAGE 7: Event Converter ==========
        self.stdout.write(self.style.WARNING("\n[7/16] Running eventconverter..."))
        try:
            from .eventconverter import Command as EventConverterCommand
            cmd = EventConverterCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ eventconverter completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ eventconverter failed: {e}"))
            raise

        # ========== STAGE 8: Battle Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[8/16] Running battledisassembler..."))
        try:
            from .battledisassembler import Command as BattleDisassemblerCommand
            cmd = BattleDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ battledisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ battledisassembler failed: {e}"))
            raise

        # ========== STAGE 9: Ally Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[9/16] Running allydisassembler..."))
        try:
            from .allydisassembler import Command as AllyDisassemblerCommand
            cmd = AllyDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ allydisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ allydisassembler failed: {e}"))
            raise

        # ========== STAGE 10: Graphics Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[10/16] Running graphicsdisassembler..."))
        try:
            from .graphicsdisassembler import Command as GraphicsDisassemblerCommand
            cmd = GraphicsDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ graphicsdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ graphicsdisassembler failed: {e}"))
            raise

        # ========== STAGE 11: Shop Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[11/16] Running shopdisassembler..."))
        try:
            from .shopdisassembler import Command as ShopDisassemblerCommand
            cmd = ShopDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ shopdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ shopdisassembler failed: {e}"))
            raise

        # ========== STAGE 12: Dialog Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[12/16] Running dialogdisassembler..."))
        try:
            from .dialogdisassembler import Command as DialogDisassemblerCommand
            cmd = DialogDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ dialogdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ dialogdisassembler failed: {e}"))
            raise

        # ========== STAGE 13: Battle Dialog Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[13/16] Running battledialogdisassembler..."))
        try:
            from .battledialogdisassembler import Command as BattleDialogDisassemblerCommand
            cmd = BattleDialogDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ battledialogdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ battledialogdisassembler failed: {e}"))
            raise

        # ========== STAGE 14: Pack Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[14/16] Running packdisassembler..."))
        try:
            from .packdisassembler import Command as PackDisassemblerCommand
            cmd = PackDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ packdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ packdisassembler failed: {e}"))
            raise

        # ========== STAGE 15: Room Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[15/16] Running roomdisassembler..."))
        try:
            from .roomdisassembler import Command as RoomDisassemblerCommand
            cmd = RoomDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ roomdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ roomdisassembler failed: {e}"))
            raise

        # ========== STAGE 16: World Map Location Disassembler ==========
        self.stdout.write(self.style.WARNING("\n[16/16] Running worldmaplocationdisassembler..."))
        try:
            from .worldmaplocationdisassembler import Command as WorldMapLocationDisassemblerCommand
            cmd = WorldMapLocationDisassemblerCommand()
            cmd.handle(rom=rom_path)
            self.stdout.write(self.style.SUCCESS("  ✓ worldmaplocationdisassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ worldmaplocationdisassembler failed: {e}"))
            raise

        # ========== Done ==========
        self.stdout.write(self.style.SUCCESS("\n" + "=" * 80))
        self.stdout.write(self.style.SUCCESS("All disassemblers completed successfully!"))
        self.stdout.write(self.style.SUCCESS("=" * 80))
