import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file))

        print("\n" + "="*50)
        print("File:", file)
        print("Shape:", df.shape)
        print(df.head())