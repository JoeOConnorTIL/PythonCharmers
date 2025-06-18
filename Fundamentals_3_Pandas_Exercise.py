# Exercise 1
# Create a DataFrame by reading in the 2019_Yellow_Taxi_Trip_Data.csv file. Examine the first 5 rows.

# import package_name
import pandas as pd

# read file to variable
file = pd.read_csv('C:\\Users\\JOE\\Documents\\Data For Python\\2019_Yellow_Taxi_Trip_Data.csv')

# print the first 5 rows
print(file.head())

# Exercise 2
# Find the dimensions (number of rows and number of columns) in the data.

# Enter code here
print(file.shape)