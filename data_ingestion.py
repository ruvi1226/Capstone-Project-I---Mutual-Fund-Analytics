import pandas as pd
import os

path = "data/raw"

for file in os.listdir(path):

    if file.endswith(".csv"):

        print("="*60)
        print("FILE:", file)

        df = pd.read_csv(os.path.join(path,file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    