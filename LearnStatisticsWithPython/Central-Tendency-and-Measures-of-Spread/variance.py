"""
Variance

- It is a descriptive statistic that describes how spread out(espalhados/distribuidos) the points in a data set are.
- Variance measures the degree of spread or dispersion of a set of values.
- It's crucial to understand the data distribution and its representativity of the median.

- Variance measures how far each value in the dataset is from the mean
- It's used to calculate the standard deviation, which is the square root of variance


-  A higher variance indicates that the data points are more dispersed, while a lower variance suggests that the values are clustered closer to the mean. 

    high variance (larger spread) - data more spread out
    lower variance (smaller spread) - data close together

***Variance is squared primarily to ensure that all deviations from the mean are treated as positive values, preventing them from canceling each other out when summed.

***The squared values have desirable mathematical properties that are crucial for statistical analysis. They allow for the use of calculus (derivatives and integrals) in optimization problems, which is essential for many statistical techniques like regression analysis.

The variance (σ²) is calculated as the sum of the squared differences between each data point and 
the population mean (μ), divided by the total number of data points (N): 
    σ² = Σ (xᵢ - μ)² / N. 

    ***After all, by comparing histograms, it was fairly easy to tell which dataset had a larger spread.

     - the formula for variance includes squaring the difference between the data and the mean, the variance is measured in units squared.


    A histogram with a wider, flatter shape typically indicates a higher variance, meaning data points are more spread out from the mean. Conversely (in the other way), a taller, narrower histogram suggests a lower variance, with data points clustered closer to the mean.


    
"""




import numpy as np

dataset = [3, 5, -2, 49, 10]
variance = np.var(dataset)

print(variance)