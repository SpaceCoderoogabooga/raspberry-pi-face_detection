import time
import range_finder
import motor_functions

range_finder.startup_lidar()

def map_room():
    current_x_position = 0
    current_y_position = 0
    delta_x = 0.1
    delta_y = 0
    x_range = range(3, 9, 0.1)
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

map_room()
motor_functions.change_position(0, 0)
