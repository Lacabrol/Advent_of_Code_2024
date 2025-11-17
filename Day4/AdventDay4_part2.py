import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input4.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        number_of_xmas = 0
        array_lines = np.array([list(line.strip()) for line in lines])
        letters_upper_row, letters_lower_row = [], []

        a_pos_x, a_pos_y = np.where(array_lines == 'A')

        for i in range(len(a_pos_x)):
            x, y = a_pos_x[i], a_pos_y[i]

            if(x!=0 and y!=0 and x!=array_lines.shape[0]-1 and y!=array_lines.shape[1]-1):
                letters_upper_row = [array_lines[x-1][y-1], array_lines[x-1][y+1]]
                letters_lower_row = [array_lines[x+1][y-1], array_lines[x+1][y+1]]
                if( (letters_upper_row+letters_lower_row).count('M')==2 and (letters_upper_row+letters_lower_row).count('S')==2):
                    if(letters_upper_row[0]==letters_upper_row[1]  or letters_upper_row[0]==letters_lower_row[0]):
                        number_of_xmas += 1
         
        print(number_of_xmas)