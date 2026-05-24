import pandas as pd
data = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard']
s = pd.Series(data, index=[1, 2, 3, 4, 5, 6])
print(s)