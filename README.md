# 📦 Trackify
_lightweight Order Management System with JWT Authentication & CRUD operations_
## 📖 Overview 
Trackify is a simple yet powerful order management system built with **Flask**.
It provides a clean dashboard UI for managing customer orders, powered by **JWT authentication** and a **RESTful API**.

This project is designed as a demo SaaS-style application, showcasing full-stack development skills (Backend + Frontend + Database).
## ✨ Features
- 🔐 JWT Authentication for secure API requests
- 👤 User Login with session management
- 📊 Dashboard UI to view orders in a neat table
- ➕ Create Orders with customer & product details
- ✏️ Update Orders with status flow (Pending → Processing → Shipped → Delivered)
- ❌ Delete Orders by ID
- 📱 Responsive Bootstrap Frontend with modals for CRUD
- 🗄️ Database persistence using SQLAlchemy

## 🛠 Tech Stack

- **Backend**: Flask, Flask-JWT-Extended, SQLAlchemy
- **Frontend**: HTML, Bootstrap, JavaScript (Fetch API)
- **Database**: SQLite (can switch to PostgreSQL/MySQL)
- **Auth**: JWT + Flask session

## ⚙️ Setup Instructions

1) Clone this repo 
```bash 
git clone https://github.com/BLACKACE13/trackify .git
cd trackify
```
2) Create Virtual Environment (Optional) and Install dependencies
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```
3) Run Application
```bash
python app.py
```
App will be live at: http://127.0.0.1:5000/

## 📡 API Endpoints
| Method| Endpoint | Description | Auth Required |
| :--- | :--- | :--- | ---: |
| POST | `/login` | Login & get JWT token | ❌ |
| GET | `/orders` | Get all orders |✅|
| POST | `/orders`| Create new order |✅|
| PUT | `/orders/<id>` | Update order status |✅|
| DELETE | `/orders/<id>` | Delete an order |✅|
| GET | `/orders/<id>/history` | Get order history |✅|

###  Create Order
```json
{
  "customer": "Alice", //example
  "product": "Laptop"
}
```

###  Update Order
```json
{
  "status": "Processing" // Pending > Processing > Shipped > Delivered
}
```
## 📸 Screenshots
Will be added soon

## 💻Future Enhancements
- 📧 Email notifications on order updates
- 👥 Role-based access (Admin/User)
- 📦 Product catalog integration
- ☁️ Deployment on AWS/Heroku

## 👯 About Team
- [Alorika Jain](https://github.com/BLACKACE13) - Backened and API Developer
- [Sarthak Jain](https://github.com/1905Sarthak) - Full Stack Developer

We hope you enjoy using it as much as we enjoyed creating it! <3
