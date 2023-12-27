# populate_db.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Item

def populate():
    items_data = [
        {'name': 'Елемент 1'},
        {'name': 'Елемент 2'},
        {'name': 'Елемент 3'},
        # Додайте більше елементів, якщо потрібно
    ]

    for item_data in items_data:
        Item.objects.create(**item_data)

if __name__ == '__main__':
    populate()
