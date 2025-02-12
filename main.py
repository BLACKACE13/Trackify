from shopify_integration import fetch_shopify_order
from update_sheets import update_excel_sheet,update_google_sheets
import time
def run_automation():
    print("Fetching data...")
    orders=fetch_shopify_order()

    print("📊 Updating Google Sheets & Excel...")
    update_google_sheets(orders)
    update_excel_sheet(orders)
    

if __name__ == "__main__":
    while True:
        run_automation()
        print("⏳ Waiting 15 minutes before next run...")
        time.sleep(900) 