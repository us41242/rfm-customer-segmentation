import pandas as pd
import os

# Paths
RAW_FILE = 'data/online_retail_II.xlsx'
OUTPUT_FILE = 'data/retail_clean.csv'

def load_and_clean_data():
    if not os.path.exists(RAW_FILE):
        print(f"❌ Error: File not found at {RAW_FILE}. Did you move the Excel file into the data folder?")
        return

    print("Step 1: Loading Excel file... (This might take a moment)")
    
    # Load all sheets from the Excel file

    xls = pd.read_excel(RAW_FILE, sheet_name=None)
    
    # Combine all sheets into one DataFrame
    df = pd.concat(xls.values(), ignore_index=True)
    print(f"✅ Data Loaded. Total Raw Rows: {df.shape[0]:,}")

    # --- CLEANING ---
    print("Step 2: Cleaning Data...")

    # 1. Remove rows with missing Customer ID
    df.dropna(subset=['Customer ID'], inplace=True)
    
    # 2. Remove Cancelled Orders (Invoices starting with 'C')
    df['Invoice'] = df['Invoice'].astype(str)
    df = df[~df['Invoice'].str.startswith('C')]

    # 3. Remove negative prices/quantities
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

    # 4. Convert Customer ID to integer
    df['Customer ID'] = df['Customer ID'].astype(int)

    print(f"✅ Cleaning Complete. Rows Remaining: {df.shape[0]:,}")

    # Save to CSV
    print(f"Step 3: Saving to {OUTPUT_FILE}...")
    df.to_csv(OUTPUT_FILE, index=False)
    print("🎉 Success! Data ready for analysis.")

if __name__ == "__main__":
    load_and_clean_data()