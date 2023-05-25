import time
import range_finder
import motor_functions
from numpy import linspace
range_finder.startup_lidar()


def calibrate():
    x_range = []
    y_range = []
    range_len = len(x_range)
    x = 1
    y = 0
    for i in range(40, 60):
        x_range.append(round(x, 1))
        y_range.append(round(x, 1))
        x += 0.1
        y += 0.1
    for i in x_range:
        motor_functions.change_position(0, i)
    for i in x_range:
        motor_functions.change_position(i, range_len)
    for i in x_range:
        motor_functions.change_position(range_len, -i)
    for i in x_range:
        motor_functions.change_position(0, 0)

def map_room():
    current_x_position = 0
    current_y_position = 0
    delta_x = 0.1
    delta_y = 0
    x_range = []
    x = 3
    for i in range(30, 90):
        x_range.append(round(x, 1))
        x += 0.1
    print(x_range)

    motor_functions.change_position(current_x_position, current_y_position)
    map = {}
    time.sleep(15)
    for x_position in x_range:
        current_x_position += delta_x
        current_y_position += delta_y
        motor_functions.change_position(x_position, current_y_position)
        time.sleep(2)
        distance = range_finder.distance()
        print(distance)
        map[current_x_position] = distance

calibrate()
map_room()
motor_functions.change_position(0, 0)
