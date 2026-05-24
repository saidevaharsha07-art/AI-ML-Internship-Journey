import pandas as pd
data = [100, 200, 300, 400, 500]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
s.loc['c'] = 350
print(s)