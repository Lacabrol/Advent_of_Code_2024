import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input4.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        number_of_xmas = 0
        array_lines = np.array([list(line.strip()) for line in lines])
        letters_upper_row, letters_lower_row = [], []

        # Find positions of 'A' in the array
        a_pos_x, a_pos_y = np.where(array_lines == 'A')

        for i in range(len(a_pos_x)):
            # Iterate through each position of 'A'
            x, y = a_pos_x[i], a_pos_y[i]

            # Check if 'A' is not on the border of the array
            if(x!=0 and y!=0 and x!=array_lines.shape[0]-1 and y!=array_lines.shape[1]-1):
                # Get the letters in the upper and lower diagonal positions
                letters_upper_row = [array_lines[x-1][y-1], array_lines[x-1][y+1]]
                letters_lower_row = [array_lines[x+1][y-1], array_lines[x+1][y+1]]
                
                # Check if the combined letters contain exactly two 'M's and two 'S's
                if( (letters_upper_row+letters_lower_row).count('M')==2 and (letters_upper_row+letters_lower_row).count('S')==2):
                    # Check the specific conditions for "MAS" and "SAM" are a cross shape                   
                    if(letters_upper_row[0]==letters_upper_row[1]  or letters_upper_row[0]==letters_lower_row[0]):
                        number_of_xmas += 1
         
        print(number_of_xmas)