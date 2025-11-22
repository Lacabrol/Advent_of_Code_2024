import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input8.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        # Convert lines to a numpy array of characters
        array_lines = np.array([list(line.strip()) for line in lines])
        array_copy = np.copy(array_lines)

        # Get unique elements in the array excluding '.'
        different_elements = np.unique(array_lines)
        different_elements = np.delete(different_elements, np.where(different_elements == '.'))

        # Initialize a list to store positions and frequencies
        positions_frequencies = []

        # Initialize variables to store echo positions
        echo_x, echo_y = 0, 0

        # Iterate through each unique element in the array
        for element in different_elements:

            # Find positions of the current frequencies of the element in the array
            positions_frequencies = np.where(array_lines == element)
            
            # Iterate through each pair of positions for the current element
            for y_pos1, x_pos1 in zip(positions_frequencies[0], positions_frequencies[1]):
                # Iterate through each pair of positions again to compare
                for y_pos2, x_pos2 in zip(positions_frequencies[0], positions_frequencies[1]):

                    # Ensure we are not comparing the same position
                    if(y_pos1 != y_pos2 and x_pos1 != x_pos2):
                        # Calculate the echo position based on the two positions
                        echo_y= y_pos1+(y_pos1 - y_pos2) 
                        echo_x= x_pos1+(x_pos1 - x_pos2)

                        # Mark the echo position in the array copy if it's within bounds
                        if(echo_y >= 0 and echo_y < array_lines.shape[0] and echo_x >= 0 and echo_x < array_lines.shape[1]):
                            array_copy[echo_y,echo_x] = '#'

        # Print the count of '#' in the final array
        print(len(np.where(array_copy == '#')[0]))


                