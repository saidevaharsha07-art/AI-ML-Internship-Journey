# Dashboard with 4 different types of plots: Line Plot, Bar Plot, Pie Chart, and Histogram. 
# Each plot should represent a different aspect of the data.
import matplotlib.pyplot as plt
students = ["A", "B", "C", "D", "E"]
math = [85, 90, 78, 92, 88]
science = [80, 95, 75, 89, 91]
plt.figure(figsize=(10, 8))
# 1. Line Plot
plt.subplot(2, 2, 1)
plt.plot(students, math, marker="o", label="Math")
plt.plot(students, science, marker="o", label="Science")
plt.title("Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
# 2. Bar Plot
plt.subplot(2, 2, 2)
plt.bar(students, math, label="Math")
plt.title("Math Marks Bar Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
# 3. Pie Chart
plt.subplot(2, 2, 3)
plt.pie(math, labels=students, autopct="%1.1f%%")
plt.title("Math Marks Pie Chart")
# 4. Histogram
plt.subplot(2, 2, 4)
plt.hist(science, bins=5, edgecolor="black")
plt.title("Science Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()