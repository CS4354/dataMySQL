import csv
import pymysql

from models import States, Counties, Addresses, Pollutions
from utils import (
    find_unique_state_attributes, 
    find_unique_pollution_attributes,
    find_unique_county_attributes,
    find_unique_address_attributes
)

connection = pymysql.connect(host="127.0.0.1", user="root", db="test")
FILENAME = "pollution_us_2000_2016.csv"
flags = dict(
    make_state_table=False,
    make_pollutions_table=True,
    make_counties_table=True,
    make_addresses_table=True,
)

def main():
    counter = 1
    data = []

    # Open the CSV document to process and insert into database
    with open(FILENAME, "r+") as rows:
        content = csv.reader(rows, delimiter=",")
        for i, row in enumerate(content):
            # Skip header
            if i == 0:
                print(row)
                continue
            # Read row only if counter is 1
            if counter != 1:
                counter += 1
            else:
                data.append(row)
                counter += 1
            
            # When we finish a group of 4, reset to 1
            if counter == 4:
                counter = 1

    state_data = find_unique_state_attributes(data)
    pollution_data = find_unique_pollution_attributes(data)
    # county_data = find_unique_county_attributes(data)
    # address_data = find_unique_address_attributes(data)

    with connection.cursor() as cursor:
        
        if flags["make_state_table"]:
            # Create State table
            for state_id, state_name in zip(state_data["unique_state_ids"], state_data["unique_state_names"]):
                data = dict(state_id=state_id, state_name=state_name)
                s = States().dump(data)
                query = "INSERT INTO `States` (`STATEID`, `STATENAME`) VALUES (%s, %s)"
                cursor.execute(query, (s.data["state_id"], s.data["state_name"]))
                connection.commit()
        
        if flags["make_pollutions_table"]:
            idx = 0
            print(pollution_data.keys())
            bound = len(pollution_data[list(pollution_data.keys())[0]])
            print("pd len:", bound)

            while idx < bound:
                for (pollution_date, no2_mean, no2_max_value, no2_max_hour,
                        no2_aqi, o3_mean, o3_max_value, o3_max_hour, 
                        o3_aqi, so2_mean, so2_max_value, so2_max_hour,
                        so2_aqi, CO_mean, CO_max_value, CO_max_hour, CO_aqi) in [pollution_data[key][i] for key in pollution_data.keys()]:
                    
                    print(pollution_date, no2_mean, no2_max_value, no2_max_hour, no2_aqi, o3_mean, o3_max_value, o3_max_hour, o3_aqi, so2_mean, so2_max_value, so2_max_hour, so2_aqi, CO_mean, CO_max_value, CO_max_hour, CO_aqi)
                    idx += 1

        connection.close()


if __name__ == "__main__":
    main()
