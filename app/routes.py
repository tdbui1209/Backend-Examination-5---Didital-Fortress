from flask import request, jsonify
from app.app import app
from app.models import Room


@app.route('/light_setup', methods=['POST'])
def light_setup():
    from app.light_utils import find_light_setups
    data = request.get_json()
    try:
        light_brightness_list = data['light_brightness_list']
    except KeyError:
        return jsonify({'error': 'light_brightness_list is required'}), 400
    try:
        expected_brightness = data['expected_brightness']
    except KeyError:
        return jsonify({'error': 'expected_brightness is required'}), 400
    result = []
    find_light_setups(light_brightness_list, expected_brightness, [], 0, result)
    
    return jsonify({'light_setups': result})


@app.route('/lights_in_room/<int:room_id>', methods=['GET'])
def get_lights_in_room(room_id):
    from app.light_utils import rainbow_order
    room = Room.query.get(room_id)
    if room is None:
        return jsonify({'error': 'Room not found'}), 404
    
    lights = room.lights
    sorted_lights = sorted(lights, key=lambda light: rainbow_order(light.color))
    light_list = [{
        'light_id': light.light_id,
        'light_name': light.light_name,
        'color': light.color,
        'brightness': light.brightness,
        'status': light.status
    } for light in sorted_lights]

    return jsonify(light_list)
