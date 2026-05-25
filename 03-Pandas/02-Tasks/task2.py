import pandas as pd
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Sneha"],
    "Age": [20, 21, 22, 20],
    "Course": ["Python", "Java", "Data Science", "AI"],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
print("Student Records:")
print(df)
print("\nColumn Names:")
print(df.columns)