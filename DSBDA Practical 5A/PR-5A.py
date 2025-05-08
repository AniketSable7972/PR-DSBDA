# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 5 :- Perform the following operations using Python on the Heart Diseases data set
# a. Data cleaning
# b. Data integration
# c. Data transformation
# d. Error correcting
# e. Data model building

# ========================================================================================================

# Importing necessary libraries for data processing and modeling
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.preprocessing import StandardScaler  # For scaling the data to standardize it
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # For model evaluation
from sklearn.linear_model import LogisticRegression  # Logistic Regression model for classification
from sklearn.tree import DecisionTreeClassifier  # Decision Tree Classifier for classification

# Loading the Heart Disease dataset
df = pd.read_csv(r"C:\Users\sable\OneDrive\Documents\Desktop\DSBDA_Practical\Dataset\heart.csv")

# Displaying the first few rows of the data
df.head()

# a) Data Cleaning
# Removing duplicate entries in the dataset
df = df.drop_duplicates()

# Descriptive statistics (e.g., mean, min, max) of each column to understand the data distribution
df.describe()

# Information about each column's data type and non-null count
df.info()

# Checking for any missing values in the dataset
df.isna().sum()

# b) Data Integration
# Exploring unique values in the 'fbs' column (Fasting Blood Sugar)
df.fbs.unique()

# Selecting relevant columns for integration (subset of features)
df1 = df[['age','cp','chol','thalachh']]  # Features related to age, chest pain type, cholesterol, and maximum heart rate
df2 = df[['exng','slp','output']]  # Features related to exercise induced angina, slope of peak exercise ST segment, and target variable output

# Merging the two datasets (df1 and df2) on columns along the horizontal axis
merging = pd.concat([df1, df2], axis=1)

# Displaying the merged dataset
merging

# d) Error Correcting
# Checking column names for clarity
df.columns

# Function to remove outliers using the IQR (Interquartile Range) method
def remove_outliers(column):
    Q1 = column.quantile(0.25)  # First quartile (25th percentile)
    Q3 = column.quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1  # Interquartile range
    threshold = 1.5 * IQR  # Defining threshold for outliers
    outlier_mask = (column < Q1 - threshold) | (column > Q3 + threshold)  # Identifying outliers
    return column[~outlier_mask]  # Returning column without outliers

# Applying outlier removal for specific columns
col_name = ['cp', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa']
for col in col_name:
    df[col] = remove_outliers(df[col])

# Dropping any rows with missing values after outlier removal
df = df.dropna()

# Dropping unnecessary column 'fbs' from the dataset
df = df.drop('fbs', axis=1)

# Splitting data into features (X) and target variable (y)
x = df[['cp', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa']]  # Features
y = df.output  # Target variable (heart disease output)

# Splitting data into training and test sets (80% for training, 20% for testing)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Displaying the shapes of the train and test sets
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# c) Data Transformation
# Standardizing the features (scaling them) so that they all have the same scale
scaler = StandardScaler()

# Fitting the scaler on the training data and transforming both train and test data
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# e) Data Model Building
# Logistic Regression Model
model = LogisticRegression()

# Training the Logistic Regression model on the scaled training data
model.fit(x_train_scaled, y_train)

# Making predictions on the test set using the trained model
y_pred = model.predict(x_test_scaled)

# Evaluating the Logistic Regression model using accuracy and a classification report
accuracy = accuracy_score(y_test, y_pred)
print("Logistic Regression Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Decision Tree Classifier Model
# Creating a Decision Tree model with the 'entropy' criterion (used for information gain)
dtc = DecisionTreeClassifier(criterion='entropy')

# Training the Decision Tree model on the scaled training data
dtc.fit(x_train_scaled, y_train)

# Making predictions on the test set using the Decision Tree model
y_pred_dtc = dtc.predict(x_test_scaled)

# Evaluating the Decision Tree model using accuracy, confusion matrix, and a classification report
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_dtc))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dtc))
print("Classification Report:\n", classification_report(y_test, y_pred_dtc))
