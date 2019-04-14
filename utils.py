
def find_unique_state_attributes(data):
    # Put the entire second column into one array
    state_id_column, state_name_column = [], []
    for item in data:  
        state_id_column.append(item[1])

    # Put the entire sixth column into one array
    for item in data:  
        state_name_column.append(item[5])

    # Only return the unique state ids and state names
    return dict(
        unique_state_ids=set(state_id_column), 
        unique_state_names=set(state_name_column),
    )

def find_unique_pollution_attributes(data):
    print("find_unique_pollution_attributes called")
    pollution_date = []
    no2_mean = []
    no2_max_value = []
    no2_max_hour = []
    no2_aqi = []
    o3_mean = []
    o3_max_value = []
    o3_max_hour = []
    o3_aqi = []
    so2_mean = []
    so2_max_value = []
    so2_max_hour = []
    so2_aqi = []
    CO_mean = []
    CO_max_value = []
    CO_max_hour = []
    CO_aqi = []

    for item in data:
        pollution_date.append(item[8])
    for item in data:
        no2_mean.append(item[10])
    for item in data:
        no2_max_value.append(item[11])
    for item in data:
        no2_max_hour.append(item[12])
    for item in data:
        no2_aqi.append(item[13])
    for item in data:
        o3_mean.append(item[15])
    for item in data:
        o3_max_value.append(item[16])
    for item in data:
        o3_max_hour.append(item[17])
    for item in data:
        o3_aqi.append(item[18])
    for item in data:
        so2_mean.append(item[20])
    for item in data:
        so2_max_value.append(item[21])
    for item in data:
        so2_max_hour.append(item[22])
    for item in data:
        so2_aqi.append(item[23])
    for item in data:
        CO_mean.append(item[25])
    for item in data:
        CO_max_value.append(item[26])
    for item in data:
        CO_max_hour.append(item[27])
    for item in data:
        CO_aqi.append(item[28])


    return dict(
        pollution_date=list(set(pollution_date)),
        no2_mean=list(set(no2_mean)),
        no2_max_value=list(set(no2_max_value)),
        no2_max_hour=list(set(no2_max_hour)),
        no2_aqi=list(set(no2_aqi)),
        o3_mean=list(set(o3_mean)),
        o3_max_value=list(set(o3_max_value)),
        o3_max_hour=list(set(o3_max_hour)),
        o3_aqi=list(set(o3_aqi)),
        so2_mean=list(set(so2_mean)),
        so2_max_value=list(set(so2_max_value)),
        so2_max_hour=list(set(so2_max_hour)),
        so2_aqi=list(set(so2_aqi)),
        CO_mean=list(set(CO_mean)),
        CO_max_value=list(set(CO_max_value)),
        CO_max_hour=list(set(CO_max_hour)),
        CO_aqi=list(set(CO_aqi)),
    )

def find_unique_county_attributes(data):
    pass

def find_unique_address_attributes(data):
    pass
