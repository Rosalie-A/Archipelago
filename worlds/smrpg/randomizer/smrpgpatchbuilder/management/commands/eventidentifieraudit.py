from django.core.management.base import BaseCommand
from randomizer.logic.enscript import EventScript
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.eventscripts.events import scripts

class Command(BaseCommand):
    def handle(self, *args, **options):
        EventScript.audit_identifiers(scripts)
