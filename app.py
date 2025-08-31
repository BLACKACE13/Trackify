from flask import Flask, request, jsonify
from database import db
from models import Order, OrderHistory, User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "Thatsmysecret@123"  # later .env 
jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()

# Create Order
@app.route("/orders", methods=["POST"])
@jwt_required()
def create_order():
    user_id = int(get_jwt_identity())
    data = request.get_json()
    new_order = Order(customer=data["customer"], product=data["product"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# Get All Orders
@app.route("/orders", methods=["GET"])
@jwt_required()
def get_orders():
    user_id = int(get_jwt_identity())
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])

# Update Order Status
@app.route("/orders/<int:order_id>", methods=["PUT"])
@jwt_required()
def update_order(order_id):
    user_id = int(get_jwt_identity())
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
@jwt_required()
def delete_order(order_id):
    user_id = int(get_jwt_identity())
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} deleted"})

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User already exists"}), 400
    
    new_user = User(username=data["username"])
    new_user.set_password(data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=str(user.id))
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
