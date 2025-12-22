import pandas as pd
import os



FILE_PATH = 'data/online_retail_II.xlsx'

# Audit the data to understand its structure and cleanliness
def audit_data():
    if not os.path.exists(FILE_PATH):
        print("❌ File not found.")
        return

    print("--- Loading Data for Audit ---")

        # Load the first sheet of the Excel file
    try:
        df = pd.read_excel(FILE_PATH) 

    except Exception as e:
        print(f"Error loading: {e}")
        return

    print(f"✅ Data Loaded. Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    print("--- 1. First 5 Rows (What does it look like?) ---")
    print(df.head(), "\n")

    print("--- 2. Data Types (Do we have numbers where text should be?) ---")
    print(df.info(), "\n")

    print("--- 3. Numerical Summary (Check for negatives) ---")
    print(df.describe(), "\n")
    
    print("--- 4. Missing Values (Where are the holes?) ---")
    print(df.isnull().sum(), "\n")



if __name__ == "__main__":
    audit_data()