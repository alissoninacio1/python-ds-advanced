# You can calculate the range using the following: 
#     range = max - min


import pandas as pd

# Creating a sample dataset
data = {
    'Product': ['Keyboard', 'Mouse', 'Monitor', 'Headphones', 'Laptop'],
    'Stock': [150, 300, 50, 200, 10]
}
df = pd.DataFrame(data)


lowest_stock = df['Stock'].min()
print(lowest_stock)
# Output: 10

highest_stock = df['Stock'].max()
print(highest_stock)
# Output: 300

