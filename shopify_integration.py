import json

def fetch_shopify_order():
    try:
        with open("test_orders.json", "r") as file:
            orders = json.load(file)
        print("Fetched test orders from JSON.")
        return orders
        '''
        order_list=[]
        for order in orders:
            i_list=[]
            for i in order:
                i_list.append(order[i])
            order_list.append(i_list)
        return order_list'''
    except Exception as e:
        print(f"Error reading test orders: {e}")
        return []
    