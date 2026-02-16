from django.core.management.base import BaseCommand
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.actionscripts.actions import scripts

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = OSCommand.assemble_from_table(scripts)

        print("combined length", hex(len(b)), len(b))

        f = open(f'write_to_0x210000.img', 'wb')
        f.write(b)
        f.close()
