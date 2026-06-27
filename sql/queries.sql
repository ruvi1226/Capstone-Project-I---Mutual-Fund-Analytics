-- Top 5 Funds by AUM
SELECT
    scheme_name     
FROM fact_nav
ORDER BY amfi_code DESC
LIMIT 5;

-- Average NAV Per Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date);

-- SIP Year-over-Year Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip
FROM fact_investor_transactions
WHERE transaction_type='sip'
GROUP BY year;

-- Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_investor_transactions
GROUP BY state;

-- Funds with Expense Ratio Less Than 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_scheme_performance
WHERE expense_ratio_pct < 1;

-- Top 10 Funds by 1-Year Return
SELECT
    scheme_name,
    return_1yr_pct
FROM fact_scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- Monthly Transaction Volume
SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS transactions
FROM fact_investor_transactions
GROUP BY month;

-- Average Investment Amount by Transaction Type
SELECT
    transaction_type,
    AVG(amount_inr) AS average_amount
FROM fact_investor_transactions
GROUP BY transaction_type;

-- Top 5 Funds by 3-Year Return
SELECT
    scheme_name,
    return_3yr_pct  
FROM fact_scheme_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- Total AUM by Fund Category

SELECT
    fund_category,
    SUM(aum_crore) AS total_aum
FROM fact_scheme_performance
GROUP BY fund_category  

-- Highest Redemption Amount

SELECT
    scheme_name,
    MAX(amount_inr) AS highest_redemption  
FROM fact_investor_transactions
WHERE transaction_type='redemption'
