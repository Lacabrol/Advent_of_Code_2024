import numpy as np

def get_gard_position(array_lines):
    position_guard = np.where(array_lines == '^')
    y_pos, x_pos = position_guard[0][0], position_guard[1][0]
    return y_pos, x_pos


if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input6.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        array_lines = np.array([list(line.strip()) for line in lines])
        array_copy = np.rot90(array_lines,3)
        y_pos, x_pos = get_gard_position(array_copy)

        obstruction_on_the_way = np.where(array_copy[y_pos,x_pos:] == '#')[0]
        while len(obstruction_on_the_way)>0:
            
            x_obstruction = x_pos + obstruction_on_the_way[0]

            array_copy[y_pos,x_pos:x_obstruction-1] = 'X'
            array_copy[y_pos,x_obstruction-1] = '^'

            array_copy=np.rot90(array_copy,1)
            y_pos, x_pos = get_gard_position(array_copy)
            obstruction_on_the_way = np.where(array_copy[y_pos,x_pos:] == '#')[0]

        array_copy[y_pos,x_pos:] = 'X'
        
        print(len(np.where(array_copy == 'X')[0]))



