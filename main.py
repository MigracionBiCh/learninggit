# This Python file integrates all the developments in one application
from import_csv import import_csv_to_df

# Importing the data
data = import_csv_to_df("data.csv")

# Printing the data
data.head()