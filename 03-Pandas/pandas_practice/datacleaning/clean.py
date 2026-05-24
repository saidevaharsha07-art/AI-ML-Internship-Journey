import pandas as pd
df = pd.read_csv("Pokemon.csv")

#Data Cleaning = the process of identifying and correcting or removing 
#                   errors, inconsistencies, and inaccuracies in a dataset to 
#                   improve its quality and reliability for analysis. It involves 
#                   handling missing data, fixing inconsistent values, standardizing text, 
#                   and ensuring data types are correct.

#Data Cleaning Steps
#1.Drop irrelevant columns
#df.drop(columns=["Legendary","#"], inplace=True)
#print(df)

#2. Handle missing data
#df = df.dropna(subset=["Type 2"])
#df = df.fillna({"Type 2": "None"})
#print(df.to_string())      

#3.Fix inconsistent values
#df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS","Fire": "FIRE", "Water": "WATER"})
#df["Type 2"] = df["Type 2"].str.capitalize()

#4. Standardize Text
#df["Name"] = df["Name"].str.lower()
#df["Name"] = df["Name"].str.title()
#df["Name"] = df["Name"].str.upper()
#df["Name"] = df["Name"].str.strip()

#5. Fix data types
#df["HP"] = df["HP"].astype(float)

#6. Remove duplicates
#df = df.drop_duplicates()
#print(df.to_string())   