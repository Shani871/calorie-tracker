# Calorie Tracker Web Application 🥗

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

A comprehensive web application for tracking daily calorie consumption, setting personalized goals, and analyzing macronutrient intake through an intuitive interface.

![Dashboard Screenshot](https://github.com/Shani871/calorie-tracker/blob/main/templates/myapp/Screenshot%202025-01-21%20at%2011.06.19%E2%80%AFPM.png?raw=true)

## ✨ Key Features

### 📊 Nutritional Tracking
- **Calorie Goal Visualization**: Progress bar showing daily consumption vs. target
- **Macronutrient Breakdown**: Detailed carb, protein, and fat analysis
- **Interactive Doughnut Chart**: Visual macronutrient distribution

### 🍎 Food Management
- **Intuitive Food Selection**: Dropdown with comprehensive food database
- **Dynamic Consumption List**: Add/remove items with real-time calculations
- **Nutritional Summaries**: Automatic total calculations for all metrics

### 🎨 User Experience
- **Responsive Design**: Works seamlessly on all devices
- **Clean Dashboard**: All critical information at a glance
- **Instant Feedback**: Visual cues when approaching calorie goals

## 🛠️ Technology Stack

| Component        | Technology               |
|------------------|--------------------------|
| **Frontend**     | HTML5, CSS3, Bootstrap 4 |
| **Data Viz**     | Chart.js                 |
| **Backend**      | Django Framework         |
| **Database**     | SQLite (Django default)  |

## 🚀 Installation Guide

### Prerequisites
- Python 3.8+
- Django 4.0+
- Pip package manager

### Setup Instructions
```bash
# Clone repository
git clone https://github.com/Shani871/calorie-tracker.git
cd calorie-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Access the application at: http://localhost:8000

## 🧩 Project Structure

```
calorie-tracker/
├── myapp/                 # Django application
│   ├── migrations/        # Database migration files
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Data models
│   ├── tests.py           # Test cases
│   ├── urls.py            # App URL routing
│   └── views.py           # Application logic
├── static/                # Static assets (CSS, JS, images)
├── manage.py              # Django command-line utility
└── db.sqlite3             # Database file (development)
```

## 📈 Future Enhancements

- [ ] User authentication system
- [ ] Meal planning functionality
- [ ] Mobile application integration
- [ ] Food database expansion
- [ ] Historical data analysis
- [ ] Barcode scanning for food input

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
