# Mutual Fund Analytics - Data Dictionary
## Dataset: 02_nav_history.csv

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | Integer | Unique AMFI code of the mutual fund | AMFI |
| date | Date | Date on which NAV was recorded | AMFI |
| nav | Float | Net Asset Value of the fund | AMFI |

## Dataset: 08_investor_transactions.csv

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| investor_id | Integer | Unique investor ID | Internal |
| transaction_date | Date | Date of transaction | Internal |
| transaction_type | Text | SIP, Lumpsum or Redemption | Internal |
| amount | Float | Transaction amount | Internal |
| state | Text | State of the investor | Internal |
| kyc_status | Text | KYC verification status | Internal |

## Dataset: scheme_performance.csv

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| scheme_name | Text | Name of the mutual fund scheme | AMFI |
| return_1yr_pct | Float | 1-year return percentage | AMFI |
| return_3yr_pct | Float | 3-year return percentage | AMFI |
| return_5yr_pct | Float | 5-year return percentage | AMFI |
| expense_ratio_pct | Float | Expense ratio charged by the fund | AMFI |
| aum_crore | Float | Assets Under Management (Crores) | AMFI |
| risk_grade | Text | Risk category of the scheme | AMFI |


## Dataset: 01_fund_master.csv

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | Integer | Unique AMFI code assigned to each mutual fund scheme | AMFI |
| fund_house | Text | Name of the Asset Management Company (AMC) | AMFI |
| scheme_name | Text | Name of the mutual fund scheme | AMFI |
| category | Text | Primary fund category | AMFI |
| sub_category | Text | Detailed scheme category | AMFI |
| plan | Text | Direct or Regular plan | AMFI |
| launch_date | Date | Scheme launch date | AMFI |
| benchmark | Text | Benchmark index used for comparison | AMFI |
| expense_ratio_pct | Float | Expense ratio charged annually (%) | AMFI |
| exit_load_pct | Float | Exit load percentage applicable on redemption | AMFI |
| min_sip_amount | Integer | Minimum SIP investment amount | AMFI |
| min_lumpsum_amount | Integer | Minimum one-time investment amount | AMFI |
| fund_manager | Text | Name of the fund manager | AMFI |
| risk_category | Text | Risk level of the scheme | AMFI |
| sebi_category_code | Text | SEBI category code | AMFI |