
import pandas as pd
from sqlalchemy import create_engine, text

# Create database connection
engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned CSV
nav = pd.read_csv("data/processed/02_nav_history.csv")

# Load into SQLite
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("NAV table loaded successfully.")

# Verify row count
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM fact_nav"))
    print("Rows in SQLite:", result.scalar())  

# Create database connection
engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned CSV
nav = pd.read_csv("data/processed/07_scheme_performance.csv")

# Load into SQLite
nav.to_sql(
    "fact_scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Scheme Performance table loaded successfully.")

# Verify row count
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM fact_scheme_performance"))
    print("Rows in SQLite:", result.scalar())      


# Create database connection
engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned CSV
nav = pd.read_csv("data/processed/08_investor_transactions.csv")

# Load into SQLite
nav.to_sql(
    "fact_investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Investor Transactions table loaded successfully.")

# Verify row count
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM fact_investor_transactions"))
    print("Rows in SQLite:", result.scalar())    


# Verify Data Loaded
from sqlalchemy import text

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT COUNT(*) FROM fact_nav")
    )

    print(result.scalar())    