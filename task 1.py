# ======================================
# TASK 1 - DATA CLEANING
# ======================================

import pandas as pd
import seaborn as sns

# Load Titanic dataset directly
df = sns.load_dataset('titanic')
print("\nFIRST 5 ROWS:\n")
print(df.head())

# Missing values
print("\nMISSING VALUES:\n")
print(df.isnull().sum())

# Fill missing age
df['age'] = df['age'].fillna(df['age'].mean())

# Fill embarked
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df = df.rename(columns={
    'survived': 'Survived_Status',
    'pclass': 'Passenger_Class'
})

# Convert datatype
df['Passenger_Class'] = df['Passenger_Class'].astype('category')
print("\nFINAL DATASET:\n")
print(df.head())

# Save cleaned dataset
df.to_csv('cleaned_titanic.csv', index=False)

print("\nTASK 1 COMPLETED SUCCESSFULLY!")