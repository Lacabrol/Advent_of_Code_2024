import numpy as np

def get_gard_position(array_lines):
    # Find the position of the guard '^' in the array
    position_guard = np.where(array_lines == '^')
    y_pos, x_pos = position_guard[0][0], position_guard[1][0]
    return y_pos, x_pos


if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input6.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        # Convert lines to a numpy array of characters
        array_lines = np.array([list(line.strip()) for line in lines])
        # Create a copy of the array and rotate it 270 degrees
        array_copy = np.rot90(array_lines,3)
        # Get the initial position of the guard
        y_pos, x_pos = get_gard_position(array_copy)

        # Find the positions of obstructions '#' in the path of the guard '^'
        obstruction_on_the_way = np.where(array_copy[y_pos,x_pos:] == '#')[0]

        # Continue until there are no obstructions in the way
        while len(obstruction_on_the_way)>0:
            # Calculate the x-coordinate of the first obstruction
            x_obstruction = x_pos + obstruction_on_the_way[0]

            # Mark the path of the guard with 'X' and place the guard symbol '^' before the obstruction
            array_copy[y_pos,x_pos:x_obstruction-1] = 'X'
            array_copy[y_pos,x_obstruction-1] = '^'

            # Rotate the array 90 degrees clockwise and update the guard's position
            array_copy=np.rot90(array_copy,1)
            y_pos, x_pos = get_gard_position(array_copy)
            obstruction_on_the_way = np.where(array_copy[y_pos,x_pos:] == '#')[0]

        # Mark the remaining path of the guard with 'X'
        array_copy[y_pos,x_pos:] = 'X'

        # Print the count of 'X' in the final array
        print(len(np.where(array_copy == 'X')[0]))