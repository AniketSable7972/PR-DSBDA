# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 6A :- Visualize the data using Python libraries matplotlib, seaborn by plotting the graphs for heart.csv dataset.
# ====================================================================================================================================

# Import required Python libraries
import numpy as np                      # For numerical operations
import pandas as pd                     # For data handling using DataFrames
import matplotlib.pyplot as plt         # For creating plots and graphs
import seaborn as sns                   # For advanced, beautiful visualizations

# Load the heart disease dataset (make sure the path is correct on your system)
df = pd.read_csv(r'C:\Users\sable\OneDrive\Documents\Desktop\DSBDA_Practical\Dataset\heart.csv')

# Show the first few rows of the dataset to get an idea of the data
df.head()

# Check the column names in the dataset
print("Columns in dataset:\n", df.columns)

# 🌸 Bar Plot: Mean Cholesterol by Gender
sns.barplot(x='sex', y='chol', data=df)
plt.title("Average Cholesterol by Gender")
plt.xlabel("Sex (0 = Female, 1 = Male)")
plt.ylabel("Cholesterol Level")
plt.show()

# 🌸 Bar Plot: Standard Deviation of Cholesterol by Gender
sns.barplot(x='sex', y='chol', data=df, estimator=np.std)
plt.title("Cholesterol STD by Gender")
plt.show()

# 🌸 Count Plot: Number of Male and Female Patients
sns.countplot(x='sex', data=df)
plt.title("Count of Patients by Gender")
plt.show()

# 🌸 Box Plot: Cholesterol Distribution (Min, Q1, Median, Q3, Max) by Gender
sns.boxplot(x='sex', y='chol', data=df)
plt.title("Cholesterol Distribution by Gender")
plt.show()

# 🌸 Violin Plot: Cholesterol Distribution + Density Shape by Gender
sns.violinplot(x='sex', y='chol', data=df)
plt.title("Violin Plot of Cholesterol by Gender")
plt.show()

# 🌸 Violin Plot with Hue (Chest Pain Type) for extra insight
sns.violinplot(x='sex', y='chol', data=df, hue='cp', split=True)
plt.title("Cholesterol by Gender and Chest Pain Type")
plt.show()

# 🌸 Distribution Plot: Histogram + KDE of Maximum Heart Rate Achieved
sns.histplot(df['thalachh'], bins=10, kde=True)
plt.title("Distribution of Maximum Heart Rate (thalachh)")
plt.xlabel("thalachh")
plt.show()

# 🌸 Joint Plot: Scatter plot showing relationship between Max Heart Rate and Gender
sns.jointplot(x='thalachh', y='sex', data=df, kind='scatter')
plt.show()

# 🌸 Joint Plot: Hexbin plot showing density of points
sns.jointplot(x='thalachh', y='sex', data=df, kind='hex')
plt.show()

# 🌸 Rug Plot: Small vertical lines showing distribution of Heart Rate values
sns.rugplot(df['thalachh'])
plt.title("Rug Plot - thalachh")
plt.show()

# 🌸 Strip Plot: Individual data points of Heart Rate vs Gender (without jitter)
sns.stripplot(x='sex', y='thalachh', data=df, jitter=False)
plt.title("Strip Plot - Heart Rate vs Gender (No Jitter)")
plt.show()

# 🌸 Strip Plot: Same but with jitter (spread horizontally for visibility)
sns.stripplot(x='sex', y='thalachh', data=df, jitter=True)
plt.title("Strip Plot - Heart Rate vs Gender (With Jitter)")
plt.show()

# 🌸 Strip Plot with Hue (Chest Pain Type) for more dimensions
sns.stripplot(x='sex', y='thalachh', data=df, jitter=True, hue='cp')
plt.title("Strip Plot - Heart Rate vs Gender & Chest Pain")
plt.show()

# 🌸 Swarm Plot: Like strip plot but better organized to avoid overlap
sns.swarmplot(x='sex', y='thalachh', data=df)
plt.title("Swarm Plot - Heart Rate vs Gender")
plt.show()

# 🌸 Swarm Plot with Hue (Chest Pain Type)
sns.swarmplot(x='sex', y='thalachh', data=df, hue='cp')
plt.title("Swarm Plot - Heart Rate vs Gender & Chest Pain")
plt.show()

# 🌸 Heatmap: Show correlation between numerical features (1 = strong, 0 = none, -1 = inverse)
corr = df.corr()  # Calculate correlation matrix
plt.figure(figsize=(10, 7))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap - Heart Dataset')
plt.show()
