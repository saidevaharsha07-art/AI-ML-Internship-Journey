import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May","Jun"]
expenses = [12000,15000,11000,18000,17000,16000]
plt.plot(months, expenses, marker="o", color="red")
plt.title("Monthly Expenses")
plt.grid()
plt.xlabel("Months")
plt.ylabel("Expenses ($)")
plt.show()