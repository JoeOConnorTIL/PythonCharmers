# Data Cleaning

# Using the taxis dataset: 

import pandas as pd

taxis = pd.read_csv('C:\\Users\\JOE\\Documents\\Data For Python\\2019_Yellow_Taxi_Trip_Data.csv')
print(taxis.head())

# dropping columns

columns_to_drop = ['vendorid','ratecodeid','pulocationid','dolocationid','store_and_fwd_flag']
taxis = taxis.drop(columns = columns_to_drop)  # Have to reassign to the variable to change taxis variable
print(taxis.head())

# renaming columns 

print(taxis.columns) # How it looked originally

taxis = taxis.rename(
    columns={
        'tpep_pickup_datetime': 'pickup',
        'tpep_dropoff_datetime': 'dropoff'
    }
)

print(taxis.columns) # With columns replaced

# Type Conversions

print(taxis.dtypes) # Shows original data types

# To change pickup and dropoff to datetimes:

taxis[['pickup','dropoff']] = taxis[['pickup','dropoff']].apply(pd.to_datetime)
print(taxis.dtypes)

# Other examples would be pd.to_numeric() or you can use astype() -shown later

# Creating new columns (there are multiple ways in pandas e.g standard formula and lambda functions)

taxis['new_column1'] = 'This is a new column'
taxis = taxis.assign(new_column2 = lambda x: 'This is a new column too')
print(taxis.head(2))

# We can create new columns based on existing columns too
# Note how 'x' in the lambda function refers to 'taxis' dataframe.

# Trip Time

taxis['trip_time1'] = taxis['dropoff'] - taxis['pickup']
taxis = taxis.assign(trip_time2 = lambda x: x.dropoff-x.pickup)
print(taxis.head(2))

# To remove these columns before we proceed:

more_columns_to_drop = ['new_column1','new_column2','trip_time1','trip_time2']
taxis = taxis.drop(columns=more_columns_to_drop)
print(taxis.head(2))

# Calculating for each row:
# 1. Elapsed time of the trip
# 2. The tip percentage
# 3. The total taxes, tolls, fees and surcharges
# 4. The average speed of the taxi

taxis = taxis.assign(
    elapsed_time = lambda x: x.dropoff - x.pickup, #1
    cost_before_tip = lambda x: x.total_amount - x.tip_amount,
    tip_pct = lambda x: x.tip_amount / x.cost_before_tip, #2
    fees = lambda x: x.cost_before_tip - x.fare_amount, #3
    avg_speed = lambda x: x.trip_distance.div(x.elapsed_time.dt.total_seconds() / 60 / 60) #4
)

print(taxis.head(2))

# Some things to note:

# We used lambda functions to 1) avoid typing taxis repeatedly and 
# 2) be able to access the cost_before_tip and elapsed_time columns
# in the same method that we create them.
# To create a single new column, we can also use df['new_col'] = 
# <values>.

# Sorting by values

# We can use the sort_values() method to sort based on any number of columns.

print(taxis.sort_values(['passenger_count', 'pickup'], ascending = [False, True]).head())

# To pick out the largest/ smallest rows, use nlargest() / nsmallest() instead.

print(taxis.nlargest(3, 'elapsed_time'))


# Working with the index

# So far, we haven't really worked with the index because 
# it's just been a row number; however, we can change the 
# values we have in the index to access additional features
# of the pandas library.

# Setting and sorting the index

# Currently we have a Rangeindex, but we can switch to a 
# DatetimeIndex by specifying a datetime column when calling 
# set_index():

taxis = taxis.set_index('pickup')
print(taxis.head(3))

# Since we have a sample of the full dataset, let's sort the index to order by pickup time:

taxis = taxis.sort_index()

# Tip: taxis.sort_index(axis=1) will sort the columns by name. The axis parameter is present
# throughout the pandas library: axis=0 targets rows and axis=1 targets columns.

# We can now select ranges from our data based on the datetime the same way we did with
# row numbers:

print(taxis['2019-10-23 07:45':'2019-10-23 08'])

# When not specifying a range, we can use the indext to select a single row:

print(taxis.loc['2019-10-23 08']) # Any time starting with '08' on this date.

# We will be working with time series later this section, but sometimes we want to reset 
# our index to row numbers and restore the columns. We can make pickup a column again with 
# the reset_index() method:

taxis = taxis.reset_index()
print(taxis.head())


