from marshmallow import Schema, fields, post_load

class OrderSchema(Schema):
    orderid = fields.Str()
    sku = fields.Str()
    qty = fields.Int()
