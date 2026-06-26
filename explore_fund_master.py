import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# print(df.columns)

# print(df["fund_house"].unique())

# print(df["category"].unique())

# print(df["sub_category"].unique())

# print(df["risk_category"].unique())

# print(df["fund_house"].nunique())

import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Print all column names
print("Columns:")
print(df.columns)

# Print unique values
print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk_Category:")
print(df["risk_category"].unique())


import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# Show column names
print(df.columns)

# Display first 5 AMFI codes
print(df["amfi_code"].head())

# Check uniqueness
print("Are AMFI codes unique?", df["amfi_code"].is_unique)

# Count unique codes
print("Total unique AMFI codes:", df["amfi_code"].nunique())

# Data type
print("Data type:", df["amfi_code"].dtype)