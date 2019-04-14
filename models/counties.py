from marshmallow import Schema, fields

class Counties(Schema):
    county_id = fields.Int()
    county_name = fields.String()
    state_id = fields.Int()
