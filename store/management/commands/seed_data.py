from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Product


PHONES = [
    ('Aster One 5G', 'Everyday', 'Aster', '128 GB', '6.5” AMOLED', '5000 mAh', 'Balanced performance, all-day battery and a bright display for the moments that matter.', 17999, 18),
    ('Mira Pro 5G', 'Camera', 'Mira', '256 GB', '6.7” OLED', '4700 mAh', 'A camera-focused phone with generous storage and a vivid edge-to-edge screen.', 34999, 13),
    ('Helio X', 'Performance', 'Helio', '256 GB', '6.8” 120 Hz AMOLED', '5500 mAh', 'Smooth gaming, responsive multitasking and power for a full day of use.', 39999, 11),
    ('Solis Mini', 'Compact', 'Solis', '128 GB', '6.1” OLED', '4300 mAh', 'A comfortable one-hand phone with capable performance and refined details.', 27999, 22),
    ('Vanta Ultra', 'Premium', 'Vanta', '512 GB', '6.9” LTPO OLED', '5100 mAh', 'An expansive display, excellent storage and a polished flagship feel.', 69999, 7),
    ('Nova Fold', 'Foldable', 'Nova', '512 GB', '7.8” foldable OLED', '4800 mAh', 'A pocketable foldable built for reading, creating and doing more on the move.', 94999, 5),
]


class Command(BaseCommand):
    help = 'Add the fictional PocketWave phone catalog for local demos'

    def handle(self, *args, **kwargs):
        for name, category, brand, storage, display, battery, description, price, stock in PHONES:
            slug = slugify(name)
            Product.objects.update_or_create(slug=slug, defaults={
                'name': name, 'category': category, 'brand': brand,
                'storage': storage, 'display': display, 'battery': battery,
                'description': description, 'price': price, 'stock': stock,
                'image_asset': f'img/products/{slug}.svg', 'image_url': '',
                'is_active': True,
            })
        self.stdout.write(self.style.SUCCESS(f'{len(PHONES)} PocketWave phones are ready.'))
