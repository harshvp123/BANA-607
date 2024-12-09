import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('baseball.csv')  # importing the csv file

data = data.dropna()


# Calculate Q1 (25th percentile) and Q3 (75th percentile) for the Salary column
Q1 = data['Salary'].quantile(0.25)
Q3 = data['Salary'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for identifying outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove rows with outliers in the Salary column
df = data[(data['Salary'] >= lower_bound) & (data['Salary'] <= upper_bound)]

#Finding Correlation
correlation_matrix = df.corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True)
plt.show()

