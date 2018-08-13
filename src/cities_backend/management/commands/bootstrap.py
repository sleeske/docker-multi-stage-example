from cities.models import City
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('collectstatic', interactive=False)
        call_command('migrate', interactive=False)
        if not City.objects.first():
            call_command('cities')
