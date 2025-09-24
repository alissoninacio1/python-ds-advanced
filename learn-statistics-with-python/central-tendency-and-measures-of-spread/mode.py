"""
Mode
 - The most frequently occurring observation in the dataset.
 - A dataset can have multiple modes if there is more than one value with the same maximum frequency.

 - The SciPy stats.mode() function can do the work of finding the mode for you. 
 -  In the example below, we import stats then use stats.mode() to calculate the mode
"""

import numpy as np
from scipy import stats

example_array = np.array([24, 16, 12, 10, 12, 28, 38, 12, 28, 24])
example_mode = stats.mode(example_array)

print(example_mode)