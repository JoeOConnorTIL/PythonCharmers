# Exercise 1
# Create a DataFrame by reading in the 2019_Yellow_Taxi_Trip_Data.csv file. Examine the first 5 rows.

# import package_name
import pandas as pd # type: ignore

# read file to variable
file = pd.read_csv('C:\\Users\\JOE\\Documents\\Data For Python\\2019_Yellow_Taxi_Trip_Data.csv')

# print the first 5 rows
print(file.head())

# Exercise 2
# Find the dimensions (number of rows and number of columns) in the data.

# Enter code here
print(file.shape)

# Using the data in the 2019_Yellow_Taxi_Trip_Data.csv file, calculate summary statistics for the fare_amount, tip_amount, tolls_amount, and total_amount columns.
print(file[['fare_amount','tip_amount','tolls_amount','total_amount']].describe())
# Exercise 4
# Isolate the fare_amount, tip_amount, tolls_amount, and total_amount for the longest trip by distance (trip_distance).

# Enter code here
print(file.columns) # returns the name of the columns
print(file['trip_distance'].max()) # identifies the max trip distance
print(file['trip_distance'].idxmax()) # identifies the index of the max value
print(file.loc[file['trip_distance'].idxmax()]) # uses the max value index to locate other info
print(file.loc[file['trip_distance'].idxmax()][['fare_amount','tip_amount','tolls_amount','total_amount']]) # isolates four columns