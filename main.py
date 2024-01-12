# This Python file integrates all the developments in one application
from import_csv import import_csv_to_df

# Importing the data
data = import_csv_to_df("data.csv")

# Printing the data
data.head()

# Shaping
row, col = data.shape()
print(f'Data have {row} rows and {col} columns')
