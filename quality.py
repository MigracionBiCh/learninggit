def count_null(df):
    nulls = df.isnull().sum()
    return nulls

def duplicates(df):
  duplicates = df.duplicates().sum()
  return duplicates
