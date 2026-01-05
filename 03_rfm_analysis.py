import pandas as pd
import datetime as dt
import os

def perform_rfm_analysis(input_file='data/retail_clean.csv', output_file='data/rfm_scores.csv'):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run 01_load_data.py first.")
        return

    print(f"--- Loading data from {input_file} ---")
    df = pd.read_csv(input_file)
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Calculate TotalPrice (for Monetary calculation)
    df['TotalPrice'] = df['Quantity'] * df['Price']
    
    # Define the reference date (max date + 1 day) for Recency
    today_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    print(f"Analysis Reference Date: {today_date}")

    # Grouping by Customer ID to calculate RFM metrics
    print("Calculating RFM metrics...")
    rfm = df.groupby('Customer ID').agg({
        'InvoiceDate': lambda date: (today_date - date.max()).days,
        'Invoice': lambda num: num.nunique(),
        'TotalPrice': lambda price: price.sum()
    })

    # Rename columns to Recency, Frequency, Monetary
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    
    # Optional: Reset index to keep 'Customer ID' as a column
    rfm.reset_index(inplace=True)

    print(f"--- RFM Summary ---")
    print(rfm.head())
    print(f"Total Customers Analyzed: {len(rfm):,}")

    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save the RFM scores
    rfm.to_csv(output_file, index=False)
    print(f"✅ Success! RFM scores saved to {output_file}")

if __name__ == "__main__":
    perform_rfm_analysis()
