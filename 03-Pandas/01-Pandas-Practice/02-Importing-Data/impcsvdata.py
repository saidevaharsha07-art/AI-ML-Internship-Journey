import pandas as pd
df = pd.read_csv("Pokemon.csv")
print(df.to_string())
df = pd.read_json("Pokemon.json", orient="records")
print(df.to_string())
