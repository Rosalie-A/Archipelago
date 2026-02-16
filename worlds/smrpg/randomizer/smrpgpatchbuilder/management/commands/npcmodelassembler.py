from django.core.management.base import BaseCommand
from randomizer.logic.npcmodel import NPCModels
from randomizer.data.npcmodels import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = NPCModels.assemble_from_table(models)

        #print("length:", hex(len(b)))

        f = open(f'write_to_0x1DB800.img', 'wb')

        f.write(b)
        f.close()

        self.stdout.write(self.style.SUCCESS("successfully assembled npc model data to write_to_0x1db800.img"))
