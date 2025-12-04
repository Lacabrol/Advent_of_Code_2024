import re

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
        first_quadrant = 0
        seconde_quadrant = 0
        third_quadrant = 0
        fourth_quadrant = 0
        array_shape = (101, 103)

        # Process each line in the input
        for line in lines:
            # Extract integers from the line
            pos_and_vel=list(map(int, numbers.findall(line)))

            # Calculate new positions based on velocity and a time factor (100)
            x = convert_to_pos_in_array(pos_and_vel[0] + (100 * pos_and_vel[2]), array_shape[0])
            y = convert_to_pos_in_array(pos_and_vel[1] + (100 * pos_and_vel[3]), array_shape[1])

            # Determine which quadrant the position falls into and increment the corresponding counter
            if (x< array_shape[0]//2 and y< array_shape[1]//2):
                first_quadrant += 1

            elif (x< array_shape[0]//2 and (array_shape[1]//2)+1<y):
                seconde_quadrant += 1

            elif ((array_shape[0]//2)<x and y< array_shape[1]//2):
                third_quadrant += 1

            elif ((array_shape[0]//2)<x and (array_shape[1]//2)<y):
                fourth_quadrant += 1

        print(first_quadrant * seconde_quadrant * third_quadrant * fourth_quadrant)