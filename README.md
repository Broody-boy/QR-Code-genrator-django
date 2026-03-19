# 📱 Django QR Code Generator

A simple, beginner-friendly web application built with Django that generates QR codes from text or URLs. This project features a beautiful, responsive UI with a modern gradient design.

![QR Code Generator](https://img.shields.io/badge/Django-4.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎯 **Simple Interface**: Clean and intuitive form to generate QR codes
- ⚡ **Instant Generation**: Create QR codes in seconds
- 💾 **Download Option**: Save generated QR codes as PNG files
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 🔒 **No Login Required**: Start generating QR codes immediately
- 💡 **Beginner-Friendly**: Easy to understand code structure for learning

## 🛠️ Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3
- **QR Code Library**: qrcode 7.4.2
- **Image Processing**: Pillow 10.1.0
- **Database**: SQLite3 (Django default)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

Follow these steps to run the project on your local machine:

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Django-QR-Code-Generator
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```

## 📖 How to Use

1. **Enter Your Data**: Type or paste any text or URL in the input field
2. **Generate**: Click the "Generate QR Code" button
3. **View**: See your QR code displayed on the screen
4. **Download**: Click "Download QR Code" to save it as a PNG file
5. **Create Another**: Click "Create Another" to generate more QR codes

## 📁 Project Structure

```
Django-QR-Code-Generator/
│
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── README.md                # Project documentation
├── db.sqlite3               # SQLite database (created after migration)
│
├── qrcode_project/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── generator/               # QR code generator app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Database models (not used in this simple version)
│   ├── views.py             # View functions for handling requests
│   ├── urls.py              # App-specific URL patterns
│   └── tests.py
│
├── templates/               # HTML templates
│   ├── base.html            # Base template with common layout
│   └── generator/
│       ├── home.html        # Home page with form
│       └── result.html      # Result page with QR code
│
├── static/                  # Static files (CSS, JS, images)
│   └── css/
│       └── style.css        # Main stylesheet
│
└── media/                   # Generated QR codes (created automatically)
    └── qrcodes/
```

## 🎨 Customization

### Changing Colors

Edit `static/css/style.css` to customize the color scheme:

```css
/* Main gradient background */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Button colors */
.btn-generate {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### QR Code Settings

Modify QR code properties in `generator/views.py`:

```python
qr = qrcode.QRCode(
    version=1,          # Size of QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,        # Size of each box in pixels
    border=4,           # Border size in boxes
)
```

## 🔧 Troubleshooting

### Issue: Module not found errors
**Solution**: Make sure you've activated the virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: Run the server on a different port:
```bash
python manage.py runserver 8080
```

### Issue: Static files not loading
**Solution**: Run the collectstatic command:
```bash
python manage.py collectstatic
```

## 🌟 Features Explained

### Home Page
- Clean form interface with a textarea for user input
- Emoji icons for visual appeal
- Info cards showing key features
- Fully responsive design

### Result Page
- Displays the generated QR code in a card layout
- Shows the original data entered
- Download button to save the QR code
- Option to create another QR code
- Usage tips for beginners

## 📚 Learning Resources

This project is perfect for beginners learning Django. Key concepts covered:

- Django project structure
- URL routing
- Views and templates
- Static files management
- Media files handling
- Form handling with POST requests
- File generation and downloads
- Responsive CSS design

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ for learning Django

## 🙏 Acknowledgments

- Django framework for making web development simple
- qrcode library for easy QR code generation
- All contributors and users of this project

## 📞 Support

If you have any questions or need help:
- Open an issue on GitHub
- Check the Django documentation: https://docs.djangoproject.com/

---

**Happy Coding! 🚀**

*Remember: This is a learning project. For production use, add proper error handling, validation, and security measures.*
