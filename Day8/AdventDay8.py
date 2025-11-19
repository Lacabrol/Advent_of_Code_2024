import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input8.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        array_lines = np.array([list(line.strip()) for line in lines])
        array_copy = np.copy(array_lines)

        different_elements = np.unique(array_lines)
        different_elements = np.delete(different_elements, np.where(different_elements == '.'))

        positions_frequencies = []

        echo_x, echo_y = 0, 0

        for element in different_elements:
            positions_frequencies = np.where(array_lines == element)
            
            for y_pos1, x_pos1 in zip(positions_frequencies[0], positions_frequencies[1]):

                for y_pos2, x_pos2 in zip(positions_frequencies[0], positions_frequencies[1]):

                    if(y_pos1 != y_pos2 and x_pos1 != x_pos2):
                    
                        echo_y= y_pos1+(y_pos1 - y_pos2) 
                        echo_x= x_pos1+(x_pos1 - x_pos2)

                        if(echo_y >= 0 and echo_y < array_lines.shape[0] and echo_x >= 0 and echo_x < array_lines.shape[1]):
                            array_copy[echo_y,echo_x] = '#'

        print(len(np.where(array_copy == '#')[0]))


                