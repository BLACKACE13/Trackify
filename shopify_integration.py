import json

def fetch_shopify_order():
    try:
        with open("test_orders.json", "r") as file:
            orders = json.load(file)
        print("Fetched test orders from JSON.")
        for order in orders:
            for i in order:
                print(order[i],end=" ")
            print("")
    except Exception as e:
        print(f"Error reading test orders: {e}")
        return []
    