import numpy as np

def get_gard_position(array_lines):

    # Find the position of the guard '^' in the array
    position_guard = np.where(array_lines == '^')
    return position_guard[0][0], position_guard[1][0]


def loop_check(array):
    # Create a copy of the array to simulate on
    arr = array.copy()

    # Create a copy of the array and rotate it 270 degrees
    arr = np.rot90(arr, 3)

    # Get the initial position of the guard
    y_pos, x_pos = get_gard_position(arr)

    # Initial orientation: guard faces UP
    rotation = 0  
    visited_states = set()
    obstruction = np.where(arr[y_pos, x_pos:] == '#')[0]

    x_obstruction = -1

    # Main simulation loop
    while len(obstruction) != 0:
        # Check for loops
        state = (y_pos, x_pos, rotation)
        
        # If the current state has been visited before, a loop is detected
        if state in visited_states:
            return True  
        
        visited_states.add(state)    

        # Calculate the x-coordinate of the first obstruction
        x_obstruction = x_pos + obstruction[0]

        # Mark the path of the guard with 'X' and place the guard symbol '^' before the obstruction
        arr[y_pos, x_pos:x_obstruction-1] = 'X'
        arr[y_pos, x_obstruction-1] = '^'

        # Rotate the array 90 degrees clockwise and update the guard's position
        arr = np.rot90(arr, 1)
        rotation = (rotation + 1) % 4
        y_pos, x_pos = get_gard_position(arr)

        # Find the positions of obstructions '#' in the path of the guard '^'
        obstruction = np.where(arr[y_pos, x_pos:] == '#')[0]

    return False

if __name__ == '__main__':
    with open("input6.txt", "r") as f:
        lines = f.readlines()
        array = np.array([list(line.strip()) for line in lines])

        # Find starting position (cannot place obstruction there)
        y_pos, x_pos = np.where(array == '^')
        y_pos, x_pos = y_pos[0], x_pos[0]

        # Initialize variables
        final_sum = 0
        array_copy = array.copy()

        # Try placing one obstruction at each empty cell
        for y in range(array.shape[0]):
            for x in range(array.shape[1]):

                # Only place obstruction on empty cells, not on guard
                if (array[y, x] == '.') and not((y, x) == (y_pos, x_pos)):    

                    # Place obstruction
                    array_copy[y, x] = '#'             

                    # If placement causes loop → valid placement
                    if loop_check(array_copy):
                        final_sum += 1
                
                # Remove obstruction
                array_copy = array.copy()

        print(final_sum)