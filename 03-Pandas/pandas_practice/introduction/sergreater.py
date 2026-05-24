import pandas as pd
data = [100, 200, 300, 400, 500]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(s[s > 300])