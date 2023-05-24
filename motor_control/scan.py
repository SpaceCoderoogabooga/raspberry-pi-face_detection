import range_finder
import motor_functions

motor_functions.startup_motor()
range_finder.startup_lidar()

def map_room():
    current_x_position = 0
    current_y_position = 0
    delta_x = 0.01
    delta_y = 0

    motor_functions.change_position(current_x_position, current_y_position)
    map = {}
    for i in range(1000):
        if current_x_position < 12:
            current_x_position += delta_x
        else:
            current_x_position -= delta_x
        if current_y_position < 12:
            current_y_position += delta_y
        else:
            current_y_position -= delta_y
        motor_functions.change_position(current_x_position, current_y_position)
        distance = range_finder.distance()
        map[current_x_position] = distance
        print(map)
