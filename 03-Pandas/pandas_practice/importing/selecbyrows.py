import pandas as pd
df = pd.read_csv("Pokemon.csv")
print(df.loc[0])
#index_col = "Name" is used to set the index of the dataframe to the "Name" column
df = pd.read_csv("Pokemon.csv",index_col="Name")
print(df)
#finding the row with index "Pikachu"
print(df.loc["Pikachu"])
#finding the value of "Type 1" and "HP" for the row with index "Pikachu"    
print(df.loc["Pikachu", ["Type 1", "HP"]])
#finding the value of "Type 1" and "HP" for the row with index "Pikachu" using iloc
print(df.iloc[0, [0, 4]])
print(df.iloc[0:11])
pokemon = input("Enter the name of the pokemon: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"Pokemon '{pokemon}' not found.")