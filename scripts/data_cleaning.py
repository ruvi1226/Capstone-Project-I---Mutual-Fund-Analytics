import pandas as pd
import numpy as np
import os

nav = pd.read_csv("data/raw/02_nav_history.csv")

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# Clean 02_nav_history.csv

# parse dates to datetime
nav["date"] = pd.to_datetime(nav["date"])

# sort by amfi_code + date
nav = nav.sort_values(
    ["amfi_code","date"]
)

# forward-fill missing NAV for holidays/weekends
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# remove duplicates
nav = nav.drop_duplicates()
# validate NAV > 0
nav = nav[nav["nav"] > 0]


# saved the result to a new file 
nav.to_csv(
    "data/processed/02_nav_history.csv",
    index=False
)

print("02_nav_history.csv saved successfully!")

print("Rows saved:", len(nav))

# result outcome 
print("Rows before cleaning:", len(pd.read_csv("data/raw/02_nav_history.csv")))
print("Rows after cleaning:", len(nav))

# Clean 08_investor_transactions.csv
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)
# standardise transaction_type values (SIP/Lumpsum/Redemption)
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.lower()
)

# validate amount > 0, fix date formats
txn = txn[txn["amount_inr"] > 0]

# Fix Date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# check KYC status enum values.
valid = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid = txn[
    ~txn["kyc_status"].isin(valid)
]
print(invalid)

# saved the result to a new file 
txn.to_csv(
    "data/processed/08_investor_transactions.csv",
    index=False
)
print("08_investor_transactions.csv saved successfully!")

# Clean 07_scheme_performance.csv
scheme = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)
# validate all return values are numeric
returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:

    scheme[col] = pd.to_numeric(
        scheme[col],
        errors="coerce"
    )
# Flag Anomalies
anomaly = scheme[
    (scheme["return_1yr_pct"] > 100)
    |
    (scheme["return_1yr_pct"] < -100)
]
print(anomaly)

# check expense_ratio range (0.1% – 2.5%).
invalid = scheme[
    (scheme["expense_ratio_pct"] < 0.1)
    |
    (scheme["expense_ratio_pct"] > 2.5)
]
print(invalid)

print("Anomalies found:", len(anomaly))
print(anomaly)

print("Invalid expense ratios found:", len(invalid))
print(invalid)

# saved the result to a new file 
scheme.to_csv(
    "data/processed/07_scheme_performance.csv",
    index=False
)
print("07_scheme_performance.csv saved successfully!")