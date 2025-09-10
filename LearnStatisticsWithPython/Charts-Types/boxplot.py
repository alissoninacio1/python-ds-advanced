"""
Box plots (diagrama de caixas) are useful for visualizing the DISTRIBUTION OF A NUMERICAL VARIABLE and for identifying outliers (valores atipicos). 
They provide information about the median, quartiles, and extreme values ​​of a data set.

"""

import matplotlib.pyplot as plt

data = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

plt.boxplot(data)

plt.title("Box plot of ages")

plt.show()