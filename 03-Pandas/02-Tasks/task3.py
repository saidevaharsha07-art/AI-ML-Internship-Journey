import pandas as pd
data = {
    "Name": ["Ravi", "Anu", None, "Sneha"],
    "Marks": [85, None, 78, 90],
    "Course": ["Python", "Java", None, "AI"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df = df.fillna({
    "Name": "Unknown",
    "Marks": 0,
    "Course": "Not Assigned"
})
print("\nDataFrame after fillna():")
print(df)