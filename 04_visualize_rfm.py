import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg') # Headless backend
import matplotlib.pyplot as plt
import numpy as np
import os

def create_rfm_visualization(input_file='data/rfm_scores.csv'):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run previous scripts first.")
        return

    # Load data
    df = pd.read_csv(input_file)

    # 1. Remove Outliers (above 95th percentile for better visualization)
    # We focus on Frequency and Monetary for this scatter plot
    f_limit = df['Frequency'].quantile(0.95)
    m_limit = df['Monetary'].quantile(0.95)
    
    df_filtered = df[(df['Frequency'] <= f_limit) & (df['Monetary'] <= m_limit)].copy()
    
    print(f"Original shape: {df.shape}")
    print(f"Filtered shape (removing top 5% outliers): {df_filtered.shape}")

    # Set aesthetic style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 8))

    # 2. Create Scatterplot
    # X = Recency (Lower is better/lefthand), Y = Frequency (Higher is better/top)
    scatter = sns.scatterplot(
        data=df_filtered, 
        x='Recency', 
        y='Frequency', 
        hue='Monetary', 
        palette='magma', 
        size='Monetary',
        sizes=(20, 200),
        alpha=0.6
    )

    # 3. Add Business Zones (Annotations)
    r_mid = df_filtered['Recency'].median()
    f_mid = df_filtered['Frequency'].median()
    
    x_max = df_filtered['Recency'].max()
    y_max = df_filtered['Frequency'].max()

    # Define Zone Rectangles & Labels
    # Champions: Low Recency (Left), High Frequency (Top)
    # At Risk: High Recency (Right), High Frequency (Top)
    # New Customers: Low Recency (Left), Low Frequency (Bottom)
    zones = [
        {"name": "CHAMPIONS", "x": [0, r_mid], "y": [f_mid, y_max], "color": "green", "alpha": 0.05},
        {"name": "AT RISK", "x": [r_mid, x_max], "y": [f_mid, y_max], "color": "red", "alpha": 0.05},
        {"name": "NEW CUSTOMERS", "x": [0, r_mid], "y": [0, f_mid], "color": "blue", "alpha": 0.05},
        {"name": "HIBERNATING", "x": [r_mid, x_max], "y": [0, f_mid], "color": "gray", "alpha": 0.05},
    ]

    for zone in zones:
        # Drawing the zone box
        plt.axvspan(zone['x'][0], zone['x'][1], 
                    ymin=zone['y'][0]/y_max, ymax=zone['y'][1]/y_max, 
                    color=zone['color'], alpha=zone['alpha'])
        
        # Adding Text Label
        text_x = sum(zone['x']) / 2
        text_y = sum(zone['y']) / 2
        plt.text(text_x, text_y, zone['name'], 
                 horizontalalignment='center', verticalalignment='center',
                 fontsize=14, fontweight='bold', color=zone['color'], alpha=0.5)

    # Aesthetics
    plt.title('RFM Segmentation: Recency vs Frequency', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Recency (Days Since Last Purchase)', fontsize=12)
    plt.ylabel('Frequency (Number of Orders)', fontsize=12)
    plt.legend(title='Monetary (£)', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    
    # Save the plot
    output_img = 'rfm_segments.png'
    plt.savefig(output_img, dpi=300)
    print(f"✅ Success! Visualization saved to {output_img}")

if __name__ == "__main__":
    create_rfm_visualization()
