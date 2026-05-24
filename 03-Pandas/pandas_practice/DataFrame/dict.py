import pandas as pd
# Creating a DataFrame from a dictionary
data = {"Name": ["Spongebob", "Patrick", "Squidward", "Sandy", "Mr. Krabs"],
        "Age": [20, 21, 30, 25, 50],}
df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3', 'Employee 4', 'Employee 5'])
print(df)
# Accessing a specific row using loc
print(df.loc['Employee 3'])
# Accessing a specific value using iloc
print(df.iloc[2]) 
# Adding a new column to the DataFrame
df["Job"] = ["Fry Cook", "Starfish", "Cashier", "Scientist", "Owner"]
print("\n",df)
# Adding a new rows to the DataFrame
new_row = pd.DataFrame({"Name": ["Plankton"], "Age": [40], "Job": ["Rival"]}, index=['Employee 6'])
new_row2 = pd.DataFrame({"Name": ["Harsha"], "Age": [14], "Job": ["Manager"]}, index=['Employee 7'])
df = pd.concat([df, new_row, new_row2])
print("\n",df)