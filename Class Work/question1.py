import pandas as pd

# Original data series
data = pd.Series([100, 200, 'python', 300.12, 400])

# Convert the series to numeric, forcing invalid parsing to NaN
numeric_data = pd.to_numeric(data, errors='coerce')

# Print the result
print("Original Data Series:")
print(data)
print("\nChange the said data type to numeric:")
print(numeric_data) 
