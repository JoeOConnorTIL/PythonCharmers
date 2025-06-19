# We will begin by introducing the Series, DataFrame, and Index classes, 
# which are the basic building blocks of the pandas library, and showing how to work with them. 
# By the end of this section, you will be able to create DataFrames and perform operations on them to
# inspect and filter the data.

# Anatomy of a DataFrame
# A DataFrame is composed of one or more Series. The names of the Series form the column names,
# and the row labels form the Index.

import pandas as pd # type: ignore

meteorites = pd.read_csv('C:\\Users\\JOE\\Documents\\Data for Python\\Meteorite_Landings.csv', nrows=5)
meteorites

print(meteorites.name)

print(meteorites.columns)

print(meteorites.index)

# Creating DataFrames
# We can create DataFrames from a variety of sources such as other Python objects, flat files, webscraping, 
# and API requests. Here, we will see just a couple of examples, but be sure to check out this page in the 
# documentation for a complete list. (https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)

# Using a flat file

import pandas as pd # type: ignore
meteorites = pd.read_csv('C:\\Users\\JOE\\Documents\\Data for Python\\Meteorite_Landings.csv')

# Further parameters for the read_csv function can be found (https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

# Using Data from an API
# Collect the data from NASA's Open Data Portal using the Socrata Open Data API (SODA) with the requests library:

import requests # type: ignore

try:
    response = requests.get(
        'https://data.nasa.gov/docs/legacy/meteorite_landings/gh4g-9sfh.json',
        params={'$limit': 50},
        timeout=10
    )
    response.raise_for_status()
    payload = response.json()
    print("Data downloaded successfully!")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#Create the DataFrame with the resulting payload:

df = pd.DataFrame(payload)
print(df.head(3))

# Tip: df.to_csv('data.csv') writes this data to a new file called data.csv.

# Inspecting the data
# Now that we have some data, we need to perform an initial inspection of it. This gives us information on what the data looks like, how many rows/columns there are, and how much data we have.

# Let's inspect the meteorites data.

# How many rows and columns are there?
print(meteorites.shape)

# What are the column names?
print(meteorites.columns)

# What types of data does each column currently hold?
print(meteorites.dtypes)

# What does the data look like?
print(meteorites.head())

# Sometimes there may be extraneous data at the end of the file, to check the bottom few rows:
print(meteorites.tail())

# Get some information about the dataframe
print(meteorites.info())

# Extracting Subsets
# A crucial part of working with DataFrames is extracting subsets of the data: finding rows that meet a certain set of criteria, isolating columns/rows of interest, etc. After narrowing down our data, we are closer to discovering insights. This section will be the backbone of many analysis tasks.

# Selecting columns
# We can select columns as attributes if their names would be valid Python variables:

print(meteorites.name)

# If their names would not be valid Python variables then we have to select them as keys. We can select multiple 
# columns at once this way.

print(meteorites[['name','mass (g)']])

# Selecting rows

print(meteorites[100:104])

# Indexing - using iloc[] to select rows and columns by their position (think of as index location of the column):

print(meteorites.iloc[100:104, [0,3,4,6]]) #This should return rows 100-104 and columns 0,3,4,6

# Alternatively use loc[] to select by name:

print(meteorites.loc[100:104, 'mass (g)':'year']) # This is selecting all the columns from mass to year.

# Filtering with Boolean masks
# A Boolean mask is a array-like structure of Boolean values – it's a way to specify which rows/columns we want to select (True) and which we don't (False).

# Here's an example of a Boolean mask for meteorites weighing more than 50 grams that were found on Earth (i.e., they were not observed falling):

print((meteorites['mass (g)'] > 50) & (meteorites.fall == 'Found'))

# Important: Take note of the syntax here. We surround each condition with parentheses, and we use bitwise
#  operators (&, |, ~) instead of logical operators (and, or, not).

# We can use a Boolean mask to select the subset of meteorites weighing more than 1 million grams (1,000 kilograms
# or roughly 2,205 pounds) that were observed falling:

print(meteorites[(meteorites['mass (g)']>1e6) & (meteorites.fall == 'Fell')])

# Tip: Boolean masks can be used with loc[] and iloc[].

# An alternative to this is the query() method:

meteorites.query("`mass(g)` > 1e6 and fall == 'Fell'")