from marshmallow import Schema, fields

class States(Schema):
    state_id = fields.Int()
    state_name = fields.Str()
