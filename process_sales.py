import pandas as pd

def run_sales_pipeline():
    print("--- STARTING E-COMMERCE SALES PIPELINE ---")
    
    # 1. Load the raw sales data
    df = pd.read_csv("raw_ecommerce_data.csv")
    print(f"[!] Loaded {len(df)} raw customer records.")
    
    # 2. Clean: Remove duplicate entries
    df = df.drop_duplicates()
    
    # 3. Clean: Drop rows where the email is missing (useless for digital marketing)
    df = df.dropna(subset=['email'])
    print(f"[-] Deduplicated and removed invalid leads. Clean records remaining: {len(df)}")
    
    # 4. Feature Engineering: Calculate Average Order Value (AOV)
    df['average_order_value'] = (df['total_spent'] / df['total_orders']).round(2)
    
    # 5. Segmentation: Segment high-value clients (VIPs)
    # If they spent over $500, they are VIP. Otherwise, Standard.
    df['customer_segment'] = df['total_spent'].apply(lambda x: 'VIP' if x >= 500 else 'Standard')
    
    # Count how many VIPs we found
    vip_count = len(df[df['customer_segment'] == 'VIP'])
    print(f"[+] Engineered AOV metric and segmented {vip_count} VIP customers.")
    
    # 6. Organize: Sort by total amount spent (Highest -> Lowest)
    df = df.sort_values(by="total_spent", ascending=False)
    
    # 7. Output: Save the clean, segmented marketing list
    df.to_csv("clean_marketing_list.csv", index=False)
    print("[✓] SUCCESS: 'clean_marketing_list.csv' generated and sorted.")
    print("------------------------------------------")

if __name__ == "__main__":
    run_sales_pipeline()