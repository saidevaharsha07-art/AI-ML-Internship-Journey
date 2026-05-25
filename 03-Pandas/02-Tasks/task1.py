import pandas as pd
names = ["Ravi", "Anu", "Kiran"]
employees = pd.Series(names, index=["E1", "E2", "E3"])
print(employees)