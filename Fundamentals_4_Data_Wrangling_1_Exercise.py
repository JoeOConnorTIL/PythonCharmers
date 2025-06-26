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

print(meteorite['year'].head())

meteorite['year'] = meteorite.year.str.slice(6, 10)
meteorite['year'] = meteorite['year'].apply(pd.to_numeric)

print(meteorite['year'].head())

meteorite['before_1970'] = meteorite['year'] < 1970
print(meteorite[['year', 'before_1970']].head())

meteorite['id'] = meteorite['id'].apply(pd.to_numeric)
meteorite = meteorite.set_index('id').sort_index() # Need to sort the index after setting it to be able to call a range
print(meteorite.loc[10036:10040])

# In the Python command:

# meteorite = meteorite.set_index('id').sort_index()
# the order of operations follows left-to-right chaining due to method chaining on a Pandas DataFrame. Here's what 
# happens step-by-step:

# meteorite.set_index('id')

# This creates a new DataFrame where the 'id' column is set as the index.

# The result is a DataFrame with 'id' as its index, and the original 'id' column is removed from the columns.

# .sort_index()

# This sorts the new DataFrame by its index — which is now 'id'.

# It returns another DataFrame, now sorted by 'id'.

# meteorite = ...

# The resulting sorted DataFrame is then reassigned back to the meteorite variable.

# Summary of Order:
# set_index('id')

# sort_index()

# Assignment to meteorite

# Each method returns a new DataFrame, not modifying the original meteorite in-place unless explicitly specified 
# with inplace=True.