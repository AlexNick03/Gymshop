import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymshop.settings')  # sau cum se numește modulul tău settings

django.setup()

with open('dump.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', stdout=f)
