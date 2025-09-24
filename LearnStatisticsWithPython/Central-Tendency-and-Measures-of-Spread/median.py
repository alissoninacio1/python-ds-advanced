"""
    Median

    - a common measure of a dataset’s center.
    - The value that, assuming the dataset is ordered from smallest to largest, falls in the middle (odd)
    - If there are an even number of values in a dataset, you either report both of the middle two values or their average.

    Manually finding the median of a dataset
    Using Python’s NumPy library to find the median of a dataset
    Interpreting what it means for a dataset to have similar and different median and mean values

    

"""


import numpy as np

mean_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36])

mean_result = np.mean(mean_array)

print(mean_result)



# considerations
# np.mean() function calculates the average of the values in an array, 
# regardless of whether the array is ordered or unordered.
# you can sort the dataset using .sort()