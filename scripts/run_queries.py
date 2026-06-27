import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")
# QUERY 1– Top 5 Funds by AUM
print("\n========== Query 1 ==========")
print("Top 5 Funds by AUM\n")

query1 = """
SELECT *
FROM fact_nav
ORDER BY amfi_code DESC
LIMIT 5;
"""
print(pd.read_sql(query1, conn))

# QUERY 2
print("\n========== Query 2 ==========")
print("Average NAV Per Month\n")

query2 = """
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date);
"""
print(pd.read_sql(query2, conn))


# Query 3 – SIP Year-wise Growth
print("\n========== Query 3 ==========")

query3 = """
SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS total_sip
FROM fact_investor_transactions
WHERE transaction_type='sip'
GROUP BY year;
"""

print(pd.read_sql(query3, conn))

# Query 4 – Transactions by State
print("\n========== Query 4 ==========")

query4 = """
SELECT
state,
COUNT(*) AS total_transactions
FROM fact_investor_transactions
GROUP BY state;
"""

print(pd.read_sql(query4, conn))

# Query 5 – Expense Ratio Less Than 1%
print("\n========== Query 5 ==========")

query5 = """
SELECT
scheme_name,
expense_ratio_pct
FROM fact_scheme_performance
WHERE expense_ratio_pct < 1;
"""

print(pd.read_sql(query5, conn))

# Query 6 – Top 10 Funds by 1-Year Return
print("\n========== Query 6 ==========")

query6 = """
SELECT
scheme_name,
return_1yr_pct
FROM fact_scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;
"""

print(pd.read_sql(query6, conn))

# Query 7 – Monthly Transaction Count
print("\n========== Query 7 ==========")

query7 = """
SELECT
strftime('%Y-%m', transaction_date) AS month,
COUNT(*) AS transactions
FROM fact_investor_transactions
GROUP BY month;
"""

print(pd.read_sql(query7, conn))

# Query 8 – Average Amount by Transaction Type
print("\n========== Query 8 ==========")

query8 = """
SELECT
transaction_type,
AVG(amount_inr) AS average_amount
FROM fact_investor_transactions
GROUP BY transaction_type;
"""

print(pd.read_sql(query8, conn))

# Query 9 – Total AUM by Category
print("\n========== Query 9 ==========")

query9 = """
SELECT
category,
SUM(aum_crore) AS total_aum
FROM fact_scheme_performance
GROUP BY category;
"""

print(pd.read_sql(query9, conn))

# Query 10 – Highest Redemption
print("\n========== Query 10 ==========")

query10 = """
SELECT
investor_id,
amount_inr
FROM fact_investor_transactions
WHERE transaction_type='redemption'
ORDER BY amount_inr DESC
LIMIT 5;
"""

print(pd.read_sql(query10, conn))

conn.close()

print("\nAll queries executed successfully.")