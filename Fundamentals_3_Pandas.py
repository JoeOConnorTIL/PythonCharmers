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
