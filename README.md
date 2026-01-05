# Customer Segmentation Analysis (RFM)

## Executive Summary
This project analyzes customer behavior for a UK-based online retailer. Using **RFM (Recency, Frequency, Monetary)** analysis, we categorized **5,878 customers** to identify high-value segments and retention opportunities.

## Key Findings
Based on the analysis of thousands of transactions, we have identified several business-critical segments:

- **🏆 Champions (2,232 Customers):** Our most valuable group. They shop frequently and have purchased within the last 3 months. 
- **⚠️ At Risk (1,079 Customers):** High-frequency shoppers who haven't made a purchase in over 96 days. These are prime targets for re-engagement campaigns.
- **🌱 New Customers (721 Customers):** Recent buyers with low frequency. There is significant potential to convert these into loyalists.
- **💰 Revenue Concentration:** The top 5 customers alone represent nearly **£1.99M** in total spend, highlighting a heavy reliance on whales.
- **📊 Average Spend:** The mean lifetime value (LTV) across the entire customer base is approximately **£3,018**.

## The Data
Source: [UCI Machine Learning Repository - Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

## How to Run
1. **Load/Clean Data:** `python 01_load_data.py`
2. **RFM Analysis:** `python 03_rfm_analysis.py`
3. **Visualization:** `python 04_visualize_rfm.py`

*The generated visualization can be found in `data/rfm_segments.png`.*