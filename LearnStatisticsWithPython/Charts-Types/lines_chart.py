
"""
Line graphs are ideal for showing TRENDS OVER TIME or in sequence. 
They are effective for viewing TIME SERIES DATA, such as the price of stocks over several months or years, 
or the average monthly temperature.
"""


import matplotlib.pyplot as plt

#data
months = ["January", "February", "March", "April", "May"]
incomes = [100, 200, 300, 400, 500]

#create line chart
# Using 'o' as part of the format string to specify circle markers and a solid line
plt.plot(months, incomes, marker="o")

plt.title("Montly Incomes")
plt.xlabel("Month")
plt.ylabel("Incomes ($)")
plt.grid(True)

plt.show()

