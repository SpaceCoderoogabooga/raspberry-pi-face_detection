import range_finder
import motor_functions

range_finder.startup_lidar()

def map_room():
    current_x_position = 0
    current_y_position = 0
    delta_x = 0.1
    delta_y = 0

    motor_functions.change_position(current_x_position, current_y_position)
    map = {}
    print('starting mapping')
    while True:
        current_x_position += delta_x
        current_y_position += delta_y
        motor_functions.change_position(current_x_position, current_y_position)
        distance = range_finder.distance()
        map[current_x_position] = distance
        print(map)

motor_functions.change_position(0, 0)
map_room()
motor_functions.change_position(0, 0)
