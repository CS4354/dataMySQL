
import os
import sys

from collections import OrderedDict
from datetime import datetime
from pprint import pprint

import geocoder

def get_latlng(address):
    """
    Given an address, return the latitude and longitude

    Make sure MAPQUEST_API_KEY is set
    """
    print("querying mapquest for", address)

    try:
        result = geocoder.mapquest(
            address, key=os.environ.get("MAPQUEST_API_KEY")
        ).json
    except Exception as e:
        print(e)
        # Exit if a match can't be found
        sys.exit(1)
    
    result = (result["lat"], result["lng"])
    print("found", result)
    return result

def c(cell):
    """
    clean annoying cell values
    """
    if " " in cell or cell == "":
        cell = -1 # Unknown or corrupt value
    return int(float(cell))

def create_states_table_rows(data):
    print("create_states_table_rows called")
    
    table_rows = []
    pk = []
    for item in data:
        # Extract primary key from row
        state_id = item[1]

        # Only use row if primary key has not already been seen
        if state_id not in pk:
            pk.append(state_id)
            table_rows.append((state_id, item[5]))
    
    return table_rows

def create_pollution_table_rows(data):
    """
    There are 500k+ rows the data list.
    We only want 1 measurement set for each day.
    Selecting 1 row and skipping 3 repeatedly
    when reading the CSV does not gaurentee this.
    """
    print("create_pollution_table_rows called")

    table_rows = []
    pk = []
    for item in data:
        # Make sure we only take 1 of each date
        primary_key = item[8]
        if primary_key in pk:
            continue
        else:
            # Track the dates we find to make sure there is only one of each day
            pk.append(primary_key)

            # Dump the row into a dictionary to make it easier for Schema object
            row = OrderedDict(
                    pollution_date=datetime(*list(map(int, primary_key.split("-")))),
                    site_id=int(item[3]),
                    no2_mean=item[10],
                    no2_max_value=c(item[11]),
                    no2_max_hour=item[12],
                    no2_aqi=item[13],
                    o3_mean=item[15],
                    o3_max_value=c(item[16]),
                    o3_max_hour=item[17],
                    o3_aqi=item[18],
                    so2_mean=item[20],
                    so2_max_value=c(item[21]),
                    so2_max_hour=item[22],
                    so2_aqi=c(item[23]),
                    CO_mean=item[25],
                    CO_max_value=c(item[26]),
                    CO_max_hour=item[27],
                    CO_aqi=c(item[28]),
                )
            table_rows.append(row)
    
    return table_rows

def create_counties_table_rows(data):
    print("create_counties_table_rows called")

    table_rows = []
    pk = []
    for item in data:
        # Extract primary key from row
        county_id = int(item[2])
        if county_id not in pk:
            pk.append(county_id)
            table_rows.append((county_id, item[6], int(item[1])))
    
    return table_rows

def create_addresses_table_rows(data):
    print("create_addresses_table_rows called")

    table_rows = []
    pk = []
    for item in data:
        site_id = int(item[3])
        if site_id not in pk:
            pk.append(site_id)
            address = item[4]
            lat, lng = get_latlng(address)
            data = (
                site_id,
                int(item[1]),
                int(item[2]),
                address,
                float(lat),
                float(lng),
            )
            table_rows.append(data)
    
    return table_rows

if __name__ == "__main__":
    print(get_latlng("Lubbock, TX"))