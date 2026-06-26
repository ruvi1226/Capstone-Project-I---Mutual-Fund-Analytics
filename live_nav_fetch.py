try:
    import requests
except ImportError:
    print("Error: 'requests' module not found. Install it using: pip install requests")
    exit()

try:
    import pandas as pd
except ImportError:
    print("Error: 'pandas' module not found. Install it using: pip install pandas")
    exit()

import os

# Create the output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Dictionary of scheme names and AMFI codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Loop through each scheme
for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{name}.csv"

        df.to_csv(filename, index=False)

        print(f"{name} data saved successfully!")

    else:
        print(f"Failed to fetch data for {name}")