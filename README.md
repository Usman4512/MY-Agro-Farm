# Agro Management System

A complete Agriculture Management System built with Flask, MySQL, HTML/CSS featuring email verification, crop management, market rates in PKR, inventory tracking, expense management, and admin panel.

## Features

- **User Authentication**
  - Registration with email verification
  - Login/Logout with session management
  - Forgot password with email reset link
  - Profile management
  - Change password

- **Dashboard**
  - Beautiful analytics cards
  - Recent crops & expenses overview
  - Profit/loss calculations in PKR
  - Quick action buttons
  - Notification system

- **Crop Management**
  - Add/Edit/View/Delete crops
  - Track crop lifecycle (Planned -> Planted -> Growing -> Harvested)
  - Record harvest data with yield & revenue
  - Filter by status, season
  - Financial tracking per crop

- **Market Rates (PKR)**
  - Daily crop rates from major Pakistani markets
  - Filter by crop, city, market
  - Average/min/max rate comparison
  - Detailed rate history per crop
  - Bar chart visualization

- **Inventory Management**
  - Track seeds, fertilizers, pesticides, tools
  - Quantity and cost tracking
  - Expiry date alerts
  - Category-wise summary

- **Expense Tracking**
  - Categorize expenses (seeds, labor, irrigation, etc.)
  - Payment method tracking
  - Total expense analytics
  - Receipt number storage

- **Admin Panel**
  - Dashboard with system analytics
  - Manage all farmers (view, suspend/activate)
  - Manage crop rates (add, deactivate)
  - Activity log tracking
  - System reports

## Technology Stack

- **Backend:** Flask (Python)
- **Database:** MySQL with PyMySQL
- **Frontend:** HTML5, CSS3, Font Awesome
- **Charts:** Chart.js
- **Email:** SMTP (Gmail compatible)

## Project Structure

```
agro_system/
|
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── README.md              # This file
|
├── /models
│   └── db.py              # Database models & helper functions
|
├── /routes
│   ├── auth.py            # Authentication routes
│   ├── dashboard.py       # Dashboard & profile routes
│   ├── crops.py           # Crop, inventory, expense routes
│   ├── admin.py           # Admin panel routes
│   └── rates.py           # Market rates routes
|
├── /templates
│   ├── base.html          # Base template
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── verify_pending.html# Email verification pending
│   ├── resend_verification.html
│   ├── forgot_password.html
│   ├── reset_password.html
│   ├── dashboard.html     # Main dashboard
│   ├── profile.html       # User profile
│   ├── notifications.html # Notifications page
│   ├── 404.html           # Error page
│   ├── 500.html           # Error page
│   ├── /crops             # Crop management templates
│   │   ├── list.html
│   │   ├── add.html
│   │   ├── view.html
│   │   ├── edit.html
│   │   ├── inventory.html
│   │   └── expenses.html
│   ├── /rates             # Market rates templates
│   │   ├── index.html
│   │   └── detail.html
│   └── /admin             # Admin panel templates
│       ├── dashboard.html
│       ├── farmers.html
│       ├── farmer_detail.html
│       ├── rates.html
│       ├── activities.html
│       └── reports.html
|
├── /static
│   ├── /css
│   │   └── style.css      # Main stylesheet
│   ├── /js               # JavaScript files
│   └── /images           # Image assets
│
└── /utils
    └── email.py           # Email sending utility
```

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- pip

### Step 1: Create MySQL Database

```sql
CREATE DATABASE agro_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Database & Email

Edit `config.py` with your MySQL credentials and email settings:

```python
# MySQL Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'agro_system'

# Email Configuration (Gmail example)
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'  # Use App Password, not your regular password
```

**Note:** For Gmail, you need to generate an App Password from your Google Account settings.

### Step 4: Initialize Database

```bash
cd agro_system
flask init-db
```

This will create all tables and insert sample data including:
- Default admin account
- 14 sample crop rates from major Pakistani markets

### Step 5: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Default Accounts

| Role | Username | Password | Email |
|------|----------|----------|-------|
| Admin | admin | admin123 | admin@agrosystem.com |

**Note:** Change the default admin password after first login!

## Email Setup Guide

### Gmail SMTP Setup

1. Go to Google Account Settings
2. Enable 2-Step Verification
3. Go to Security > App Passwords
4. Generate a new app password for "Mail"
5. Use this password in config.py (not your regular Gmail password)

### Other Email Providers

Update these settings in config.py:
- **Outlook:** MAIL_SERVER = 'smtp.office365.com', MAIL_PORT = 587
- **Yahoo:** MAIL_SERVER = 'smtp.mail.yahoo.com', MAIL_PORT = 587

## Environment Variables

You can also configure via environment variables:

```bash
export SECRET_KEY='your-secret-key'
export MYSQL_HOST='localhost'
export MYSQL_USER='root'
export MYSQL_PASSWORD='password'
export MYSQL_DB='agro_system'
export MAIL_USERNAME='email@gmail.com'
export MAIL_PASSWORD='app-password'
```

## Sample Crop Rates Included

The system comes with pre-loaded rates from major Pakistani markets:

| Crop | Variety | Market | Rate (Rs./kg) |
|------|---------|--------|---------------|
| Wheat | Desi | Lahore Grain Market | 65.00 |
| Rice | Basmati | Gujranwala Mandi | 280.00 |
| Cotton | MNH-786 | Multan Cotton Market | 185.00 |
| Sugarcane | CP-77 | Faisalabad Mandi | 12.00 |
| Maize | Hybrid | Sahiwal Grain Market | 58.00 |
| Mango | Chaunsa | Multan Fruit Market | 150.00 |

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

This project is open source and available for personal and educational use.

## Support

For issues or questions, please contact the development team.

---

**Built with love for Pakistani farmers!** <i class="fas fa-heart"></i>
