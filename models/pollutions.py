class Pollutions(object):
    def __init__(
        self, pollution_date, 
        no2_mean, no2_max_value, no2_max_hour, no2_aqi,
        o3_mean, o3_max_value, o3_max_hour, o3_aqi,
        so2_mean, so2_max_value, so2_max_hour, so2_aqi,
        CO_mean, CO_max_value, CO_max_hour, CO_aqi
    ):
        self.pollution_date = pollution_date
        self.no2_mean = no2_mean
        self.no2_max_value = no2_max_value
        self.no2_max_hour = no2_max_hour
        self.no2_aqi = no2_aqi
        self.o3_mean = o3_mean
        self.o3_max_value = o3_max_value
        self.o3_max_hour = o3_max_hour
        self.o3_aqi = o3_aqi
        self.so2_mean = so2_mean 
        self.so2_max_value = so2_max_value 
        self.so2_max_hour = so2_max_hour
        self.so2_aqi = so2_aqi
        self.CO_mean = CO_mean
        self.CO_max_value = CO_max_value 
        self.CO_max_hour = CO_max_hour
        self.CO_aqi = CO_aqi