# import something such as csv
import csv

# https://github.com/PyMySQL/PyMySQL
import pymysql

from models import States, Counties, Addresses, Pollutions
connection = pymysql.connect(host="127.0.0.1", user='root', db="pollution")

# Connect to Google Cloud SQL (proxy)
FILENAME = "pollution_us_2000_2016.csv"

counter = 1
# WARNING: The size of this new list will consume 1GB of memory on your computer
new_rows = []

def find_unique_state_attributes():
    # Put the entire second column into one array
    state_id_column, state_name_column = [], []
    for item in new_rows:  
        state_id_column.append(item[1])

    # Put the entire sixth column into one array
    for item in new_rows:  
        state_name_column.append(item[5])

    # Only return the unique state ids and state names
    return set(state_id_column), set(state_name_column)

# Open the CSV document to process and insert into database
with open(FILENAME, "r+") as data:
    content = csv.reader(data, delimiter=",")
    for i, row in enumerate(content):
        if i == 0:
            print(row)
            continue
        if counter != 1:
            counter += 1
        else:
            new_rows.append(row)
            counter += 1
        
        if counter == 4:
            counter = 1

unique_state_ids, unique_state_names = find_unique_state_attributes()
print(len(unique_state_ids), len(unique_state_names))

with connection.cursor() as cursor:
    # Create State table
    for state_id, state_name in zip(unique_state_ids, unique_state_names):
        print(state_id, state_name)
        s = States(state_id, state_name)
        command = "INSERT INTO `States` (`StateID`, `StateName`) VALUES (%s, %s)"
        cursor.execute(command, (s.state_id, s.state_name))
        connection.commit()
    connection.close()

# c = Counties(item[2], item[6], item[5])
#  a = Addresses(item[3], item[1], item[2], item[4], item[8])
#  p = Pollutions(item[8], item[10], item[11], item[12], item[13], item[15], item[16], item[17], item[18], item[20], item[21], item[22], item[23], item[25], item[26], item[27], item[28])    
#  Create a new record
