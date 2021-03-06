from marshmallow import Schema, fields

class Addresses(Schema):
    site_id = fields.Int()
    state_id = fields.Int()
    county_id = fields.Int()
    address_name = fields.String()
    latitude = fields.Float()
    longitude = fields.Float()
