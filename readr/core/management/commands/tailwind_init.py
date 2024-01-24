# your_app/management/commands/tailwind_init.py

from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Initialize Tailwind CSS'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Initializing Tailwind CSS...'))
        subprocess.run(['npx', 'tailwindcss', 'init'])
        self.stdout.write(self.style.SUCCESS('Tailwind CSS initialized successfully.'))
