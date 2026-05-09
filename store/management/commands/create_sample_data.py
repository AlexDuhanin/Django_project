from django.core.management.base import BaseCommand
from store.models import Category, Product
import random

class Command(BaseCommand):
    help = 'Создаёт тестовые данные для моделей Category и Product'

    def handle(self, *args, **options):
        # Создаём категории
        categories_data = [
            {'name': 'Электроника', 'description': 'Электронные устройства и гаджеты'},
            {'name': 'Одежда', 'description': 'Одежда и аксессуары'},
            {'name': 'Книги', 'description': 'Художественная и научная литература'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Создана категория: {category.name}')
            else:
                self.stdout.write(f'Категория уже существует: {category.name}')

        # Создаём товары
        product_names = [
            'Смартфон', 'Ноутбук', 'Футболка', 'Джинсы', 'Роман', 'Учебник',
            'Планшет', 'Наушники', 'Куртка', 'Брюки', 'Детектив', 'Энциклопедия'
        ]

        products_created = 0
        for name in product_names:
            product = Product.objects.create(
                name=name,
                description=f'Описание для {name}',
                price=round(random.uniform(100, 5000), 2),
                category=random.choice(categories)
            )
            products_created += 1
            self.stdout.write(f'Создан товар: {product.name} ({product.price} руб.)')

        self.stdout.write(
            self.style.SUCCESS(
                f'Успешно создано: {len(categories)} категорий и {products_created} товаров'
            )
        )
