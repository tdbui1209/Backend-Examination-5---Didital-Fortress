def find_light_setups(light_brightness_list, expected_brightness, current_set=[], index=0, result=[]):
    '''
    Find all possible light setups that can achieve the expected brightness
    '''
    if expected_brightness == 0:
        result.append(list(current_set))
        return

    if index == len(light_brightness_list):
        return

    if expected_brightness >= light_brightness_list[index]:
        current_set.append(light_brightness_list[index])
        find_light_setups(light_brightness_list, expected_brightness - light_brightness_list[index],
                          current_set, index, result)
        current_set.pop()

    find_light_setups(light_brightness_list, expected_brightness, current_set, index + 1, result)


def rainbow_order(color):
    '''
    Return the order of the color in the rainbow
    '''
    rainbow_order_map = {
        'red': 1,
        'orange': 2,
        'yellow': 3,
        'green': 4,
        'blue': 5,
        'indigo': 6,
        'violet': 7
    }
    return rainbow_order_map.get(color)
