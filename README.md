# 🥗 Modern Calorie Tracker - Premium Health Analytics Platform

[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.x-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE.txt)

A state-of-the-art, personalized nutrition tracking application with **automatic BMR/TDEE calculation**, real-time macro targeting, and premium data visualization. Built as a production-ready MCA final year project demonstrating advanced full-stack development with Django.

---

## ✨ Project Overview

The **Modern Calorie Tracker** is a comprehensive health analytics platform that combines clinical nutrition science with modern web technologies. Unlike basic calorie counters, this application provides **personalized nutrition targets** based on your unique health metrics using the **Mifflin-St Jeor equation** - the gold standard in metabolic rate calculation.

### 🎯 What Makes This Special?

- **Science-Based**: Uses clinically validated BMR/TDEE formulas
- **Personalized**: Tailored nutrition targets based on your goals
- **Real-Time**: Instant calculations and visual feedback
- **Beautiful**: Premium dual-theme UI with glassmorphism effects
- **Secure**: Complete user authentication and data isolation

---

## 🚀 Key Features

### 👤 Advanced User Profile System
- **Health Metrics Tracking**: Gender, age, height, weight, activity level, and health goals
- **Automatic BMR Calculation**: Uses Mifflin-St Jeor equation for clinical accuracy
- **TDEE Computation**: Total Daily Energy Expenditure based on activity multipliers
- **Smart Goal Adjustment**: Automatic calorie and macro targets for weight loss, maintenance, or gain
- **Real-time Preview**: See your nutrition targets update instantly as you edit metrics

### 🔐 Secure Personalization
- **User Authentication**: Secure login and registration with Django's auth framework
- **Private Data**: Each user's health data and logs are completely isolated
- **Profile Management**: Automatic profile creation with sensible defaults
- **Session Security**: CSRF protection and secure password hashing

### 📊 Intelligent Tracking & Visualization
- **Dynamic Dashboard**: Real-time progress tracking with visual indicators
- **Dual Chart System**:
  - **Nutrient Distribution**: Doughnut chart showing macro breakdown
  - **Weekly Progress**: Bar chart tracking 7-day calorie trends vs. goals
- **Macronutrient Analysis**: Automated calculation of Carbs, Protein, and Fats
- **Date-based Logging**: Track consumption history across multiple days
- **Portion Control**: Quantity multipliers for accurate tracking

### 🎨 Premium Dual-Theme UI/UX
- **Light Theme (Dashboard)**: Fresh, nature-inspired design with mint/emerald palette
- **Dark Theme (Profile)**: Premium glassmorphism with purple gradients
- **Micro-Animations**: Smooth transitions and hover effects throughout
- **Mobile-First**: Fully responsive design for all devices
- **Real-time Feedback**: Toast notifications and inline validation

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend** | Django | 5.1+ | Server-side logic, ORM, authentication |
| **Language** | Python | 3.8+ | Core programming language |
| **Database** | SQLite3 | Built-in | Lightweight, file-based data storage |
| **Frontend Framework** | Bootstrap | 5.3 | Responsive grid and components |
| **Forms** | Django Crispy Forms | Latest | Enhanced form rendering and validation |
| **Form Templates** | Crispy Bootstrap5 | Latest | Bootstrap 5 template pack |
| **Data Visualization** | Chart.js | 4.x | Interactive charts and graphs |
| **Styling** | Custom CSS | - | Glassmorphism and modern effects |
| **Fonts** | Google Fonts (Inter) | - | Modern, professional typography |

---

## 🔧 Installation & Setup

### Prerequisites
- **Python** 3.8 or higher
- **pip** package manager
- **Git** (for cloning the repository)
- **Virtual environment** (recommended)

### Quick Start Guide

#### 1. Clone the Repository
```bash
git clone https://github.com/Shani871/calorie-tracker.git
cd calorie-tracker
```

#### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate          # MacOS/Linux
venv\Scripts\activate             # Windows
```

#### 3. Install Dependencies
```bash
# Install required packages
pip install django django-crispy-forms crispy-bootstrap5

# Or create a requirements.txt with:
# django>=5.0
# django-crispy-forms>=2.0
# crispy-bootstrap5>=0.7
# Then run: pip install -r requirements.txt
```

#### 4. Database Setup
```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate
```

#### 5. Create Admin User (Optional)
```bash
# Create superuser for admin panel access
python manage.py createsuperuser
```

#### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### 🎬 First-Time Usage

1. **Register**: Navigate to `http://127.0.0.1:8000/register/` and create your account
2. **Set Up Profile**: Complete your health profile at `/profile/` with:
   - Gender, age, height, weight
   - Activity level
   - Health goal (weight loss, maintenance, or gain)
3. **Add Foods**: Create your food library with nutritional information
4. **Start Tracking**: Log your meals on the dashboard and watch your progress!

### 🔑 Admin Panel Access

Access the Django admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials to:
- Manage users
- View and edit food database
- Monitor consumption logs
- Manage user profiles

---

## 📐 BMR/TDEE Calculation Logic

### Mifflin-St Jeor Equation
**For Males:**
```
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5
```

**For Females:**
```
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161
```

### TDEE Calculation
```
TDEE = BMR × Activity Level Multiplier
```

**Activity Levels:**
- Sedentary: 1.2
- Lightly Active: 1.375
- Moderately Active: 1.55
- Very Active: 1.725
- Extra Active: 1.9

### Goal-Based Adjustments
- **Weight Loss**: TDEE - 500 cal (35% protein, 35% carbs, 30% fats)
- **Maintenance**: TDEE (25% protein, 50% carbs, 25% fats)
- **Weight Gain**: TDEE + 300 cal (30% protein, 45% carbs, 25% fats)

---

## 📊 Database Schema

### Profile Model
```python
- user (OneToOne with User)
- gender (Male/Female)
- age (Integer)
- height (Float, cm)
- weight (Float, kg)
- activity_level (Float, 1.2-1.9)
- goal_type (loss/maintain/gain)
- calorie_goal (Integer, calculated)
- protein_goal_pct (Integer)
- carbs_goal_pct (Integer)
- fats_goal_pct (Integer)
```

### Food Model
```python
- name (String)
- carbs (Float, grams)
- protein (Float, grams)
- fats (Float, grams)
- calories (Integer)
```

### Consume Model
```python
- user (ForeignKey to User)
- food_consumed (ForeignKey to Food)
- quantity (Float, multiplier)
- date (DateField, auto)
```

---

## 🎯 Feature Highlights

### Real-Time Macro Preview
As you edit your profile (weight, activity, goal), JavaScript instantly recalculates:
- Daily calorie target
- Protein grams and percentage
- Carbs grams and percentage
- Fats grams and percentage

### Weekly Progress Analytics
Track your consistency with a 7-day bar chart showing:
- Daily calorie intake
- Goal baseline (red dashed line)
- Hover tooltips with exact values

### Custom Food Library
Add your own food items with complete nutritional data:
- Name
- Calories
- Macronutrient breakdown

---

## 📈 Recent Updates (v2.0)

### December 2025 - Major Feature Release
1. **User Profile System**
   - Complete health metrics tracking
   - Automatic BMR/TDEE calculation
   - Goal-based macro targeting
   - Real-time JavaScript preview

2. **Weekly Analytics Dashboard**
   - 7-day calorie trend chart
   - Historical data visualization
   - Goal comparison baseline

3. **UI/UX Overhaul**
   - Dual-theme design (Light + Dark)
   - Glassmorphism effects
   - Smooth animations
   - Enhanced mobile responsiveness

4. **Backend Improvements**
   - Date-based consumption tracking
   - Quantity multipliers
   - Improved validation
   - Secure user isolation

---

## 🎓 Educational Value

This project demonstrates:
- **Clinical Nutrition Science**: Mifflin-St Jeor BMR calculation
- **Full-Stack Development**: Django backend + modern frontend
- **Database Design**: Normalized schema with relationships
- **User Experience**: Real-time updates and visual feedback
- **Security Best Practices**: Authentication, CSRF, data isolation
- **Responsive Design**: Mobile-first CSS and Bootstrap grid
- **Data Visualization**: Chart.js integration and customization

---

## 🚀 Future Enhancements

- [ ] Export nutrition data as PDF reports
- [ ] Integration with fitness trackers (Apple Health, Google Fit)
- [ ] Meal planning and recipe suggestions
- [ ] Barcode scanner for food lookup
- [ ] Social features (share progress, challenges)
- [ ] Multiple BMR formula options (Harris-Benedict, Katch-McArdle)
- [ ] Weight history tracking with trend graphs
- [ ] Micronutrient tracking (vitamins, minerals)

---

## 📸 Screenshots

### 🏠 Dashboard (Light Theme)
![Dashboard Preview](https://via.placeholder.com/800x500/e8f5e9/2e7d32?text=Dashboard+-+Light+Theme)

**Features:**
- Fresh, nature-inspired design with mint/emerald palette
- Weekly progress bar chart (7-day calorie trends)
- Nutrient distribution doughnut chart
- Real-time macro tracking
- Food consumption log with date filtering

### 👤 Profile Page (Dark Theme)
![Profile Preview](https://via.placeholder.com/800x500/1a1a2e/9d4edd?text=Profile+-+Dark+Theme)

**Features:**
- Premium glassmorphism UI with purple gradients
- Real-time BMR/TDEE calculations
- Interactive macro target preview
- Health metrics input with instant feedback
- Goal-based nutrition recommendations

### 🔐 Authentication Pages
![Auth Preview](https://via.placeholder.com/800x500/ffffff/333333?text=Login+%26+Register)

**Features:**
- Clean, modern login/register forms
- Django Crispy Forms integration
- CSRF protection
- User-friendly validation messages

---

## 👨‍💻 Development

### Project Structure
```
calorie-tracker/
├── DjangoProject4/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Website/                 # Main app
│   ├── models.py           # Profile, Food, Consume
│   ├── views.py            # BMR/TDEE logic
│   ├── urls.py
│   └── admin.py
├── templates/               # HTML templates
│   ├── index.html          # Dashboard
│   ├── profile.html        # User profile
│   ├── login.html
│   └── register.html
├── static/
│   └── css/
│       └── style.css       # Custom styling
└── db.sqlite3              # Database
```

### Running Tests
```bash
python manage.py test
```

### Admin Panel
Access at `http://127.0.0.1:8000/admin/` with superuser credentials

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📧 Contact & Support

**Developer**: Shani Chauhan  
**Project**: MCA Final Year Project  
**GitHub**: [@Shani871](https://github.com/Shani871)  
**Repository**: [calorie-tracker](https://github.com/Shani871/calorie-tracker)

### 💬 Get Help
- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/Shani871/calorie-tracker/issues)
- **Discussions**: Ask questions in [GitHub Discussions](https://github.com/Shani871/calorie-tracker/discussions)

---

## ⭐ Show Your Support

If you found this project helpful, please consider:
- Giving it a ⭐ on GitHub
- Sharing it with others
- Contributing to its development

---

<div align="center">

**Built with ❤️ using Django, Bootstrap, and Chart.js**

*Combining nutrition science with modern web development*

</div>
