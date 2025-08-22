from datetime import datetime
from database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "customer": self.customer,
            "product": self.product,
            "status": self.status,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }
