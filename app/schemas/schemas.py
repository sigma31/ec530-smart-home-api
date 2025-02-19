from marshmallow import Schema, fields, validate

# Using the marshmallow library to deal with JSON serialization and deserialization

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))

class HouseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    owner_id = fields.Int(required=True)

class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    house_id = fields.Int(required=True)

class DeviceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    room_id = fields.Int(required=True)
    status = fields.Str(validate=validate.OneOf(["on", "off"])) # For now on or off

user_schema = UserSchema()
# This is initialized for cases where we have multi-object serialization 
users_schema = UserSchema(many=True)

house_schema = HouseSchema()
houses_schema = HouseSchema(many=True)

room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)

device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)