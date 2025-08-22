from flask import Flask, request, jsonify
from database import db
from models import Order, OrderHistory

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Create Order
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    new_order = Order(customer=data["customer"], product=data["product"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# Get All Orders
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])

# Update Order Status
@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()

    if "status" in data:
        old_status = order.status
        new_status = data["status"]

        # Enforce valid workflow
        valid_flow = {
            "Pending": "Processing",
            "Processing": "Shipped",
            "Shipped": "Delivered"
        }

        if new_status not in valid_flow.values() and new_status != "Delivered":
            return jsonify({"error": "Invalid status"}), 400

        order.status = new_status

        # Log status change
        history = OrderHistory(
            order_id=order.id,
            old_status=old_status,
            new_status=new_status
        )
        db.session.add(history)

        # Mock email (console print)
        print(f"[EMAIL MOCK] Order {order.id} status changed from {old_status} → {new_status}")

    db.session.commit()
    return jsonify(order.to_dict())

@app.route("/orders/<int:order_id>/history", methods=["GET"])
def get_order_history(order_id):
    history = OrderHistory.query.filter_by(order_id=order_id).all()
    return jsonify([
        {
            "id": h.id,
            "order_id": h.order_id,
            "old_status": h.old_status,
            "new_status": h.new_status,
            "timestamp": h.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for h in history
    ])

# Delete Order
@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} deleted"})

if __name__ == "__main__":
    app.run(debug=True)
