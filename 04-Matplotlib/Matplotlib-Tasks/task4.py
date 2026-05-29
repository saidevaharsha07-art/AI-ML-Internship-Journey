import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Pokemon.csv")
plt.figure(figsize=(12, 10))
# 1. Top 10 Pokemon by HP
top_hp = df.nlargest(10, "HP")
plt.subplot(2, 2, 1)
plt.bar(top_hp["Name"], top_hp["HP"])
plt.title("Top 10 Pokemon by HP")
plt.xlabel("Pokemon")
plt.ylabel("HP")
plt.xticks(rotation=45)
# 2. Attack Distribution
plt.subplot(2, 2, 2)
plt.hist(df["Attack"], bins=10, edgecolor="black")
plt.title("Attack Distribution")
plt.xlabel("Attack")
plt.ylabel("Frequency")
# 3. Attack vs Defense
plt.subplot(2, 2, 3)
plt.scatter(df["Attack"], df["Defense"])
plt.title("Attack vs Defense")
plt.xlabel("Attack")
plt.ylabel("Defense")
# 4. Pokemon Type Distribution
type_counts = df["Type 1"].value_counts().head(5)
plt.subplot(2, 2, 4)
plt.pie(type_counts,
        labels=type_counts.index,
        autopct="%1.1f%%")
plt.title("Top 5 Pokemon Types")
plt.tight_layout()
plt.show()