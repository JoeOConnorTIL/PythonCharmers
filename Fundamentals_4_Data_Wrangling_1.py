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




