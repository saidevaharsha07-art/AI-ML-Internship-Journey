import pandas as pd
data = {
    "Employee": ["Ram", None, "Kiran", "Anu"],
    "Salary": [25000, 30000, None, 40000],
    "Department": ["HR", "IT", "Sales", None]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_clean = df.dropna()
print("\nDataFrame after dropna():")
print(df_clean)