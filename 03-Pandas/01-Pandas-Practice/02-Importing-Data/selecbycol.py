import pandas as pd
df = pd.read_csv("Pokemon.csv")
#print(df["Name"].to_string())
#print(df[["Type 1"]].to_string())
#print(df[["HP"]].to_string())
print(df[["Name", "Type 1", "HP"]].to_string())