"""
range=max(data) − min(data)

A histogram helps summarize data to inform decisions or explain distributions. It is useful for showing trends, while averages can sometimes be misleading about underlying trends.

Histograms are helpful for understanding how your data is distributed.

When plotting a histogram, it’s essential to select bins that fully capture the trends in the underlying data.

-In the context of a histogram, bins represent the intervals or ranges of values ​​and therefore determine the width of each bar.




-In NumPy, np.amin() is a function used to find the minimum value within an array or along a specified axis. 
It is an alias for np.min(), meaning both functions perform the same operation.

-In NumPy, np.amax and np.max are essentially the same function. np.max is an alias for np.amax. 
Both functions return the maximum value of an array or the maximum value along a specified axis of an array.

pyplot uses .histo() - This function not only calculates the histogram data but also plots it as a chart, is for data visuzalition

numpy uses .histogram() - it returns an array. It does not create a visual chart, is for computation and analysis
    The first array contains the counts (or frequencies) of values that fall into each bin.
    The second array contains the bin edges, which are the boundaries for each of the bins

"""

import numpy as np


exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42, 22, 34, 26,27])


min_age = np.amin(exercise_ages) 
max_age = np.amax(exercise_ages) 
age_range = max_age - min_age


print(f"min:{min_age}, max:{max_age}, range:{age_range}")

"""
FIND THE MIN AND MAX IS ESSENTIAL, THIS IS TO KNOW THE RANGE OF OUR HISTOGRAM
FREQUENTLY WE CANNOT VISUALIZE THE AMOUNT OF DATA, SO WE FIND THE RANGE. 

BIN = A bin is a sub-range of values that falls within the range of a dataset. Bins are like chunks of data. 
COUNT = A count is the number of values that fall within a bin’s range.  
"""

ages_hist = np.histogram(exercise_ages, range = (22, 62), bins = 2)
print(ages_hist)


