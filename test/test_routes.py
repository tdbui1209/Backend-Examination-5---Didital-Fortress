import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from app.routes import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_light_setup_valid_input(self):
        data = {
            'light_brightness_list': [100, 200, 300],
            'expected_brightness': 500
        }
        response = self.app.post('/light_setup', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('light_setups', response.json)
        self.assertIsInstance(response.json['light_setups'], list)

    def test_light_setup_missing_light_brightness(self):
        data = {
            'expected_brightness': 500
        }
        response = self.app.post('/light_setup', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'light_brightness is required')

    def test_light_setup_missing_expected_brightness(self):
        data = {
            'light_brightness_list': [100, 200, 300]
        }
        response = self.app.post('/light_setup', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'expected_brightness is required')

    def test_get_light_in_rooms(self):
        '''
        Test the /lights_in_room/<int:room_id> route
        '''
        with patch('app.routes.Room') as mock_room:
            mock_room.query.get.return_value = MagicMock(
                lights=[
                    MagicMock(light_id=1, light_name='light1', color='blue', brightness=100, status='on'),
                    MagicMock(light_id=2, light_name='light2', color='red', brightness=200, status='off'),
                    MagicMock(light_id=3, light_name='light3', color='green', brightness=300, status='on'),
                    MagicMock(light_id=4, light_name='light4', color='yellow', brightness=400, status='off')
                ])
            response = self.app.get('/lights_in_room/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [
                {'light_id': 2, 'light_name': 'light2', 'color': 'red', 'brightness': 200, 'status': 'off'},
                {'light_id': 4, 'light_name': 'light4', 'color': 'yellow', 'brightness': 400, 'status': 'off'},
                {'light_id': 3, 'light_name': 'light3', 'color': 'green', 'brightness': 300, 'status': 'on'},
                {'light_id': 1, 'light_name': 'light1', 'color': 'blue', 'brightness': 100, 'status': 'on'},
            ])


if __name__ == '__main__':
    unittest.main()
