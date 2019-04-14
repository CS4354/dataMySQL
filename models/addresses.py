from marshmallow import Schema, fields

class Addresses(Schema):
    site_id = fields.Int()
    state_id = fields.Int()
    county_id = fields.Int()
    address_name = fields.String()
    pollution_date = fields.Date()
