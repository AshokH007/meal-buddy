# 🚀 Deploy MealBuddy to Vercel

This guide will help you deploy the Django food delivery app to Vercel for a live link.

## 📋 Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: For version control (recommended)
3. **Vercel CLI**: Install globally
   ```bash
   npm i -g vercel
   ```

## 🔧 Deployment Steps

### 1. Initialize Git Repository
```bash
cd FinalMealmate-main/FinalMealmate-main
git init
git add .
git commit -m "Initial commit - Django food delivery app"
```

### 2. Push to GitHub
```bash
# Create a new repository on GitHub first
git remote add origin https://github.com/yourusername/mealmate-django.git
git push -u origin main
```

### 3. Deploy to Vercel

#### Option A: Using Vercel CLI
```bash
# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Set up and deploy "~/project"
# - Which scope do you want to deploy to? (Your account)
# - Link to existing project? [y/N] (N for new project)
# - What's your project's name? (mealmate-django)
# - In which directory is your code located? (./)
# - Want to override the settings? [y/N] (N)
```

#### Option B: Using Vercel Dashboard
1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click "Add New..." → "Project"
3. Import your GitHub repository
4. Vercel will auto-detect Django framework
5. Click "Deploy"

### 4. Environment Variables
In Vercel dashboard, add these environment variables:

```
DJANGO_SETTINGS_MODULE=meal_buddy.settings
DJANGO_DEBUG=False
SECRET_KEY=your-secure-secret-key-here-change-this
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
```

### 5. Database Setup (Important!)
Since Vercel is serverless, SQLite won't work persistently. You have two options:

#### Option A: Use PostgreSQL (Recommended)
1. Sign up for [Neon](https://neon.tech) or [Supabase](https://supabase.com)
2. Get database URL
3. Add to Vercel environment variables:
   ```
   DATABASE_URL=postgresql://user:password@host:port/database
   ```
4. Update `settings.py` to use PostgreSQL

#### Option B: Use SQLite (Demo Only)
For demo purposes, the app will work with SQLite but data will reset on each deployment.

## 🗂️ Project Structure for Vercel

```
FinalMealmate-main/
├── api/
│   └── index.py          # Vercel serverless handler
├── delivery/             # Django app
├── meal_buddy/           # Django project
├── vercel.json          # Vercel configuration
├── requirements.txt      # Python dependencies
├── package.json         # Node.js metadata
└── manage.py           # Django management
```

## 🔍 Configuration Files Explained

### `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ],
  "env": {
    "DJANGO_SETTINGS_MODULE": "meal_buddy.settings",
    "DJANGO_DEBUG": "False"
  }
}
```

### `api/index.py`
- Handles Vercel serverless function requests
- Converts Vercel requests to Django WSGI format
- Routes all requests to Django app

## 🚨 Important Notes

### Static Files
Static files are served through Django's static file system in production.

### Database Persistence
- SQLite: Data resets on each deployment (good for demos)
- PostgreSQL: Persistent data (recommended for production)

### Performance
- Cold starts may take 2-3 seconds
- Subsequent requests are fast
- Perfect for food delivery demo

### Costs
- Vercel Hobby tier: Free
- Database: Neon/Supabase free tier available

## 🎯 After Deployment

1. **Test the Live App**: Visit your Vercel URL
2. **Create Test User**: Use signup page
3. **Test Order Flow**: Browse → Add to Cart → Checkout
4. **Share Link**: Your app is now live! 🎉

## 🔧 Troubleshooting

### Common Issues

1. **Build Errors**
   - Check Python version compatibility
   - Verify all dependencies in requirements.txt

2. **Runtime Errors**
   - Check environment variables
   - Verify database connection

3. **Static Files Not Loading**
   - Ensure STATIC_URL is set correctly
   - Check collectstatic is working

### Debug Mode
To enable debug mode temporarily:
```bash
vercel env add DJANGO_DEBUG
# Set value to: True
```

## 📱 Alternative Deployment Options

If Vercel doesn't work, try:
- **PythonAnywhere**: Easier for Django
- **Heroku**: Django-friendly
- **Railway**: Modern deployment
- **DigitalOcean**: Full control

---

**Your food delivery app will be live in minutes! 🍕🚀**
