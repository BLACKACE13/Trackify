from shopify_integration import fetch_shopify_order

def run_automation():
    print("Fetching data...")
    shopify_orders = fetch_shopify_order()
    print(shopify_orders)
#hehehe

run_automation()