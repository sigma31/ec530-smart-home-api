from flask import Blueprint, request, jsonify
from app.models import db, User, House, Room, Device
from app.schemas import user_schema, users_schema, house_schema, houses_schema, room_schema, rooms_schema, device_schema, devices_schema

api = Blueprint('api', __name__)

# User Routes
@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = User(name=data["name"], email=data["email"], password_hash="hashed_password")
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

# House Routes
@api.route("/houses", methods=["POST"])
def create_house():
    data = request.get_json()
    errors = house_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    house = House(name=data["name"], owner_id=data["owner_id"])
    db.session.add(house)
    db.session.commit()
    return house_schema.jsonify(house), 201

@api.route("/houses", methods=["GET"])
def get_houses():
    houses = House.query.all()
    return jsonify(houses_schema.dump(houses))

# Room Routes
@api.route("/rooms", methods=["POST"])
def create_room():
    data = request.get_json()
    errors = room_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    room = Room(name=data["name"], house_id=data["house_id"])
    db.session.add(room)
    db.session.commit()
    return room_schema.jsonify(room), 201

@api.route("/rooms", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()
    return jsonify(rooms_schema.dump(rooms))

# Device Routes
@api.route("/devices", methods=["POST"])
def create_device():
    data = request.get_json()
    errors = device_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    device = Device(name=data["name"], room_id=data["room_id"], status=data.get("status", "off"))
    db.session.add(device)
    db.session.commit()
    return device_schema.jsonify(device), 201

@api.route("/devices", methods=["GET"])
def get_devices():
    devices = Device.query.all()
    return jsonify(devices_schema.dump(devices))