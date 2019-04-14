import csv
import pymysql

from pprint import pprint
from models import States, Counties, Addresses, Pollutions
from utils import (
    find_unique_state_attributes, 
    create_pollution_table_rows,
    find_unique_county_attributes,
    find_unique_address_attributes
)

connection = pymysql.connect(host="127.0.0.1", user="root", db="test", autocommit=True)
FILENAME = "pollution_us_2000_2016.csv"
flags = dict(
    make_state_table=False,
    make_pollutions_table=False,
    make_counties_table=False,
    make_addresses_table=False,
)

states_insertion = "INSERT INTO `States` (`STATEID`, `STATENAME`) VALUES (%s, %s)"
pollutions_insertion = """
INSERT INTO `Pollutions` (
`POLLUTIONDATE`, `NO2MEAN`, `NO2MAXVALUE`,
`NO2MAXHOUR`, `NO2AQI`, `O3MEAN`, `O3MAXVALUE`, 
`O3MAXHOUR`, `O3AQI`, `SO2MEAN`, `SO2MAXVALUE`,
`SO2MAXHOUR`, `SO2AQI`, `COMEAN`, `COMAXVALUE`,
`COMAXHOUR`, `COAQI`
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
counties_insertion = "INSERT INTO `Counties` (`COUNTYID`, `COUNTYNAME`, `STATEID`) VALUES (%s, %s, %s)"
addresses_insertion = "INSERT INTO `Addresses` (`SITEID`, `STATEID`, `COUNTYID`, `ADDRESSNAME`, `POLLUTIONDATE`) VALUES (%s, %s, %s, %s, %s)"

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
            
            # When we finish a group of 3, reset to 1
            if counter == 4:
                counter = 1

    with connection.cursor() as cursor:
        if flags["make_state_table"]:
            # Create States table
            state_data = find_unique_state_attributes(data)
            for state_id, state_name in zip(state_data["unique_state_ids"], state_data["unique_state_names"]):
                data = dict(state_id=state_id, state_name=state_name)
                s = States().dump(data)
                cursor.execute(states_insertion, (s.data["state_id"], s.data["state_name"]))
        
        if flags["make_pollutions_table"]:
            # Create Pollutions table
            pollution_data = create_pollution_table_rows(data)
            for data in pollution_data:
                p = Pollutions().dump(data)
                values = tuple([p.data[key] for key in data.keys()])
                cursor.execute(pollutions_insertion, values)
        
        if flags["make_counties_table"]:
            # Create Counties table
            county_data = find_unique_county_attributes(data)
            for county_id, county_name, state_id in zip(county_data["unique_county_ids"], county_data["unique_county_names"], county_data["unique_state_ids"]):
                data = dict(county_id=county_id, county_name=county_name, state_id=state_id)
                c = Counties().dump(data)
                cursor.execute(counties_insertion, (c.data["county_id"], c.data["county_name"], c.data["state_id"]))
        
        if flags["make_addresses_table"]:
            # Create Addresses table
            address_data = find_unique_address_attributes(data)
            data_iters = (
                address_data["unique_site_ids"], address_data["unique_state_ids"], 
                address_data["unique_county_ids"], address_data["unique_address_names"], 
                address_data["unique_pollution_dates"], 
            )

            for site_id, state_id, county_id, address_name, pollution_date in zip(*data_iters):
                data = dict(site_id=site_id, state_id=state_id, county_id=county_id, address_name=address_name, pollution_date=pollution_date)
                a = Addresses().dump(data)
                values = (a.data["site_id"], a.data["state_id"], a.data["county_id"], a.data["address_name"], a.data["pollution_date"])
                cursor.execute(addresses_insertion, values)
        
        connection.close()


if __name__ == "__main__":
    main()
