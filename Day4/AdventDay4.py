import numpy as np

def find_xmas(tab):
    number_of_xmas = 0
    for line in tab : 
        number_of_xmas += ( line.count("XMAS")) + (line.count("SAMX"))
    return number_of_xmas

def convert_to_string(lines):
    return [''.join(line) for line in lines]

def get_diagonals(matrix):
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[0])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[0],-matrix.shape[0],-1))
    return diags


if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input4.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        # Count "XMAS" in rows
        number_of_xmas = find_xmas(lines)
        array_lines = np.array([list(line.strip()) for line in lines])

        # Count "XMAS" in columns
        rotate_list=np.rot90(array_lines)
        number_of_xmas += find_xmas(convert_to_string(rotate_list.tolist()))
      
        # Count "XMAS" in diagonals
        diagonals=convert_to_string([list(diag) for diag in get_diagonals(array_lines)])
        number_of_xmas += find_xmas(diagonals)

        #Count "XMAS" in right-to-left columns

        print(number_of_xmas)        