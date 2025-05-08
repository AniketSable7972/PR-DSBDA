# Name :- Aniket Sable
# Roll No. :- 54
# Class :- TE(IT)
# Practical 5 :- Perform the following operations using Python on the Air Quality data set
# a. Data cleaning
# b. Data integration
# c. Data transformation
# d. Error correcting
# e. Data model building

# ========================================================================================================

# Importing Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Loading the Air Quality dataset
df = pd.read_csv(r"C:\Users\sable\OneDrive\Documents\Desktop\DSBDA_Practical\Dataset\air quality.csv", encoding="latin1")

# Displaying the first few rows of the data
df.head()

# ========================================================================================================
# 1. DATA CLEANING
# ========================================================================================================

# Show basic info
df.info()

# Show missing values
print("Missing values:\n", df.isnull().sum())

# Drop rows with too many missing values or impute
df = df.dropna(thresh=len(df.columns)-2) # drop rows with more than 2 missing values
df.fillna(df.mean(numeric_only=True), inplace=True) # fill numeric NaNs with column mean

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# check again
df.info()

# ========================================================================================================
# (b) Data Integration
# ========================================================================================================

# Creating data subsets
df1 = df[['state','location','agency','type']]
df2 = df[['so2','no2','rspm','spm']]
merging=pd.concat([df1,df2],axis=1)
merging

# ========================================================================================================
# (c) Data Transformation
# ========================================================================================================

# Create new feature (e.g., Air Quality Index Category)
def aqi_category(pm2_5):
    if pm2_5 <= 0.12:
        return 'Good'
    elif pm2_5 <= 0.35:
        return 'Moderate'
    else:
        return 'Unhealthy'

df['AQI_Category'] = df['pm2_5'].apply(aqi_category)
df.head()

# ========================================================================================================
# (d) Error Correcting
# ========================================================================================================

# Find anomalies (e.g., negative values in PM2.5)
print("Negative pm2_5 values:\n", df[df['pm2_5'] < 0])

# Replace negative values with NaN and then fill
df['pm2_5'] = df['pm2_5'].apply(lambda x: np.nan if x < 0 else x)
df['pm2_5'].fillna(df['pm2_5'].mean(), inplace=True)

# ========================================================================================================
# (e) Data Model Building
# ========================================================================================================

# Clean and prepare the data
model_df = df[['so2', 'no2']].dropna() # drop rows with missing so2 or no2

# Define X and y
X = model_df[['so2']] # independent variable
y = model_df['no2'] # dependent variable

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted NO2 values
plt.scatter(X_test, y_test, color='purple', label='Actual NO2')
plt.plot(X_test, y_pred, color='black', label='Predicted NO2')
plt.xlabel('SO2')
plt.ylabel('NO2')
plt.title('Linear Regression: SO2 vs NO2')
plt.legend()
plt.grid(True)
