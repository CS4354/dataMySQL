from marshmallow import Schema, fields

class LocationSchema(Schema):
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)

class MarkerDataSchema(Schema):
    no2_max_value = fields.Int()
    no2_max_hour = fields.Int()
    no2_aqi = fields.Int()
    o3_mean = fields.Float()
    o3_max_value = fields.Int()
    o3_max_hour = fields.Int()
    o3_aqi = fields.Int()
    so2_mean = fields.Float()
    so2_max_value = fields.Int() 
    so2_max_hour = fields.Int()
    so2_aqi = fields.Int()
    CO_mean = fields.Float()
    CO_max_value = fields.Int() 
    CO_max_hour = fields.Int()
    CO_aqi = fields.Int()

class Marker(Schema):
    location = LocationSchema()
    data = MarkerDataSchema()
    state_id = fields.Int()
