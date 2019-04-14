from datetime import datetime
from collections import OrderedDict

def c(cell):
    """
    clean annoying cell values
    """
    if " " in cell or cell == "":
        cell = -1 # Unknown or corrupt value
    return int(float(cell))

def find_unique_state_attributes(data):
    print("find_unique_state_attributes called")
    
    state_id_column, state_name_column = [], []
    for item in data:
        # Put the entire second column into one array
        state_id_column.append(item[1])
        # Put the entire sixth column into one array
        state_name_column.append(item[5])
   
    # Only return the unique state ids and state names
    return OrderedDict(
        unique_state_ids=set(state_id_column), 
        unique_state_names=set(state_name_column),
    )

def create_pollution_table_rows(data):
    """
    There are 500k+ rows the data list.
    We only want 1 measurement set for each day.
    Selecting 1 row and skipping 3 repeatedly
    when reading the CSV does not gaurentee this.
    """
    print("find_unique_pollution_attributes called")

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

def find_unique_county_attributes(data):
    print("find_unique_county_attributes called")

    county_ids_column = []
    county_names_column = []
    state_ids_column = []

    for item in data:
        county_ids_column.append(int(item[2]))
        county_names_column.append(item[6])
        state_ids_column.append(int(item[1]))
    
    return OrderedDict(
        unique_county_ids=set(county_ids_column),
        unique_county_names=set(county_names_column), 
        unique_state_ids=set(state_ids_column),
    )

def find_unique_address_attributes(data):
    print("find_unique_address_attributes called")

    site_ids_column = []
    state_ids_column = []
    county_ids_column = []
    address_names_column = []
    pollution_dates_column = []

    for item in data:
        site_ids_column.append(int(item[3]))
        state_ids_column.append(int(item[1]))
        county_ids_column.append(int(item[2]))
        address_names_column.append(item[4])
        pollution_dates_column.append(datetime(*list(map(int, item[8].split("-")))))
    
    return OrderedDict(
        unique_site_ids=set(site_ids_column),
        unique_state_ids=set(state_ids_column),
        unique_county_ids=set(county_ids_column),
        unique_address_names=set(address_names_column),
        unique_pollution_dates=set(pollution_dates_column),
    )
