"""
Combined Django management command to run all assemblers.

This command orchestrates the complete assembly process by running all
assemblers with the same output options.
"""

from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = "Run all assemblers with the same options"

    def add_arguments(self, parser):
        parser.add_argument(
            "-t", "--text",
            action='store_true',
            dest="text",
            help="Output as plain text files"
        )
        parser.add_argument(
            "-b", "--bin",
            action='store_true',
            dest="bin",
            help="Output as flexhex-compatible img files"
        )
        parser.add_argument(
            "-r", "--rom",
            dest="rom",
            help="Path to ROM for BPS patch generation"
        )

    def handle(self, *args, **options):
        # Extract options
        output_text = options.get("text", False)
        output_bin = options.get("bin", False)
        rom_path = options.get("rom")

        self.stdout.write(self.style.WARNING("=" * 80))
        self.stdout.write(self.style.WARNING("Starting combo assembly process..."))
        self.stdout.write(self.style.WARNING("=" * 80))

        # Prepare arguments for assemblers
        assembler_args = {}
        if output_text:
            assembler_args["text"] = True
        if output_bin:
            assembler_args["bin"] = True
        if rom_path:
            assembler_args["rom"] = rom_path

        # ========== STAGE 1: Ally Assembler ==========
        self.stdout.write(self.style.WARNING("\n[1/15] Running allyassembler..."))
        try:
            from .allyassembler import Command as AllyAssemblerCommand
            cmd = AllyAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ allyassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ allyassembler failed: {e}"))
            raise

        # ========== STAGE 2: Animation Assembler ==========
        self.stdout.write(self.style.WARNING("\n[2/15] Running animationassembler..."))
        try:
            from .animationassembler import Command as AnimationAssemblerCommand
            cmd = AnimationAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ animationassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ animationassembler failed: {e}"))
            raise

        # ========== STAGE 3: Battle Assembler ==========
        self.stdout.write(self.style.WARNING("\n[3/15] Running battleassembler..."))
        try:
            from .battleassembler import Command as BattleAssemblerCommand
            cmd = BattleAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ battleassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ battleassembler failed: {e}"))
            raise

        # ========== STAGE 4: Battle Dialog Assembler ==========
        self.stdout.write(self.style.WARNING("\n[4/15] Running battledialogassembler..."))
        try:
            from .battledialogassembler import Command as BattleDialogAssemblerCommand
            cmd = BattleDialogAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ battledialogassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ battledialogassembler failed: {e}"))
            raise

        # ========== STAGE 5: Dialog Assembler ==========
        self.stdout.write(self.style.WARNING("\n[5/15] Running dialogassembler..."))
        try:
            from .dialogassembler import Command as DialogAssemblerCommand
            cmd = DialogAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ dialogassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ dialogassembler failed: {e}"))
            raise

        # ========== STAGE 6: Enemy Assembler ==========
        self.stdout.write(self.style.WARNING("\n[6/15] Running enemyassembler..."))
        try:
            from .enemyassembler import Command as EnemyAssemblerCommand
            cmd = EnemyAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ enemyassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ enemyassembler failed: {e}"))
            raise

        # ========== STAGE 7: Enemy Attack Assembler ==========
        self.stdout.write(self.style.WARNING("\n[7/15] Running enemyattackassembler..."))
        try:
            from .enemyattackassembler import Command as EnemyAttackAssemblerCommand
            cmd = EnemyAttackAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ enemyattackassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ enemyattackassembler failed: {e}"))
            raise

        # ========== STAGE 8: Event Assembler ==========
        self.stdout.write(self.style.WARNING("\n[8/15] Running eventassembler..."))
        try:
            from .eventassembler import Command as EventAssemblerCommand
            cmd = EventAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ eventassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ eventassembler failed: {e}"))
            raise

        # ========== STAGE 9: Graphics Assembler ==========
        self.stdout.write(self.style.WARNING("\n[9/15] Running graphicsassembler..."))
        try:
            from .graphicsassembler import Command as GraphicsAssemblerCommand
            cmd = GraphicsAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ graphicsassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ graphicsassembler failed: {e}"))
            raise

        # ========== STAGE 10: Item Assembler ==========
        self.stdout.write(self.style.WARNING("\n[10/15] Running itemassembler..."))
        try:
            from .itemassembler import Command as ItemAssemblerCommand
            cmd = ItemAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ itemassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ itemassembler failed: {e}"))
            raise

        # ========== STAGE 11: Pack Assembler ==========
        self.stdout.write(self.style.WARNING("\n[11/15] Running packassembler..."))
        try:
            from .packassembler import Command as PackAssemblerCommand
            cmd = PackAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ packassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ packassembler failed: {e}"))
            raise

        # ========== STAGE 12: Room Assembler ==========
        self.stdout.write(self.style.WARNING("\n[12/15] Running roomassembler..."))
        try:
            from .roomassembler import Command as RoomAssemblerCommand
            cmd = RoomAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ roomassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ roomassembler failed: {e}"))
            raise

        # ========== STAGE 13: Shop Assembler ==========
        self.stdout.write(self.style.WARNING("\n[13/15] Running shopassembler..."))
        try:
            from .shopassembler import Command as ShopAssemblerCommand
            cmd = ShopAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ shopassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ shopassembler failed: {e}"))
            raise

        # ========== STAGE 14: Spell Assembler ==========
        self.stdout.write(self.style.WARNING("\n[14/15] Running spellassembler..."))
        try:
            from .spellassembler import Command as SpellAssemblerCommand
            cmd = SpellAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ spellassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ spellassembler failed: {e}"))
            raise

        # ========== STAGE 15: World Map Location Assembler ==========
        self.stdout.write(self.style.WARNING("\n[15/15] Running worldmaplocationassembler..."))
        try:
            from .worldmaplocationassembler import Command as WorldMapLocationAssemblerCommand
            cmd = WorldMapLocationAssemblerCommand()
            cmd.handle(**assembler_args)
            self.stdout.write(self.style.SUCCESS("  ✓ worldmaplocationassembler completed"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  ✗ worldmaplocationassembler failed: {e}"))
            raise

        # ========== Done ==========
        self.stdout.write(self.style.SUCCESS("\n" + "=" * 80))
        self.stdout.write(self.style.SUCCESS("All assemblers completed successfully!"))
        self.stdout.write(self.style.SUCCESS("=" * 80))
