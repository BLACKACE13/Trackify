from datetime import datetime
from zoneinfo import ZoneInfo   
from werkzeug.security import generate_password_hash, check_password_hash
from database import db

IST = ZoneInfo("Asia/Kolkata")  

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    date = db.Column(db.DateTime, default=lambda: datetime.now(IST))  

    def to_dict(self):
        return {
            "id": self.id,
            "customer": self.customer,
            "product": self.product,
            "status": self.status,
            "date": self.date.strftime("%d-%m-%Y %H:%M:%S")
        }

class OrderHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    old_status = db.Column(db.String(50))
    new_status = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(IST))  # ✅ IST instead of UTC

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
