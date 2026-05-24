import pandas as pd
calories = {'day1': 200, 'day2': 250, 'day3': 300, 'day4': 350, 'day5': 400}
s = pd.Series(calories)
print(s.loc['day3'])
s.loc['day3'] = 320
print(s)
print(s[s > 300])
print(s[s < 300])