from django.core.management.base import BaseCommand
from delivery.models import Restaurant, Item

class Command(BaseCommand):
    help = 'Seed the database with realistic food data'

    def handle(self, *args, **options):
        # Clear existing data
        Restaurant.objects.all().delete()
        
        # Create restaurants with different cuisines
        restaurants = [
            {
                'name': 'Burger Palace',
                'picture': 'https://images.unsplash.com/photo-1568901346391-7c5b25a7e7b5?w=400',
                'cuisine': 'American, Burger, Fast Food',
                'rating': 4.5,
                'items': [
                    {'name': 'Classic Cheeseburger', 'description': 'Juicy beef patty with cheese, lettuce, tomato', 'price': 299, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1568901346391-7c5b25a7e7b5?w=300'},
                    {'name': 'Veggie Burger', 'description': 'Plant-based patty with fresh vegetables', 'price': 249, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1562967916-eb82221dfb46?w=300'},
                    {'name': 'BBQ Bacon Burger', 'description': 'Beef patty with crispy bacon and BBQ sauce', 'price': 399, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1562967916-eb82221dfb46?w=300'},
                ]
            },
            {
                'name': 'Pizza Heaven',
                'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
                'cuisine': 'Italian, Pizza',
                'rating': 4.7,
                'items': [
                    {'name': 'Margherita Pizza', 'description': 'Fresh mozzarella, tomato sauce, basil', 'price': 349, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Pepperoni Pizza', 'description': 'Classic pepperoni with mozzarella cheese', 'price': 449, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Farmhouse Pizza', 'description': 'Loaded with fresh vegetables and herbs', 'price': 499, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                ]
            },
            {
                'name': 'Biryani House',
                'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=400',
                'cuisine': 'Indian, Biryani, Mughlai',
                'rating': 4.8,
                'items': [
                    {'name': 'Chicken Biryani', 'description': 'Aromatic basmati rice with tender chicken', 'price': 399, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                    {'name': 'Veg Biryani', 'description': 'Fragrant rice with mixed vegetables', 'price': 299, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                    {'name': 'Mutton Biryani', 'description': 'Premium mutton pieces with special spices', 'price': 549, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                ]
            },
            {
                'name': 'South Indian Express',
                'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=400',
                'cuisine': 'South Indian, Dosa, Idli',
                'rating': 4.4,
                'items': [
                    {'name': 'Masala Dosa', 'description': 'Crispy dosa with potato filling', 'price': 199, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                    {'name': 'Idli Sambar', 'description': 'Soft steamed rice cakes with lentil soup', 'price': 149, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                    {'name': 'Uttapam', 'description': 'Thick pancake with vegetables', 'price': 249, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1589302166068-9a64e9c8c621?w=300'},
                ]
            },
            {
                'name': 'Chinese Wok',
                'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
                'cuisine': 'Chinese, Asian, Noodles',
                'rating': 4.3,
                'items': [
                    {'name': 'Hakka Noodles', 'description': 'Stir-fried noodles with vegetables', 'price': 279, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Chilli Chicken', 'description': 'Spicy chicken with bell peppers', 'price': 349, 'vegeterian': False, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Manchurian', 'description': 'Crispy vegetable balls in gravy', 'price': 299, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                ]
            },
            {
                'name': 'Dessert Paradise',
                'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
                'cuisine': 'Desserts, Bakery, Ice Cream',
                'rating': 4.6,
                'items': [
                    {'name': 'Chocolate Cake', 'description': 'Rich chocolate layer cake', 'price': 349, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Ice Cream Sundae', 'description': 'Vanilla ice cream with toppings', 'price': 199, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                    {'name': 'Gulab Jamun', 'description': 'Traditional Indian sweet', 'price': 149, 'vegeterian': True, 'picture': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300'},
                ]
            }
        ]
        
        created_restaurants = []
        for rest_data in restaurants:
            items_data = rest_data.pop('items')
            restaurant = Restaurant.objects.create(**rest_data)
            created_restaurants.append((restaurant, items_data))
            
        # Create items for each restaurant
        for restaurant, items_data in created_restaurants:
            for item_data in items_data:
                Item.objects.create(restaurant=restaurant, **item_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(restaurants)} restaurants with food items!')
        )
