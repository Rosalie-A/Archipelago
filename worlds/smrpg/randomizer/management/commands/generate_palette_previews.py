"""Django management command to generate ally palette preview images.

Usage:
    python manage.py generate_palette_previews

This command generates preview images for all ally character palettes,
showing what each character looks like with that palette applied.
"""

import os
from django.core.management.base import BaseCommand
from randomizer.utils.sprite_renderer import generate_ally_palette_preview
from randomizer.data.allies.palettes import mario, mallow, geno, bowser, toadstool
from pathlib import Path


# Mapping of character name to (sprite_id, module, output_dir)
ALLY_CONFIG = {
    'mario': {
        'sprite_id': 0,
        'module': mario,
        'output_dir': 'mario',
    },
    'toadstool': {
        'sprite_id': 7,
        'module': toadstool,
        'output_dir': 'toadstool',
    },
    'bowser': {
        'sprite_id': 13,
        'module': bowser,
        'output_dir': 'bowser',
    },
    'mallow': {
        'sprite_id': 19,
        'module': mallow,
        'output_dir': 'mallow',
    },
    'geno': {
        'sprite_id': 25,
        'module': geno,
        'output_dir': 'geno',
    },
}


class Command(BaseCommand):
    help = 'Generate preview images for all ally character palettes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--character',
            type=str,
            choices=['mario', 'toadstool', 'bowser', 'mallow', 'geno'],
            help='Generate previews for a specific character only',
        )
        parser.add_argument(
            '--scale',
            type=int,
            default=3,
            help='Scale factor for output images (default: 3)',
        )

    def handle(self, *args, **options):
        character_filter = options.get('character')
        scale = options.get('scale')

        # Base output directory in static files
        base_output_dir = Path(__file__).parent.parent.parent.parent / 'randomizer' / 'static' / 'randomizer' / 'images' / 'palette_previews'
        base_output_dir.mkdir(parents=True, exist_ok=True)

        # Determine which characters to process
        characters_to_process = [character_filter] if character_filter else ALLY_CONFIG.keys()

        total_generated = 0
        for char_name in characters_to_process:
            config = ALLY_CONFIG[char_name]
            sprite_id = config['sprite_id']
            module = config['module']
            char_output_dir = base_output_dir / config['output_dir']
            char_output_dir.mkdir(exist_ok=True)

            self.stdout.write(f"Generating previews for {char_name}...")

            # Find all palette classes in the module
            palette_classes = []
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                # Check if it's a class and has the required attributes
                if (isinstance(attr, type) and
                    hasattr(attr, 'colours') and
                    hasattr(attr, 'id') and
                    hasattr(attr, 'name') and
                    attr_name not in ['MarioPalette', 'MallowPalette', 'GenoPalette', 'BowserPalette', 'ToadstoolPalette']):
                    palette_classes.append(attr)

            # Generate preview for each palette
            for palette_class in palette_classes:
                # Skip "Default" and "Random" palettes, and base palette classes with no ID
                if palette_class.name in ['Default', 'Random'] or palette_class.id is None:
                    continue

                # Generate safe filename from palette ID (unique enum value)
                # Use ID instead of name since names don't have to be unique
                safe_id = str(palette_class.id).lower().replace(' ', '_').replace("'", '')
                output_path = char_output_dir / f'{safe_id}.png'

                try:
                    generate_ally_palette_preview(
                        sprite_id=sprite_id,
                        palette_class=palette_class,
                        output_path=str(output_path),
                        mold_index=0,
                        scale=scale
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f"  ✓ Generated: {output_path.relative_to(base_output_dir)}")
                    )
                    total_generated += 1
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"  ✗ Failed to generate {palette_class.name}: {e}")
                    )

        self.stdout.write(
            self.style.SUCCESS(f"\nTotal previews generated: {total_generated}")
        )
