import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymshop.settings')
django.setup()

from products.models import Product, Category
from django.contrib.auth.models import User

with open('dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Încarcă categoriile
for cat in data.get('categories', []):
    category = Category(
        title=cat['title'],
        image=cat.get('image', '')
    )
    category.save()

# Încarcă produsele
for prod in data.get('products', []):
    # Găsește categoria (presupunând că există)
    category = Category.objects.get(id=prod['category_id'])
    product = Product(
        title=prod['title'],
        price=prod['price'],
        category=category
    )
    product.save()

# Încarcă utilizatorii
for user_data in data.get('users', []):
    User.objects.create_user(
        username=user_data['username'],
        email=user_data.get('email', ''),
        password='parola_default123'  # schimba dacă vrei
    )

print("Toate datele au fost încărcate cu succes!")