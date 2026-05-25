import pandas as pd
data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [80, None, 75, 90]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print("\nMean Marks:", mean_marks)
print("\nUpdated DataFrame:")
print(df)