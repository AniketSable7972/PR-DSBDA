# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 4 :- Perform the following operations using Python on the Facebook metrics data set:
# a. Create data subsets
# b. Merge Data
# c. Sort Data
# d. Transposing Data
# e. Shape and reshape Data

import pandas as pd
import numpy as np

# Load Facebook Metrics Dataset
df = pd.read_csv(r'C:\Users\sable\OneDrive\Documents\Desktop\DSBDA_Practical\Dataset\Facebook Metrics of Cosmetic Brand.csv')
print("Original Dataset:\n", df.head())

# ------------------------------
# 1. DATA SUBSETS
# ------------------------------

# a) Subset by Selecting Specific Columns
subset_cols = df[['Type', 'Page total likes', 'Lifetime Post Total Reach']]
print("\nSubset - Specific Columns:\n", subset_cols.head())

# b) Subset by Filtering Rows
high_reach = df[df['Lifetime Post Total Reach'] > 50000]
print("\nSubset - Filter Rows (Reach > 50000):\n", high_reach.head())

# c) Subset by Rows and Columns
subset_rows_cols = df.loc[df['Type'] == 'Photo', ['Type', 'Post Month', 'Lifetime Post Total Reach']]
print("\nSubset - Rows and Columns (Photo Posts):\n", subset_rows_cols.head())

# d) Subset by Index
subset_by_index = df.iloc[10:20]
print("\nSubset - Index 10 to 20:\n", subset_by_index)

# e) Random Sampling for Subsetting
random_sample = df.sample(n=5)
print("\nRandom Sample (5 rows):\n", random_sample)

# f) Subset Based on Multiple Conditions
multiple_conditions = df[(df['Type'] == 'Video') & (df['Post Weekday'] == 3)]
print("\nSubset - Multiple Conditions (Video & Weekday==3):\n", multiple_conditions)

# ------------------------------
# 2. MERGE DATA
# ------------------------------

df1 = df[['Type', 'Post Month', 'Post Weekday']]
df2 = df[['Type', 'Page total likes', 'Lifetime Post Total Reach']]

# Inner Join
inner = pd.merge(df1, df2, on='Type', how='inner')
print("\nInner Join Result:\n", inner.head())

# Outer Join
outer = pd.merge(df1, df2, on='Type', how='outer')
print("\nOuter Join Result:\n", outer.head())

# Left Join
left = pd.merge(df1, df2, on='Type', how='left')
print("\nLeft Join Result:\n", left.head())

# Right Join
right = pd.merge(df1, df2, on='Type', how='right')
print("\nRight Join Result:\n", right.head())

# ------------------------------
# 3. SORT DATA
# ------------------------------

# a) Sort by Single Column
sorted_single = df.sort_values(by='Page total likes', ascending=False)
print("\nSorted by Page total likes (Descending):\n", sorted_single.head())

# b) Sort by Multiple Columns
sorted_multiple = df.sort_values(by=['Type', 'Post Month'], ascending=[True, False])
print("\nSorted by Type and Post Month:\n", sorted_multiple.head())

# ------------------------------
# 4. TRANSPOSING DATA
# ------------------------------

transposed = df.head().transpose()
print("\nTransposed Data (first 5 rows):\n", transposed)

# ------------------------------
# 5. SHAPE AND RESHAPE DATA
# ------------------------------

# a) Shape of Data
print("\nShape of the dataset (rows, columns):", df.shape)

# b) Reshape Example - Convert first 10 'like' values to numpy array and reshape
like_array = df['like'].head(10).to_numpy()
reshaped_like = like_array.reshape(2, 5)
print("\nReshaped 'like' values (2 rows x 5 cols):\n", reshaped_like)
