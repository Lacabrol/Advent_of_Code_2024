import numpy as np

def get_robot_position(array_lines):
    # Find the position of the robot '@' in the array
    position_robot = np.where(array_lines == '@')
    row, col = position_robot[0][0], position_robot[1][0]
    return row, col

def move(direction, row, col, array):
    # Move the robot in the specified direction if possible
    i=0
    # Move left
    if direction == '<':
        # Check if the robot can move left
        if col == 0:
            return array
        # Move left if the next cell is empty
        if array[row][col-1] == '.':
            array[row][col], array[row][col-1] = '.', '@'
            return array

        # Push the 'O' object to the left if possible
        if array[row][col-1] == 'O':
            i = col - 1
            # Find how far the 'O' object can be pushed
            while i >= 0 and array[row][i] == 'O':
                i -= 1
            # Check if the 'O' object can be pushed into an empty space
            if i >= 0 and array[row][i] == '.':
                array[row][i] = 'O'
                array[row][col-1] = '@'
                array[row][col] = '.'
        # Return the updated array
        return array

    # Move right
    elif direction == '>':
        # Check if the robot can move right
        if col == array.shape[1] - 1:
            return array

        # Move right if the next cell is empty
        if array[row][col+1] == '.':
            array[row][col], array[row][col+1] = '.', '@'
            return array

        # Push the 'O' object to the right if possible
        if array[row][col+1] == 'O':
           
            i = col + 1
            # Find how far the 'O' object can be pushed
            while i < array.shape[1] and array[row][i] == 'O':
                i += 1

            # Check if the 'O' object can be pushed into an empty space
            if i < array.shape[1] and array[row][i] == '.':
                array[row][i] = 'O'
                array[row][col+1] = '@'
                array[row][col] = '.'

        # Return the updated array
        return array

    # Move up
    elif direction == '^':
        # Check if the robot can move up
        if row == 0:
            return array

        # Move up if the next cell is empty
        if array[row-1][col] == '.':
            array[row][col], array[row-1][col] = '.', '@'
            return array

        # Push the 'O' object up if possible
        if array[row-1][col] == 'O':
            i = row - 1
            # Find how far the 'O' object can be pushed
            while i >= 0 and array[i][col] == 'O':
                i -= 1

            # Check if the 'O' object can be pushed into an empty space
            if i >= 0 and array[i][col] == '.':
                array[i][col] = 'O'
                array[row-1][col] = '@'
                array[row][col] = '.'

        # Return the updated array
        return array

    # Move down
    elif direction == 'v':
        # Check if the robot can move down
        if row == array.shape[0] - 1:
            return array

        # Move down if the next cell is empty
        if array[row+1][col] == '.':
            array[row][col], array[row+1][col] = '.', '@'
            return array

        # Push the 'O' object down if possible
        if array[row+1][col] == 'O':
            i = row + 1
            # Find how far the 'O' object can be pushed
            while i < array.shape[0] and array[i][col] == 'O':
                i += 1

            # Check if the 'O' object can be pushed into an empty space
            if i < array.shape[0] and array[i][col] == '.':
                array[i][col] = 'O'
                array[row+1][col] = '@'
                array[row][col] = '.'

        # Return the updated array
        return array

    # If the direction is invalid, return the array unchanged
    return array

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input15.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        array = np.array([])
        second_part = False
        row, col = 0, 0
        final_sum = 0
        all_positions_x, all_positions_y = [], []

        # Process each line in the input
        for line in lines:
            # Check for empty line to separate grid and instructions
            if line == '\n':
                second_part = True
            # Build the initial array from the input lines
            elif not second_part:
                array = np.append(array, [list(line.strip())])
            

            # Process movement instructions
            else:       
                for instruction in line.strip():
                    # Get the current position of the robot
                    row, col = get_robot_position(array)
                    # Move the robot according to the instruction
                    array = move(instruction, row, col, array)

    # Calculate the final sum based on the positions of 'O' objects    
    all_positions_x, all_positions_y = np.where(array == 'O')
    for i in range(len(all_positions_x)):
        final_sum += all_positions_x[i] *100 + all_positions_y[i]

    print(final_sum)
                    
                        