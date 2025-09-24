"""
Standard Deviation

 - Standard deviation is computed by taking the square root of the variance. 
 - It's more useful to interpret data than the variance
-Measures Dispersion: It quantifies the spread or variability of data. 

 Low Standard Deviation: Indicates data points are close to the mean, suggesting less variability. 
 High Standard Deviation: Indicates data points are further from the mean, suggesting more variability. 

 In Python, you can take the square root of a number using ** 0.5:

 There is a NumPy function dedicated to finding the standard deviation of a dataset — we can cut out the step of first finding the variance.

 The NumPy function std() takes a dataset as a parameter and returns the standard deviation of that dataset.
 
"""

import numpy as np

dataset = [4, 8, 15, 16, 23, 42]
standard_deviation = np.std(dataset)


