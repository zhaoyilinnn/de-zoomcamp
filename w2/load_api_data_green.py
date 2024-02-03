import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url_green_taxi1 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url_green_taxi2 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url_green_taxi3 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    
    
    
    taxi_dtypes = {
        'VendorID': 'Int64',
        'store_and_fwd_flag': 'str',
        'RatecodeID': 'Int64',
        'PULocationID': 'Int64',
        'DOLocationID': 'Int64',
        'passenger_count': 'Int64',
        'trip_distance': 'float64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'ehail_fee': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'payment_type': 'float64',
        'trip_type': 'float64',
        'congestion_surcharge': 'float64'
    }

    parse_dates_green_taxi = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    # ,  
    data1 = pd.read_csv(url_green_taxi1, sep=',', dtype=taxi_dtypes, parse_dates=parse_dates_green_taxi )
    data2 = pd.read_csv(url_green_taxi2, sep=',', dtype=taxi_dtypes, parse_dates=parse_dates_green_taxi )
    data3 = pd.read_csv(url_green_taxi3, sep=',', dtype=taxi_dtypes, parse_dates=parse_dates_green_taxi )

    data = pd.concat([data1, data2, data3])
    # data['lpep_pickup_datetime'] = data['lpep_pickup_datetime'] .dt.strftime('%Y-%m')
    # data['lpep_dropoff_datetime'] = data['lpep_dropoff_datetime'] .dt.strftime('%Y-%m')
    # data = data[data['lpep_pickup_datetime'].str.contains('2020-10')]
    # print(data['lpep_pickup_datetime'].unique())
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
