import pandas as pd

tsa = pd.read_csv('C:\\Users\\JOE\\Documents\\Data For Python\\tsa_passenger_throughput.csv')

print(tsa.head())

# First, we will lowercase the column names and take the first word (e.g., 2021 for 2021
# Traveler Throughput) to make this easier to work with:

tsa = tsa.rename(columns = lambda x: x.lower().split()[0])

print(tsa.head())

# Melting

# Melting helps convert our data into long format, to get all of the traveller throughput 
# numbers in one column:

tsa_melted = pd.melt(tsa, # Our dataframe
                     id_vars = ['date'], # Column or list of columns that uniquely identifies a row (can be multiple)
                     var_name = 'year', # Name for the variable column created by melting.
                     value_name = 'travelers' # name for new column containing values from melted columns.
                     )
print(tsa_melted.sample(5, random_state = 1)) # Show some random entries

# To convert this into a time series of traveler throughput, we need to replace the year in the date column with 
# the one in the year column. Otherwise, we are marking prior years' numbers with the wrong year.

# 'dt' is the datetime section of the pandas library
# 'strftime' stands for "string format time". It converts datetime objects into a string 
# '-%m-%d' access the month and day from the existing date field

tsa_melted['date'] = tsa_melted['date'].apply(pd.to_datetime) # Changing the date column to datetime to make the below work:

tsa_melted = tsa_melted.assign(
    date = lambda x: pd.to_datetime(x.year + x.date.dt.strftime('-%m-%d'))
)

# Alternatively: 

tsa_melted['date'] = pd.to_datetime(tsa_melted['year'] + tsa_melted['date'].dt.strftime('-%m-%d'))

print(tsa_melted.sample(5, random_state=1))

# This leaves us with some null values - dates that aren't present in the dataset

print(tsa_melted.sort_values('date').tail(3))

# These can be dropped with the dropna() method:

tsa_melted = tsa_melted.dropna()
print(tsa_melted.sort_values('date').tail(3))

# Pivoting

# Using the melted data, we can pivot the data to compare TSA traveler throughput on specific days across years. 
# Let's look at the first 10 days in March:

# already converted date column to date format.

# 'copy()' here is ensuring that 'first_10_days' becomes a standalone DataFrame
first_10_days = tsa_melted.loc[(tsa_melted['date'].dt.month == 3) & (tsa_melted['date'].dt.day <= 10)].copy()
first_10_days['day_in_march'] = first_10_days['date'].dt.day

# pivot dataset
first_10_days_pivot = pd.pivot(first_10_days,index='year', columns='day_in_march', values='travelers')
print(first_10_days_pivot)

# Alternatively these steps can be combined as below
tsa_pivoted = tsa_melted\
    .query('date.dt.month == 3 and date.dt.day <= 10')\
    .assign(day_in_march=lambda x: x.date.dt.day)\
    .pivot(index='year', columns='day_in_march', values='travelers')
# Backslashes mean that you're doing a continuation of a line.

print(tsa_pivoted)

# note we currently have two headers, to return to one use '.reset_index()
# the 'day_in_march' column can now be dropped

tsa_pivoted = tsa_pivoted.reset_index()
print(tsa_pivoted)

# We have not covered unstack() and stack() methods, which are additional ways to pivot and melt, 
# respectively. These come in handy when we have a multi-level index (e.g. if we ran set_index()
# with more than one column) More information here: 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html

# Transposing

# The T attribute provides a quick way to flip rows and columns.

print(tsa_pivoted.T)

# Merging (Joining)

# Introducing second dataset, setting data type for date, setting date as index and ordering.

holidays = pd.read_csv('C:\\Users\\JOE\\Documents\\Data For Python\\holidays.csv')
holidays['date'] = holidays['date'].apply(pd.to_datetime)
holidays = holidays.set_index('date').sort_index()
print(holidays.head())

# Merging the holidays with the TSA traveler throughput data:

# 'merge()' will join two dataframes, in the form df1.merge(df2, ......)
# 'left_on' & 'right_on' are the columns or list of columns you are joining on, 
#   - in this case we use an index so there is a special parameter for that
# 'how' defines the type of join, e.g. 'left','inner',etc.
tsa_melted_holidays = tsa_melted.merge(
    holidays, 
    left_on='date', 
    right_index=True, 
    how='left')
    
tsa_melted_holidays = tsa_melted_holidays.sort_values('date')
print(tsa_melted_holidays.head())
