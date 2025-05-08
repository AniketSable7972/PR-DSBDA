# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 6B :- Visualize the data using Python libraries matplotlib, seaborn by plotting the graphs for air-quality dataset.
# =================================================================================================================================================

# 🌸 Import necessary libraries
import numpy as np                      # For numerical calculations (like mean, std)
import pandas as pd                     # For data handling (DataFrames, CSV reading)
import matplotlib.pyplot as plt         # For plotting graphs
import seaborn as sns                   # For advanced visualizations

# 🌸 Load the air quality dataset (make sure the file path is correct for your system)
df2 = pd.read_csv(r"C:\Users\sable\OneDrive\Documents\Desktop\DSBDA_Practical\Dataset\air quality.csv", encoding='cp1252')

# 🌸 Display the first few rows to get a glimpse of the data
df2.head()

# 🌸 Print all column names in the dataset
print("Columns:", df2.columns.tolist())

# 🌸 Bar Plot: Mean SO2 levels (Sulfur Dioxide) by State
plt.figure(figsize=(12,6))  # Make plot wider for better readability
sns.barplot(x='state', y='so2', data=df2)
plt.title("Average SO2 Levels by State")
plt.xticks(rotation=90)  # Rotate x-axis labels to avoid overlap
plt.ylabel("SO2 Level")
plt.show()

# 🌸 Bar Plot: Standard Deviation (variability) of SO2 by State
plt.figure(figsize=(12,6))
sns.barplot(x='state', y='so2', data=df2, estimator=np.std)  # Using std instead of mean
plt.title("SO2 Standard Deviation by State")
plt.xticks(rotation=90)
plt.ylabel("SO2 STD")
plt.show()

# 🌸 Box Plot: Distribution of SO2 values by State (shows median, quartiles, outliers)
plt.figure(figsize=(12,6))
sns.boxplot(x='state', y='so2', data=df2)
plt.title("SO2 Distribution by State")
plt.xticks(rotation=90)
plt.show()

# 🌸 Count Plot: Number of data records available per State
plt.figure(figsize=(12,6))
sns.countplot(x='state', data=df2)
plt.title("Record Count by State")
plt.xticks(rotation=90)
plt.show()

# 🌸 Violin Plot: SO2 distribution + density + spread by State
plt.figure(figsize=(12,6))
sns.violinplot(x='state', y='so2', data=df2)
plt.title("Violin Plot of SO2 by State")
plt.xticks(rotation=90)
plt.show()

# 🌸 Distribution Plot: Histogram + Kernel Density Estimate (KDE) for NO2 levels
plt.figure(figsize=(8,4))
sns.histplot(df2['no2'], bins=10, kde=True)
plt.title("Distribution of NO2 Levels")
plt.xlabel("NO2")
plt.show()

# 🌸 Histogram: SO2 levels (without KDE)
plt.figure(figsize=(8,4))
sns.histplot(df2['so2'], bins=10, kde=False)
plt.title("SO2 Distribution")
plt.xlabel("SO2")
plt.show()

# 🌸 Joint Plot: Relationship between SO2 and NO2 (scatter plot)
sns.jointplot(x='so2', y='no2', data=df2, kind='scatter')
plt.suptitle("Joint Plot: SO2 vs NO2", y=1.02)
plt.show()

# 🌸 Rug Plot: Small lines at the base to show distribution of SO2 values
plt.figure(figsize=(8,2))
sns.rugplot(df2['so2'])
plt.title("Rug Plot of SO2")
plt.xlabel("SO2")
plt.show()

# 🌸 Strip Plot: SO2 levels by State (without jitter, so points may overlap)
plt.figure(figsize=(12,6))
sns.stripplot(x='state', y='so2', data=df2, jitter=False)
plt.title("Strip Plot of SO2 by State (No Jitter)")
plt.xticks(rotation=90)
plt.show()
