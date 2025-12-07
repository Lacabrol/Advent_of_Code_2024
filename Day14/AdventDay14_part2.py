import re
import numpy as np
from PIL import Image

#The answer is 6668

def convert_to_pos_in_array(pos, array_shape):
    # Convert a position to fit within the bounds of an array shape using wrapping
    if pos > 0:
        # Use modulo to wrap around positive positions
        return pos % array_shape
    
    else:
        # Adjust negative positions to wrap around correctly
        pos +=(abs(pos)//array_shape) * array_shape

        # If the position is still negative after adjustment, add the array shape once more
        if pos < 0:
            pos += array_shape
        return pos

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input14.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        # Regular expression to find all integers in a line
        numbers = re.compile('-?\d+')

        # Initialize variables
        pos_and_vel = []
        array_shape = (101, 103)
        array = np.zeros(array_shape, dtype=int)

       
        for i in range(10000):
             # Process each line in the input
            for line in lines:
                # Extract integers from the line
                pos_and_vel=list(map(int, numbers.findall(line)))

                # Calculate new positions based on velocity and a time factor (i)
                x = convert_to_pos_in_array(pos_and_vel[0] + (i * pos_and_vel[2]), array_shape[0])
                y = convert_to_pos_in_array(pos_and_vel[1] + (i * pos_and_vel[3]), array_shape[1])
                array[x][y] = 1
            # Create and save an image from the array
            img = Image.fromarray(np.uint8(array * 255) , 'L')
            img.save("output_" + str(i) + ".png")
            array.fill(0)