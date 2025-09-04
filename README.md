# <img src="static\images\logo.png" alt="Logo" width="27"> Trackify
_lightweight Order Management System with JWT Authentication & CRUD operations_

<img src="static\images\order_dashboard.png" alt="dashboard" width="">

## 📖 Overview 
**Trackify** is a simple yet powerful order management platform.
It deliveres a SaaS-style **Analytics Dashboard** with interactive charts, advanced filters, search, and sorting enabling 10x faster order tracking and improved decision visibility. 

It provides a real time dashboard UI for managing customer orders, powered by **JWT authentication** and a **RESTful API**.

## ✨ Features
- 🔐 JWT Authentication for secure API requests
- 👤 User Login with session management
- 💻 Real-time analytics dashboard (orders by status, trends, top customers/products)
- 📊 Optimized query performance  with search, sorting, and filters (status, date range, customer).
- ➕ Create Orders with customer & product details
- ✏️ Update Orders with status flow (Pending → Processing → Shipped → Delivered)
- ❌ Delete Orders by ID
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

###  Create Order (Example)
```json
{
  "customer": "Alice", 
  "product": "Laptop"
}
```

###  Update Order ( Pending > Processing > Shipped > Delivered)
```json
{
  "status": "Processing" 
}
```
## 📸 Screenshots
<img src="static\images\home.png" alt="Home" width="350"> <img src="static\images\login.png" alt="Login" width="350"> 
<img src="static\images\analytics.png" alt="Analytics" width="350"> 
<img src="static\images\features.png" alt="About" width="350">

## 💻Future Enhancements
- 📧 Email notifications on order updates
- 👥 Role-based access (Admin/User)
- 📦 Product catalog integration
- ☁️ Deployment on AWS/Heroku

## 👯 About Team
- [Alorika Jain](https://github.com/BLACKACE13) - Backened and API Developer
- [Sarthak Jain](https://github.com/1905Sarthak) - Frontend Developer

We hope you enjoy using it as much as we enjoyed creating it! <3