import numpy as np
import pandas as pd

# Load data
golf = pd.read_csv('Golf Stats.csv') # importing the csv file
print(golf.describe())

#Renaming Columns
golf.columns = [s.strip().replace(' ', '_') for s in golf.columns] # all columns

df_filled_mean = golf.fillna(golf.mean(numeric_only=True))

print(df_filled_mean)

df = pd.DataFrame(df_filled_mean)

# # #Finding Correlation
correlation_matrix = df.corr()
print(correlation_matrix)

# correlation_matrix.to_csv('golf_correlation_matrix.csv')

# Visualize the finding
import seaborn as sn
import matplotlib.pyplot as plt

sn.heatmap(correlation_matrix, annot=True)
plt.show()