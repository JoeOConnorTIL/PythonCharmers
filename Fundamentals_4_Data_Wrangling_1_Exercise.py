# Exercise 1
# Read in the meteorite data from the Meteorite_Landings.csv 
# file, rename the mass (g) column to mass, and drop all the 
# latitude and longitude columns. Sort the result by mass in
# descending order.

# Enter your code here

import pandas as pd

meteorite = pd.read_csv('C:\\Users\\JOE\\Documents\\Data for Python\\Meteorite_Landings.csv')

print(meteorite.columns)

meteorite = meteorite.rename(
    columns= {
        'mass (g)':'mass'
    }
)

print(meteorite.columns)

columns_to_drop = ['reclat','reclong']

meteorite = meteorite.drop(columns=columns_to_drop)

print(meteorite.columns)

meteorite = meteorite.sort_values(['mass'], ascending= [False])

print(meteorite[['name','mass']])

# Exercise 2
# Using the meteorite data from the Meteorite_Landings.csv 
# file, update the year column to only contain the year,
# convert it to a numeric data type, and create a new 
# column indicating whether the meteorite was observed 
# falling before 1970. Set the index to the id column and 
# extract all the rows with IDs between 10,036 and 10,040 
# (inclusive) with loc[].

# Hint 1: Use year.str.slice() to grab a substring.

# Hint 2: Make sure to sort the index before using loc[]
# to select the range.

# Bonus: There's a data entry error in the year column. 
# Can you find it? (Don't spend too much time on this.)

# Enter your code here