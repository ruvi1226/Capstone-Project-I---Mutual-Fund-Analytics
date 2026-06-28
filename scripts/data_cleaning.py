from ast import Load

import pandas as pd
import numpy as np
import os

nav = pd.read_csv("data/raw/02_nav_history.csv")

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
# # Clean 02_nav_history.csv

# # parse dates to datetime
# nav["date"] = pd.to_datetime(nav["date"])

# # sort by amfi_code + date
# nav = nav.sort_values(
#     ["amfi_code","date"]
# )

# # forward-fill missing NAV for holidays/weekends
# nav["nav"] = nav.groupby(
#     "amfi_code"
# )["nav"].ffill()

# # remove duplicates
# nav = nav.drop_duplicates()
# # validate NAV > 0
# nav = nav[nav["nav"] > 0]


# # saved the result to a new file 
# nav.to_csv(
#     "data/processed/02_nav_history.csv",
#     index=False
# )

# print("02_nav_history.csv saved successfully!")

# print("Rows saved:", len(nav))

# # result outcome 
# print("Rows before cleaning:", len(pd.read_csv("data/raw/02_nav_history.csv")))
# print("Rows after cleaning:", len(nav))

# # Clean 08_investor_transactions.csv
# txn = pd.read_csv(
#     "data/raw/08_investor_transactions.csv"
# )
# # standardise transaction_type values (SIP/Lumpsum/Redemption)
# txn["transaction_type"] = (
#     txn["transaction_type"]
#     .str.strip()
#     .str.lower()
# )

# # validate amount > 0, fix date formats
# txn = txn[txn["amount_inr"] > 0]

# # Fix Date
# txn["transaction_date"] = pd.to_datetime(
#     txn["transaction_date"]
# )

# # check KYC status enum values.
# valid = [
#     "Verified",
#     "Pending",
#     "Rejected"
# ]

# invalid = txn[
#     ~txn["kyc_status"].isin(valid)
# ]
# print(invalid)

# # saved the result to a new file 
# txn.to_csv(
#     "data/processed/08_investor_transactions.csv",
#     index=False
# )
# print("08_investor_transactions.csv saved successfully!")

# # Clean 07_scheme_performance.csv
# scheme = pd.read_csv(
#     "data/raw/07_scheme_performance.csv"
# )
# # validate all return values are numeric
# returns = [
#     "return_1yr_pct",
#     "return_3yr_pct",
#     "return_5yr_pct"
# ]

# for col in returns:

#     scheme[col] = pd.to_numeric(
#         scheme[col],
#         errors="coerce"
#     )
# # Flag Anomalies
# anomaly = scheme[
#     (scheme["return_1yr_pct"] > 100)
#     |
#     (scheme["return_1yr_pct"] < -100)
# ]
# print(anomaly)

# # check expense_ratio range (0.1% – 2.5%).
# invalid = scheme[
#     (scheme["expense_ratio_pct"] < 0.1)
#     |
#     (scheme["expense_ratio_pct"] > 2.5)
# ]
# print(invalid)

# print("Anomalies found:", len(anomaly))
# print(anomaly)

# print("Invalid expense ratios found:", len(invalid))
# print(invalid)

# # saved the result to a new file 
# scheme.to_csv(
#     "data/processed/07_scheme_performance.csv",
#     index=False
# )
# print("07_scheme_performance.csv saved successfully!")

# Clean 03_aum_by_fund_house.csv
# print(aum.head())
# print(aum.info())
# print(aum.isnull().sum())

# # Convert Date
# aum["date"] = pd.to_datetime(aum["date"])
# print(aum.dtypes)

# # Sort the Data
# aum = aum.sort_values(
#     by=["fund_house", "date"]
# )

# # Forward-fill missing AUM values for each fund house
# aum["aum_crore"] = aum.groupby("fund_house")["aum_crore"].ffill()   

# # Remove Duplicate Rows
# duplicates = aum.duplicated().sum()

# print("Duplicate rows:", duplicates)

# aum = aum.drop_duplicates()

# print(aum.isnull().sum())
# aum["aum_crore"] = aum["aum_crore"].fillna(0)
# aum["aum_lakh_crore"] = aum["aum_lakh_crore"].fillna(0)

# # Save the Cleaned File
# aum.to_csv(
#     "data/processed/03_aum_by_fund_house.csv",
#     index=False
# )
# print("03_aum_by_fund_house.csv saved successfully!")

# category = pd.read_csv("data/raw/05_category_inflows.csv")

# print("Dataset Loaded Successfully!\n")

# # Display First 5 Rows

# print(category.head())

# # Display Dataset Information

# print("\nDataset Information\n")

# print(category.info())

# #  Check Missing Values

# print("\nMissing Values\n")

# print(category.isnull().sum())

# # Convert Month Column to Datetime

# category["month"] = pd.to_datetime(category["month"])

# # Remove Extra Spaces

# category["category"] = category["category"].str.strip()

# # Standardize Category Names
# category["category"] = category["category"].str.title()

# # Sort Dataset

# category = category.sort_values(
#     by=["month", "category"]
# )

# # Remove Duplicate Rows

# duplicates = category.duplicated().sum()

# print("\nDuplicate Rows :", duplicates)

# category = category.drop_duplicates()

# # Convert Inflow Column to Numeric

# category["net_inflow_crore"] = pd.to_numeric(
#     category["net_inflow_crore"],
#     errors="coerce"
# )

# # Check Missing Values Again

# print("\nMissing Values After Conversion\n")

# print(category.isnull().sum())

# # Remove Invalid Rows

# # If inflow is missing, remove that row

# category = category.dropna(subset=["net_inflow_crore"])


# # Check for Extreme Values

# print("\nTop 10 Highest Inflows\n")

# print(
#     category.sort_values(
#         "net_inflow_crore",
#         ascending=False
#     ).head(10)
# )

# print("\nTop 10 Lowest Inflows\n")

# print(
#     category.sort_values(
#         "net_inflow_crore",
#         ascending=True
#     ).head(10)
# )

# print("\nFinal Shape")

# print(category.shape)

# # Save Clean Dataset

# category.to_csv(
#     "data/processed/05_category_inflows.csv",
#     index=False
# )

# print("05_category_inflows.csv saved successfully!")

# Data Cleaning Script for 01_fund_master.csv
# Load Dataset

# fund = pd.read_csv("data/raw/01_fund_master.csv")

# print("Dataset Loaded Successfully!\n")

# # Display Dataset Information

# print(fund.head())

# print("\nDataset Information\n")

# print(fund.info())

# # Check Missing Values

# print("\nMissing Values\n")

# print(fund.isnull().sum())

# # Convert Launch Date to Datetime

# fund["launch_date"] = pd.to_datetime(
#     fund["launch_date"],
#     errors="coerce"
# )

# # Remove Extra Spaces

# text_columns = [

#     "fund_house",

#     "scheme_name",

#     "category",

#     "sub_category",

#     "plan",

#     "benchmark",

#     "fund_manager",

#     "risk_category",

#     "sebi_category_code"

# ]

# for col in text_columns:

#     fund[col] = fund[col].str.strip()


# # Remove Duplicate Rows

# duplicates = fund.duplicated().sum()

# print("\nDuplicate Rows :", duplicates)

# fund = fund.drop_duplicates()

# # Check Unique AMFI Codes

# duplicate_codes = fund["amfi_code"].duplicated().sum()

# print("\nDuplicate AMFI Codes :", duplicate_codes)

# # Convert Numeric Columns

# numeric_columns = [

#     "expense_ratio_pct",

#     "exit_load_pct",

#     "min_sip_amount",

#     "min_lumpsum_amount"

# ]

# for col in numeric_columns:

#     fund[col] = pd.to_numeric(
#         fund[col],
#         errors="coerce"
#     )

# # Validate Expense Ratio

# # Valid range : 0.1% to 2.5%

# invalid_expense = fund[
#     (fund["expense_ratio_pct"] < 0.1) |
#     (fund["expense_ratio_pct"] > 2.5)
# ]

# print("\nInvalid Expense Ratio Rows")

# print(invalid_expense)

# # Validate Exit Load

# # Exit load cannot be negative

# fund = fund[fund["exit_load_pct"] >= 0]

# # Validate Minimum Investment Amounts

# fund = fund[fund["min_sip_amount"] > 0]

# fund = fund[fund["min_lumpsum_amount"] > 0]

# # Standardize Risk Category

# fund["risk_category"] = fund["risk_category"].str.title()

# valid_risk = [

#     "Low",

#     "Moderate",

#     "Moderately High",

#     "High",

#     "Very High"

# ]

# invalid_risk = fund[
#     ~fund["risk_category"].isin(valid_risk)
# ]

# print("\nInvalid Risk Categories")

# print(invalid_risk)

# #  Sort Dataset

# fund = fund.sort_values(
#     by=["fund_house", "scheme_name"]
# )

# # Final Dataset Shape

# print("\nFinal Shape")

# print(fund.shape)

# #  Save Clean Dataset

# fund.to_csv(
#     "data/processed/01_fund_master.csv",
#     index=False
# )
# print("01_fund_master.csv saved successfully!")

# Data Cleaning Script for 06_industry_folio_count.csv
# Load Dataset

# folio_count = pd.read_csv("data/raw/06_industry_folio_count.csv")

# print("Dataset Loaded Successfully!\n")


# # Display First Five Rows

# print(folio_count.head())

# # Display Dataset Information

# print("\nDataset Information\n")

# print(folio_count.info())

# # Check Missing Values

# print("\nMissing Values\n")

# print(folio_count.isnull().sum())

# # Convert Month to Datetime

# folio_count["month"] = pd.to_datetime(
#     folio_count["month"],
#     errors="coerce"
# )

# # Sort Dataset by Month

# folio_count = folio_count.sort_values("month")

# # Remove Duplicate Rows

# duplicates = folio_count.duplicated().sum()

# print("\nDuplicate Rows :", duplicates)

# folio_count = folio_count.drop_duplicates()

# # Convert Numeric Columns

# numeric_columns = [

#     "total_folios_crore",

#     "equity_folios_crore",

#     "debt_folios_crore",

#     "hybrid_folios_crore",

#     "others_folios_crore"

# ]

# for col in numeric_columns:

#     folio_count[col] = pd.to_numeric(
#         folio_count[col],
#         errors="coerce"
#     )

# # Check Missing Values Again

# print("\nMissing Values After Conversion\n")

# print(folio_count.isnull().sum())

# # Remove Rows with Missing Values

# folio_count = folio_count.dropna()

# # Validate Folio Counts

# # Folio counts should never be negative

# for col in numeric_columns:

#     folio_count = folio_count[folio_count[col] >= 0]

# # Verify Total Folios

# # The total folios should generally be greater than or equal to
# # the sum of the category-wise folios.

# folio_count["category_total"] = (

#     folio_count["equity_folios_crore"]

#     + folio_count["debt_folios_crore"]

#     + folio_count["hybrid_folios_crore"]

#     + folio_count["others_folios_crore"]

# )

# # Display rows where the difference is more than 0.05 crore

# difference = abs(folio_count["total_folios_crore"] - folio_count["category_total"])

# anomalies = folio_count[difference > 0.05]

# print("\nPossible Anomalies")

# print(anomalies)

# # Remove helper column

# folio_count.drop(columns=["category_total"], inplace=True)

# #  Display Highest Folio Counts

# print("\nTop 5 Total Folio Counts")

# print(

#     folio_count.sort_values(

#         "total_folios_crore",

#         ascending=False

#     ).head()

# )

# # Final Dataset Shape

# print("\nFinal Dataset Shape")

# print(folio_count.shape)

# # Save Clean Dataset

# folio_count.to_csv(

#     "data/processed/06_industry_folio_count.csv",

#     index=False

# )

# print("06_industry_folio_count.csv saved successfully!")

# # Data Cleaning Script for 04_monthly_sip_inflows.csv
# # Load CSV
# sip= pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
# print("Dataset Loaded Successfully\n")

# # Display Basic Information

# print(sip.head())

# print("\nDataset Information\n")

# print(sip.info())

# # Check Missing Values

# print("\nMissing Values\n")

# print(sip.isnull().sum())

# # Convert Month Column

# # Convert text into datetime

# sip["month"] = pd.to_datetime(sip["month"])

# # Sort Dataset

# sip = sip.sort_values("month")

# # Remove Duplicate Rows

# duplicates = sip.duplicated().sum()

# print("\nDuplicate Rows :", duplicates)

# sip = sip.drop_duplicates()

# # Convert Numeric Columns

# numeric_columns = [

#     "sip_inflow_crore",

#     "active_sip_accounts_crore",

#     "new_sip_accounts_lakh",

#     "sip_aum_lakh_crore",

#     "yoy_growth_pct"

# ]

# for col in numeric_columns:

#     sip[col] = pd.to_numeric(
#         sip[col],

#         errors="coerce"

#     )

# # Handle Missing Values

# # YoY Growth can be blank for the first year.
# # Replace missing values with 0.

# sip["yoy_growth_pct"] = sip["yoy_growth_pct"].fillna(0)

# # Validate Values

# # SIP Inflow should never be negative

# sip = sip[sip["sip_inflow_crore"] >= 0]

# # Active SIP Accounts

# sip = sip[sip["active_sip_accounts_crore"] >= 0]

# # New SIP Accounts

# sip = sip[sip["new_sip_accounts_lakh"] >= 0]

# # SIP AUM

# sip = sip[sip["sip_aum_lakh_crore"] >= 0]

# # Check Outliers

# print("\nLargest SIP Inflows\n")

# print(

#     sip.sort_values(

#         "sip_inflow_crore",

#         ascending=False

#     ).head()

# )

# # Final Dataset Info

# print("\nFinal Dataset Shape")

# print(sip.shape)

# # Save Clean Dataset

# sip.to_csv(

#     "data/processed/04_monthly_sip_inflows.csv",

#     index=False

# )

# print("04_monthly_sip_inflows.csv saved successfully!")


# # Data Cleaning Script for 09_portfolio_holdings.csv
# # Load Dataset
# portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# print("Dataset Loaded Successfully!\n")

# # Display Dataset Information

# print(portfolio.head())

# print("\nDataset Information\n")

# print(portfolio.info())

# # Check Missing Values

# print("\nMissing Values\n")

# print(portfolio.isnull().sum())

# # Convert Portfolio Date

# portfolio["portfolio_date"] = pd.to_datetime(
#     portfolio["portfolio_date"],
#     errors="coerce"
# )

# # Remove Extra Spaces

# text_columns = [

#     "stock_symbol",

#     "stock_name",

#     "sector"

# ]

# for col in text_columns:

#     portfolio[col] = portfolio[col].str.strip()

# # Remove Duplicate Rows

# duplicates = portfolio.duplicated().sum()

# print("\nDuplicate Rows :", duplicates)

# portfolio = portfolio.drop_duplicates()

# # Convert Numeric Columns

# numeric_columns = [

#     "weight_pct",

#     "market_value_cr",

#     "current_price_inr"

# ]

# for col in numeric_columns:

#     portfolio[col] = pd.to_numeric(
#         portfolio[col],
#         errors="coerce"
#     )

# # Remove Missing Values

# portfolio = portfolio.dropna()

# # Validate Weight Percentage
# # Weight must be between 0 and 100

# invalid_weight = portfolio[
#     (portfolio["weight_pct"] < 0) |
#     (portfolio["weight_pct"] > 100)
# ]

# print("\nInvalid Weight Percentage")

# print(invalid_weight)

# # Keep only valid records

# portfolio = portfolio[
#     (portfolio["weight_pct"] >= 0) &
#     (portfolio["weight_pct"] <= 100)
# ]

# # Validate Market Value

# portfolio = portfolio[portfolio["market_value_cr"] > 0]

# # Validate Current Price

# portfolio = portfolio[portfolio["current_price_inr"] > 0]

# # Sort Dataset
# portfolio = portfolio.sort_values(
#     by=["amfi_code", "portfolio_date", "weight_pct"],
#     ascending=[True, True, False]
# )

# # Display Top Holdings

# print("\nTop Holdings by Weight\n")

# print(
#     portfolio[
#         ["stock_name", "weight_pct"]
#     ].sort_values(
#         "weight_pct",
#         ascending=False
#     ).head(10)
# )

# #  Final Dataset Shape

# print("\nFinal Dataset Shape")

# print(portfolio.shape)

# #  Save Clean Dataset

# portfolio.to_csv(
#     "data/processed/09_portfolio_holdings.csv",
#     index=False
# )

# print("09_portfolio_holdings.csv saved successfully!")

# Data Cleaning Script for 10_benchmarks_indices.csv
# Load Dataset

#  Load Dataset
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Dataset Loaded Successfully!\n")

# Display Dataset

print(benchmark.head())

print("\nDataset Information\n")

print(benchmark.info())

# Check Missing Values

print("\nMissing Values\n")

print(benchmark.isnull().sum())

# Convert Date Column

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

# Remove Extra Spaces

benchmark["index_name"] = benchmark["index_name"].str.strip()

# Optional:
# Convert all index names to uppercase
# (Nifty50 -> NIFTY50)

benchmark["index_name"] = benchmark["index_name"].str.upper()

# Remove Duplicate Rows

duplicates = benchmark.duplicated().sum()

print("\nDuplicate Rows :", duplicates)

benchmark = benchmark.drop_duplicates()

# Convert Close Value to Numeric

benchmark["close_value"] = pd.to_numeric(
    benchmark["close_value"],
    errors="coerce"
)

# Remove Missing Values

benchmark = benchmark.dropna()

# Validate Closing Value

# Index value should always be greater than zero

invalid_close = benchmark[benchmark["close_value"] <= 0]

print("\nInvalid Closing Values")

print(invalid_close)

# Keep only valid records

benchmark = benchmark[benchmark["close_value"] > 0]

# Sort Dataset

benchmark = benchmark.sort_values(
    by=["index_name", "date"]
)

# Display Latest Benchmark Values

print("\nLatest Benchmark Values\n")

latest = (
    benchmark.sort_values("date")
      .groupby("index_name")
      .tail(1)
)

print(latest)

# Final Dataset Shape

print("\nFinal Dataset Shape")

print(benchmark.shape)

# Save Clean Dataset

benchmark.to_csv(
    "data/processed/10_benchmark_indices.csv",
    index=False
)

print("10_benchmark_indices.csv saved successfully!")