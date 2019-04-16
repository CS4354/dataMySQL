import csv
import pymysql

from pprint import pprint
from models import States, Counties, Addresses, Pollutions
from utils import (
    create_states_table_rows, 
    create_pollution_table_rows,
    create_counties_table_rows,
    create_addresses_table_rows,
)

FILENAME = "pollution_us_2000_2016.csv"
states_insertion = "INSERT INTO `States` (`STATEID`, `STATENAME`) VALUES (%s, %s)"
pollutions_insertion = "INSERT INTO `Pollutions` (" \
"`POLLUTIONDATE`, `SITEID`, `NO2MEAN`, `NO2MAXVALUE`," \
"`NO2MAXHOUR`, `NO2AQI`, `O3MEAN`, `O3MAXVALUE`," \
"`O3MAXHOUR`, `O3AQI`, `SO2MEAN`, `SO2MAXVALUE`," \
"`SO2MAXHOUR`, `SO2AQI`, `COMEAN`, `COMAXVALUE`," \
"`COMAXHOUR`, `COAQI`" \
") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
counties_insertion = "INSERT INTO `Counties` (`COUNTYID`, `COUNTYNAME`, `STATEID`) VALUES (%s, %s, %s)"
addresses_insertion = "INSERT INTO `Addresses` (`SITEID`, `STATEID`, `COUNTYID`, `ADDRESSNAME`, `LATITUDE`, `LONGITUDE`) VALUES (%s, %s, %s, %s, %s, %s)"

def create_tables():
    connection = pymysql.connect(host="127.0.0.1", user="root", db="test", autocommit=True)
    counter = 1
    data = []
    flags = dict(
        make_states_table=False,
        make_counties_table=False,
        make_addresses_table=False,
        make_pollutions_table=True,
    )

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
        if flags["make_states_table"]:
            # Create States table
            state_data = create_states_table_rows(data)
            for row in state_data:
                data = dict(state_id=row[0], state_name=row[1])
                s = States().dump(data)
                cursor.execute(states_insertion, (s.data["state_id"], s.data["state_name"]))
            connection.commit()

        if flags["make_counties_table"]:
            # Create Counties table
            county_data = create_counties_table_rows(data)
            for row in county_data:
                data = dict(county_id=row[0], county_name=row[1], state_id=row[2])
                c = Counties().dump(data)
                cursor.execute(counties_insertion, (c.data["county_id"], c.data["county_name"], c.data["state_id"]))
            connection.commit()

        if flags["make_addresses_table"]:
            # Create Addresses table
            address_data = create_addresses_table_rows(data)
            
            for row in address_data:
                data = dict(site_id=row[0], state_id=row[1], county_id=row[2], address_name=row[3], latitude=row[4], longitude=row[5])
                a = Addresses().dump(data)
                values = (a.data["site_id"], a.data["state_id"], a.data["county_id"], a.data["address_name"], a.data["latitude"], a.data["longitude"])
                cursor.execute(addresses_insertion, values)
            connection.commit()

        if flags["make_pollutions_table"]:
            # Create Pollutions table
            pollution_data = create_pollution_table_rows(data)
            for data in pollution_data:
                p = Pollutions().dump(data)
                values = tuple([p.data[key] for key in data.keys()])
                cursor.execute(pollutions_insertion, values)
            connection.commit()

        connection.close()

if __name__ == "__main__":
    create_tables()