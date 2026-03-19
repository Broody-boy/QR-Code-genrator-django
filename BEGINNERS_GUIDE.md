# 🎓 Beginner's Guide to Django QR Code Generator

Welcome! This guide will help you understand and run this Django project, even if you're new to web development.

## 📚 What You'll Learn

- How Django projects are structured
- How to set up a Python virtual environment
- How web forms work
- How to generate and serve files in Django
- Basic HTML and CSS for web design

## 🎯 Project Overview

This project is a simple web application that:
1. Takes text or URL input from a user
2. Generates a QR code image
3. Displays the QR code on the web page
4. Allows users to download the QR code

## 📂 Understanding the Project Structure

Let's break down what each file and folder does:

### Root Directory Files

- **`manage.py`**: Django's command-line tool. You'll use this to run the server, migrate the database, etc.
- **`requirements.txt`**: Lists all Python packages needed for this project
- **`README.md`**: Main project documentation
- **`setup.sh`** / **`setup.bat`**: Automated setup scripts for Linux/Mac and Windows
- **`db.sqlite3`**: The database file (created after first migration)
- **`.gitignore`**: Tells git which files to ignore

### Project Configuration (`qrcode_project/`)

This folder contains the main Django project settings:

- **`settings.py`**: All project settings (database, installed apps, static files, etc.)
- **`urls.py`**: Main URL routing - connects web addresses to views
- **`wsgi.py`** / **`asgi.py`**: Server deployment files (you don't need to touch these as a beginner)

### App Directory (`generator/`)

This is where the main application logic lives:

- **`views.py`**: Functions that handle web requests and return responses
  - `home()`: Shows the main form
  - `generate_qr()`: Creates the QR code
  - `download_qr()`: Handles QR code downloads

- **`urls.py`**: URL patterns specific to this app
  - `/` → home page
  - `/generate/` → QR generation page
  - `/download/` → download handler

- **`models.py`**: Database models (empty in this project - we don't store QR codes permanently)
- **`admin.py`**: Admin panel configuration
- **`tests.py`**: Test cases

### Templates (`templates/`)

HTML files that define what users see:

- **`base.html`**: The main layout template (header, footer, common structure)
- **`generator/home.html`**: Home page with the input form
- **`generator/result.html`**: Result page showing the generated QR code

### Static Files (`static/`)

CSS, JavaScript, and image files:

- **`css/style.css`**: All styling for the website (colors, layouts, animations)

### Media Files (`media/`)

User-uploaded or generated files:

- **`qrcodes/`**: Where generated QR codes are temporarily stored

## 🔧 How the Application Works

### 1. User Flow

```
User visits home page (/) 
    ↓
Enters text/URL in form
    ↓
Submits form to (/generate/)
    ↓
Django generates QR code
    ↓
Saves image to /media/qrcodes/
    ↓
Displays result page with QR code
    ↓
User can download or create another
```

### 2. Django Request-Response Cycle

```
Browser Request → Django URLs → View Function → Template → HTML Response
```

**Example:**
1. Browser requests: `GET /`
2. Django checks `urls.py` and finds pattern `''` → calls `views.home`
3. `views.home()` renders `home.html`
4. HTML is sent back to browser

### 3. QR Code Generation Process

When you submit the form:

```python
# 1. Get data from form
data = request.POST.get('qr_data')

# 2. Create QR code object
qr = qrcode.QRCode(...)

# 3. Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# 4. Generate image
img = qr.make_image(fill_color="black", back_color="white")

# 5. Save to file
img.save(filepath)

# 6. Return URL to show image
return render(request, 'result.html', {'qr_code_url': url})
```

## 🚀 Getting Started

### Option 1: Use the Setup Script (Easiest)

**On Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```
setup.bat
```

### Option 2: Manual Setup

**Step 1: Create Virtual Environment**
```bash
python3 -m venv venv
```

**Step 2: Activate Virtual Environment**

*Linux/Mac:*
```bash
source venv/bin/activate
```

*Windows:*
```
venv\Scripts\activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run Migrations**
```bash
python manage.py migrate
```

**Step 5: Start Server**
```bash
python manage.py runserver
```

**Step 6: Open Browser**
Go to: `http://127.0.0.1:8000/`

## 🎨 Customization Ideas

### 1. Change Colors

Edit `static/css/style.css`:

```css
/* Change background gradient */
body {
    background: linear-gradient(135deg, #your-color1 0%, #your-color2 100%);
}
```

### 2. Modify QR Code Appearance

Edit `generator/views.py`:

```python
qr = qrcode.QRCode(
    version=1,              # Size (1-40, bigger = more data)
    error_correction=...,    # Error tolerance level
    box_size=10,            # Pixel size of each box
    border=4,               # White border size
)

# Change colors
img = qr.make_image(fill_color="blue", back_color="yellow")
```

### 3. Add More Features

Some ideas to extend this project:
- Add different QR code colors
- Allow users to upload logos for QR codes
- Add history of generated QR codes
- Email QR codes to users
- Generate bulk QR codes from CSV file

## 🐛 Common Issues & Solutions

### Issue: "Module not found" error
**Solution:** Make sure you activated the virtual environment and installed requirements:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution:** Either stop the process using port 8000, or run on different port:
```bash
python manage.py runserver 8080
```

### Issue: Static files not loading
**Solution:** 
1. Check `STATIC_URL` in settings.py
2. Make sure `{% load static %}` is at top of template
3. Run `python manage.py collectstatic`

### Issue: Generated QR code not displaying
**Solution:**
1. Check that `media/qrcodes/` directory exists
2. Verify `MEDIA_URL` and `MEDIA_ROOT` in settings.py
3. Check file permissions

## 📖 Django Concepts Explained

### What is a Virtual Environment?

A virtual environment is an isolated Python environment where you can install packages without affecting your system Python. Think of it as a separate container for your project's dependencies.

**Why use it?**
- Different projects need different package versions
- Keeps your system Python clean
- Makes project portable

### What is a View?

A view is a Python function that receives a web request and returns a web response. It's the "logic" of your web application.

**Example:**
```python
def home(request):
    # This runs when someone visits the home page
    return render(request, 'home.html')
```

### What is a Template?

A template is an HTML file that can include Django template language (variables, loops, conditionals). Django processes these and returns plain HTML.

**Example:**
```html
<h1>Welcome, {{ user.name }}!</h1>  <!-- Variable -->
{% if user.is_logged_in %}          <!-- Conditional -->
    <p>You are logged in!</p>
{% endif %}
```

### What is a URL Pattern?

URL patterns map web addresses to view functions.

**Example:**
```python
urlpatterns = [
    path('', views.home, name='home'),           # / → home view
    path('generate/', views.generate_qr, name='generate_qr'),  # /generate/ → generate_qr view
]
```

### What is Static vs Media?

- **Static files**: CSS, JS, images that are part of your code (don't change)
- **Media files**: User-uploaded or generated files (change based on user actions)

## 🎓 Learning Resources

### Django Documentation
- Official Docs: https://docs.djangoproject.com/
- Django Tutorial: https://docs.djangoproject.com/en/4.2/intro/tutorial01/

### Python
- Python.org Tutorial: https://docs.python.org/3/tutorial/
- Learn Python: https://www.learnpython.org/

### HTML/CSS
- MDN Web Docs: https://developer.mozilla.org/
- W3Schools: https://www.w3schools.com/

### QR Codes
- qrcode library docs: https://pypi.org/project/qrcode/

## 💡 Next Steps

After getting comfortable with this project:

1. **Add user authentication** - Let users create accounts
2. **Save QR codes to database** - Keep history of generated codes
3. **Add API endpoint** - Let other apps generate QR codes
4. **Deploy to production** - Host on Heroku, PythonAnywhere, or AWS
5. **Add testing** - Write unit tests for your views

## 🤝 Need Help?

- Read error messages carefully - they often tell you what's wrong
- Google the error message
- Check Django documentation
- Ask in Django community forums
- Check Stack Overflow

## 🎉 Congratulations!

You've learned how to run a complete Django web application! This project covers:
- ✅ Django project structure
- ✅ Virtual environments
- ✅ Forms and user input
- ✅ File generation and serving
- ✅ HTML templates
- ✅ CSS styling
- ✅ URL routing

Keep building and learning! 🚀

---

**Remember:** Every expert was once a beginner. Don't be afraid to experiment and break things - that's how you learn!
