import configparser
import time

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from datetime import datetime

mouse = PyMouse()
keyboard = PyKeyboard()

keymap_dict = {
    'up': keyboard.up_key,
    'down': keyboard.down_key,
    'left': keyboard.left_key,
    'right': keyboard.right_key,
    'enter': keyboard.enter_key,
    'ctrl': keyboard.control_l_key,
    'alt': keyboard.alt_l_key,
    'tab': keyboard.tab_key
}


def remove_space(raw_string):
    return str(raw_string).strip()


def string_to_int(value_time_hour_minute_second):
    hour, minute, second = [int(i) for i in str(value_time_hour_minute_second).split(':')]
    return [hour, minute, second]


def key_times_split(key_times):
    key, times = str(key_times).split(',')
    key_new = remove_space(key)
    times_new = remove_space(times)
    return key_new, times_new


def parse_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    config_sections = config.sections()

    config_dict = []
    for section in config_sections:
        option = config.options(section)

        time_hour_minute_second = option[0]
        value_time_hour_minute_second = config[section][time_hour_minute_second]
        time_list = string_to_int(value_time_hour_minute_second)

        keys = option[1:]

        key_times_list = []
        for key in keys:
            key_times = config[section][key]
            key, times = key_times_split(key_times)
            key_times_list.append([key, int(times)])

        config_dict.append([time_list, key_times_list])
    return config_dict


def press_key_custom(key_times_list):
    for key, times in key_times_list:
        for _ in range(times):
            keyboard.press_key(keymap_dict.get(key, key))
            time.sleep(1)


def is_in_time_range(hour, minute, second):
    h = datetime.now().hour
    m = datetime.now().minute
    s = datetime.now().second

    if h == hour and m == minute and second - 1 <= s <= second + 3:
        return True
    else:
        return False


def main():
    config_list = parse_config()

    while 1:
        time.sleep(1)
        for each_config in config_list:
            hour, minute, second = each_config[0]
            key_times_list = each_config[1]

            time_flag = is_in_time_range(hour, minute, second)
            if time_flag:
                press_key_custom(key_times_list)
                time.sleep(4)


if __name__ == '__main__':
    main()
