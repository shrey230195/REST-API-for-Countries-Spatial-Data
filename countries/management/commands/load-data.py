# your_app/management/commands/maybe_init_data.py

from django.core.management import call_command
from django.core.management.base import BaseCommand

from countries.models import Countries

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Checking initial data')
        if not Countries.objects.exists():
            self.stdout.write('Seeding initial data')
            call_command('loaddata', 'data/db.json')