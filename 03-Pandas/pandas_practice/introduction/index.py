import pandas as pd
data = [100, 200, 300, 400, 500]
s = pd.Series(data, index=['apartment A', 'apartment B', 'apartment C', 'apartment D', 'apartment E'])
print(s)