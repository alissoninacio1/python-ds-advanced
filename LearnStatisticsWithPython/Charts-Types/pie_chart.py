"""

Pie charts PARTS OF A WHOLE and are useful for showing the PROPORTION of each category in a data set. 
However, their use is recommended with CAUTION, as they can be difficult to interpret correctly, 
especially when there are many categories or when the differences between the parts are small.

"""

import matplotlib.pyplot as plt 

categories = ['A', 'B', 'C', 'D']
percent = [25, 30, 20, 25]

plt.pie(percent, labels=categories, autopct='%1.1f%%')

plt.title('Categories Distribution')

plt.show()