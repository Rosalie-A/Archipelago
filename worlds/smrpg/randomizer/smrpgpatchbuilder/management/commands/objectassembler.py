from django.core.management.base import BaseCommand
from randomizer.logic.roomobject import RoomObjects
from randomizer.data.roomobjects.roomobjects import rooms

class Command(BaseCommand):
    def handle(self, *args, **options):
        npcs, eventtiles, exits, partitions = RoomObjects.assemble_from_table(rooms)

        allnpcbytes = npcs[0] + npcs[1]
        print("combined length", hex(len(allnpcbytes)), len(allnpcbytes))

        f = open(f'write_to_0x148000.img', 'wb')
        f.write(allnpcbytes)
        f.close()

        alleventbytes = eventtiles[0] + eventtiles[1]
        print("combined length", hex(len(alleventbytes)), len(alleventbytes))

        f = open(f'write_to_0x20E000.img', 'wb')
        f.write(alleventbytes)
        f.close()

        allexitbytes = exits[0] + exits[1]
        print("combined length", hex(len(allexitbytes)), len(allexitbytes))

        f = open(f'write_to_0x1D2D64.img', 'wb')
        f.write(allexitbytes)
        f.close()

        f = open(f'write_to_0x1DDE00.img', 'wb')
        f.write(partitions)
        f.close()

        self.stdout.write(self.style.SUCCESS("successfully assembled room objects"))