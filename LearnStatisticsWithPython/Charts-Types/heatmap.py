"""
Heat maps are effective for visualizing the relationship between two categorical variables. 
They use colors to represent the frequency or density of observations in a contingency table.
"""

import matplotlib.pyplot as plt
import numpy as np

categories = ["A", "B", "C", "D"]
values = np.array([[10, 20, 30, 40],
                   [15, 25, 35, 45],
                   [20, 30, 40, 50],
                   [25, 35, 45, 55]])


plt.imshow(values, cmap = "hot", interpolation="nearest")

plt.title("Heatmap")
plt.colorbar(label="Value")
plt.xticks(np.arange(len(categories)), categories)
plt.yticks(np.arange(len(categories)), categories)

plt.show()