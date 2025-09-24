"""
The mean/average

- often referred to as the average, is a way to measure the center of a dataset.

The average of a set is calculated using a two-step process:
# Add all of the observations in your dataset.
# Divide the total sum from step one by the number of points in your dataset.


x = (x1 + x2 ... + xn) / n 

or

mean = sum of all values / number of values

"""


import numpy as np

average_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36])
mean_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

average_result = np.average(average_array)
mean_result = np.mean(mean_array)

print(average_result)
print(mean_result)



#considerations:

# * Use numpy instead of doing the calculation by yourself
# *numpy allow to use arrays. Arrays must be of the same data type
#  for numerical computing, memory efficiency, fixed size

# *list - dynamic, less memory efficiente, general purpose

# np.mean(): Computes the arithmetic mean (average) of the elements 
# np.average() Computes the weighted average of the elements

# media aritmetica (mesmo peso ou sem peso) e media ponderada (pesos diferentes)

