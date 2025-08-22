# E-Commerce Order Automation 📦
## 📌 Project Overview 
A backend service built with Flask + SQLite that automates order management.
Supports CRUD APIs for creating, updating, retrieving, and deleting orders.
(Upcoming: automated order workflow, status tracking, email alerts).

## 🛠 Tech Stack

- Flask (backend framework)
- Flask-SQLAlchemy (ORM for database)
- SQLite (lightweight database, easy to switch to Postgres)

## ⚙️ Setup Instructions

1) Clone this repo 
```bash 
git clone https://github.com/BLACKACE13/e-commerce-order-automation.git
```
2) Install dependencies
```bash
pip install -r requirements.txt
```
3) Run server
```bash
python app.py
```
## 📡 API Endpoints
### ➕ Create Order
POST /orders
```json
{
  "customer": "Alice",
  "product": "Laptop"
}
```
### 📋 Get All Orders
GET /orders

### ✏️ Update Order
PUT /orders/{id}
```json
{
  "status": "Processing"
}
```
### ❌ Delete Order
DELETE /orders/{id}