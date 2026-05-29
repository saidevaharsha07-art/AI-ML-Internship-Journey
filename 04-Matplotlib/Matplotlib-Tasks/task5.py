import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7]
temp = [32, 34, 35, 33, 31, 30, 29]
humidity = [60, 65, 70, 68, 64, 62, 61]
# Temperature line
plt.plot(days, temp,
         marker="o",
         label="Temperature")
# Humidity line
plt.plot(days, humidity,
         marker="s",
         label="Humidity")
plt.title("Weather Analytics Dashboard")
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()