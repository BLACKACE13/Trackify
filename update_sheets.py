import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Authenticate Google Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
def authenticate_google_sheets():
    
    creds = Credentials.from_service_account_file("e-commerce-gsheet-944f2f495406.json", scopes=SCOPES)
    client = gspread.authorize(creds)
    return client

# Update Google Sheets
def update_google_sheets(orders):
    client = authenticate_google_sheets()
    sheet = client.open("e-commerce-gsheet").sheet1 

    # Convert orders to list format
    data = [["Order ID", "Email", "Items", "Total Price"]]
    for order in orders:
        data.append([order["order_id"], order["email"], ", ".join(order["items"]), order["total_price"]])

    # Clear existing data and update
    sheet.clear()
    sheet.update(data)

    print("✅ Google Sheets updated successfully.")

def update_excel_sheet(orders):
    file_path = "e-commerce_orders.xlsx"  # Path to your Excel file

    # Convert orders to DataFrame
    df = pd.DataFrame(orders)

    # Save to Excel (Creates file if it doesn't exist)
    df.to_excel(file_path, index=False)
    
    print("✅ Excel file updated successfully.")

def update_sheets(orders, method="google"):
    if method == "google":
        update_google_sheets(orders)
    else:
        update_excel_sheet(orders)
