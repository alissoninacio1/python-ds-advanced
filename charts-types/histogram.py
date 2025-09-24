"""
A histogram is a visual representation of the distribution of quantitative (numerical) data, 
where the range of data is divided into "bins" or "intervals," and the height of each rectangular bar shows the frequency (count) 
of data points that fall into that specific bin. They identify the shape and symmetry of the distribution.
Histograms are used to understand the shape, center, and spread of a dataset. 

"""

import matplotlib.pyplot as plt #the same as: from matplotlib import pyplot as plt

data = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]


plt.hist(data, bins=5)


plt.title('Age Histograms')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')


plt.show()