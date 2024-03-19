import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.light_utils import find_light_setups, rainbow_order


class TestLightUtils(unittest.TestCase):
    def test_find_light_setups_example_1(self):
        # Example 1
        light_brightness_list = [200, 300, 600, 700]
        expected_brightness = 700
        result = []
        find_light_setups(light_brightness_list, expected_brightness, [], 0, result)
        self.assertEqual(result, [[200, 200, 300], [700]])

    def test_find_light_setups_example_2(self):
        # Example 2
        light_brightness_list = [200, 300, 500]
        expected_brightness = 800
        result = []
        find_light_setups(light_brightness_list, expected_brightness, [], 0, result)
        self.assertEqual(result, [[200, 200, 200, 200], [200, 300, 300], [300, 500]])

    def test_find_light_setups_example_3(self):
        # Example 3
        light_brightness_list = [200]
        expected_brightness = 100
        result = []
        find_light_setups(light_brightness_list, expected_brightness, [], 0, result)
        self.assertEqual(result, [])

    def test_rainbow_order(self):
        self.assertEqual(rainbow_order('red'), 1)
        self.assertEqual(rainbow_order('orange'), 2)
        self.assertEqual(rainbow_order('yellow'), 3)
        self.assertEqual(rainbow_order('green'), 4)
        self.assertEqual(rainbow_order('blue'), 5)
        self.assertEqual(rainbow_order('indigo'), 6)
        self.assertEqual(rainbow_order('violet'), 7)


if __name__ == '__main__':
    unittest.main()