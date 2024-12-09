
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('hypothesis_testing_dataset.csv')

# Example T-test: Comparing Satisfaction Score based on Gender
group_male = df[df['Gender'] == 'Male']['Satisfaction_Score']
group_female = df[df['Gender'] == 'Female']['Satisfaction_Score']
t_stat, p_value = stats.ttest_ind(group_male, group_female)
print(f'T-Test Results: t-statistic = {t_stat}, p-value = {p_value}')

# Example F-test: Comparing variances of Income between Educational level groups
High_School_group = df[df['Education_Level'] == 'High School']['Income']
Bachelor_group = df[df['Education_Level'] == 'Bachelor']['Income']
Master_group = df[df['Education_Level'] == 'Master']['Income']
PhD_group = df[df['Education_Level'] == 'PhD']['Income']
f_stat, f_p_value = stats.levene(High_School_group , Bachelor_group, Master_group, PhD_group)
print(f'F-Test Results: F-statistic = {f_stat}, p-value = {f_p_value}')

# # Example Chi-Squared Test: Testing relationship between Customer_Type and Product_Category
contingency_table = pd.crosstab(df['Customer_Type'], df['Product_Category'])
chi2_stat, chi2_p_val, dof, expected = stats.chi2_contingency(contingency_table)
print(f'Chi-Squared Test Results: chi2_stat = {chi2_stat}, p-value = {chi2_p_val}')

# # Visualization: Boxplot for Income based on Gender
# sns.boxplot(x='Gender', y='Income', data=df)
# plt.title('Income Distribution by Gender')
# plt.show()