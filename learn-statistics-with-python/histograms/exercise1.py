import numpy as np


new_array = np.array([1, 2, 2, 6, 9, 10, 11, 3, 6])

show_bins = np.histogram(new_array, range = (0, 12), bins = 3)

print(show_bins)
#shows the number of values in each bin