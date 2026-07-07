import pandas as pd
import numpy as np

# Generate 100 raw customer records
np.random.seed(24)
data = {
    "customer_id": range(1001, 1101),
    "name": [f"Customer_{i}" for i in range(100)],
    "email": [f"user_{i}@example.com" if np.random.rand() > 0.15 else np.nan for i in range(100)],
    "total_orders": np.random.randint(1, 25, size=100),
    "total_spent": np.random.uniform(15.50, 1200.00, size=100).round(2),
    "country": np.random.choice(["US", "CA", "UK", "Unknown", None], size=100, p=[0.6, 0.1, 0.1, 0.1, 0.1])
}

df = pd.DataFrame(data)

# Inject some identical duplicate rows to simulate messy platform exports
df = pd.concat([df, df.iloc[[8, 45, 45]]], ignore_index=True)

# Save raw file
df.to_csv("raw_ecommerce_data.csv", index=False)
print("SUCCESS: 'raw_ecommerce_data.csv' created with duplicates and missing emails.")