# MealBuddy - Food Delivery Web App

A modern, production-ready food delivery application built with Django and styled with Tailwind CSS, inspired by Zomato/Swiggy.

## 🚀 Features

- **Modern UI/UX**: Beautiful, responsive design with Tailwind CSS
- **Complete Order Flow**: Browse → Add to Cart → Checkout → Payment → Order Success
- **Restaurant Management**: Multiple restaurants with different cuisines
- **Realistic Food Data**: 15+ food items with high-quality images
- **Location Detection**: Geolocation API integration
- **Payment Integration**: Razorpay payment gateway (mock mode)
- **Professional UI States**: Loading spinners, toast notifications, empty states
- **Mobile Responsive**: Works perfectly on all device sizes

## 📋 Prerequisites

- Python 3.8+
- pip package manager

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd FinalMealmate-main/FinalMealmate-main
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Food Data
```bash
python manage.py seed_data
```

### 5. Create Test User (Optional)
```bash
python manage.py shell
```
Then run:
```python
from delivery.models import Customer
Customer.objects.create(username='testuser', password='test123', email='test@example.com', mobile='9999999999', address='Test Address')
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The app will be available at: **http://127.0.0.1:8000/**

## 🧪 Testing the App

### Test User Credentials
- **Username**: testuser
- **Password**: test123

### Complete Order Flow Test
1. **Homepage**: Browse restaurants and food categories
2. **Sign In**: Use test credentials or create new account
3. **Browse Restaurants**: View all available restaurants
4. **View Menu**: Click on any restaurant to see food items
5. **Add to Cart**: Add items to cart (shows success notification)
6. **View Cart**: Review cart items with price breakdown
7. **Checkout**: Enter delivery details and choose payment method
8. **Payment**: Mock Razorpay payment or Cash on Delivery
9. **Order Success**: Beautiful confirmation page with tracking

## 🏗️ Project Structure

```
FinalMealmate-main/
├── meal_buddy/           # Django project settings
├── delivery/            # Main app
│   ├── models.py        # Database models (Customer, Restaurant, Item, Cart)
│   ├── views.py         # Business logic and views
│   ├── urls.py          # URL routing
│   ├── templates/       # HTML templates
│   └── management/      # Django management commands
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🎨 UI Features

- **Modern Design**: Clean, professional interface inspired by Zomato
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Hover effects, transitions, and micro-interactions
- **Toast Notifications**: User-friendly feedback system
- **Loading States**: Professional loading spinners
- **Empty States**: Helpful messages when no data is available
- **Location Features**: City selection with geolocation support

## 📱 Pages & Features

### Homepage
- Hero section with call-to-action
- Cuisine categories (Pizza, Burger, Biryani, etc.)
- Popular restaurants showcase
- Special offers and promotions
- Why choose us section

### Restaurant Listing
- Filter by cuisine, rating, price
- Search functionality
- Sort options
- Restaurant cards with ratings and delivery time

### Menu Page
- Restaurant header with image and details
- Food item cards with images
- Veg/Non-veg indicators
- Add to cart functionality
- Fixed cart summary bar

### Cart Page
- Item management (quantity, remove)
- Price breakdown (subtotal, delivery, taxes)
- Order summary
- Checkout button

### Checkout Page
- Delivery address form
- Order items review
- Payment method selection
- Razorpay integration

### Order Success
- Confirmation message
- Order details
- Delivery tracking
- Continue shopping options

## 🔧 Technical Features

- **Backend**: Django 6.0.3 with SQLite
- **Frontend**: Tailwind CSS for styling
- **Database**: SQLite with Django ORM
- **Payment**: Razorpay integration (test mode)
- **Images**: Unsplash API for high-quality food photos
- **Icons**: Heroicons and emoji for UI elements
- **Fonts**: Google Fonts (Poppins)

## 🚀 Deployment Notes

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL/MySQL instead of SQLite
4. Set up production web server (Gunicorn + Nginx)
5. Configure environment variables for sensitive data
6. Use production Razorpay keys

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For any questions or issues, please create an issue in the repository.

---

**Happy Coding! 🍕🍔🍛**
