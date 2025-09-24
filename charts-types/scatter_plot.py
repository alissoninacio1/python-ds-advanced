"""
 Scatter plots show the RELATIONSHIP between two continuous variables.
 They are useful for IDENTIFYING PATTERNS OR CORRELATIONS between variables, 
 such as the relationship between age and income.
"""

import matplotlib.pyplot as plt #the same as: from matplotlib import pyplot as plt

ages = [25, 30, 35, 40, 45]
incomes = [500, 600, 550, 700, 650]

plt.scatter(ages, incomes)

plt.title("Relation between Ages and Incomes")
plt.xlabel("Ages")
plt.ylabel("Incomes")
plt.grid(True)

plt.show()


#-------------------
# This function is to plot automatically two lists

# def scatter_plot(list_one, list_two):
#     plt.scatter(list_one, list_two)

#     plt.title("Relation between Ages and Incomes")
#     plt.xlabel("Ages")
#     plt.ylabel("Incomes")
#     plt.grid(True)

#     plt.show()

# scatter_plot(ages, incomes)
