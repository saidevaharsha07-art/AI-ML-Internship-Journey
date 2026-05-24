import pandas as pd
df = pd.read_csv("Pokemon.csv")
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())

#Single column
#print(df["HP"].mean())
#print(df["HP"].sum())
#print(df["HP"].min())
#print(df["HP"].max())
#print(df["HP"].count())

#groupby
#print(df.groupby("Type 1")["HP"].mean())
#print(df.groupby("Type 1")["HP"].sum())

#group = df.groupby("Type 1")
#print(group["HP"].mean())
#print(group["HP"].sum())
#print(group["HP"].min())
#print(group["HP"].max())
#print(group["HP"].count())