"""
Bar graphs are excellent for COMPARING QUANTITIES between different categories. 
They are useful for viewing categorical data and can be horizontal or vertical. 
For example, it can be used to compare quarterly sales by region or to show gender distribution in a population.

"""

import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West"]
sellings = [4500, 4200, 5000, 4700]


plt.bar(regions, sellings)

plt.title("Sellings by region")
plt.xlabel("Region")
plt.ylabel("Sellings ($)")
plt.grid(axis="y")

plt.show()