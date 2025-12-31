import pandas as pd

# Load CSV file
df = pd.read_csv('sales_data.csv')

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset shape
print("\nShape of dataset:", df.shape)

# Column names and data types
print("\nDataset information:")
print(df.info())
