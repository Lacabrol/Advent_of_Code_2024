import numpy as np

def find_trailhead_score(array,x_pos,y_pos,current_number):
    #Check for out-of-bounds or mismatched values
    if(x_pos<0 or x_pos>=array.shape[1] or y_pos<0 or y_pos>=array.shape[0]):
        return 0
    
    # If the current position matches the current number and is 0
    elif(array[y_pos][x_pos]==current_number and current_number==9):
        return 1
    
    # If the current position does not match the current number, return 0
    elif(array[y_pos][x_pos]!=current_number):
        return 0
    
    else:
        # Recursively check all four adjacent positions (up, down, left, right)
        return (find_trailhead_score(array,x_pos+1,y_pos,current_number+1) +
                    find_trailhead_score(array,x_pos-1,y_pos,current_number+1) +
                    find_trailhead_score(array,x_pos,y_pos+1,current_number+1) +
                    find_trailhead_score(array,x_pos,y_pos-1,current_number+1))
    
if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input10.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        array = np.array([list(map(int, line.strip())) for line in lines])  # Convert lines to a 2D numpy array of integers

        zeros_in_array = np.where(array == 0)  # Find the indices of all zeros in the array
        final_score = 0 # Initialize final score

        for i in range(len(zeros_in_array[0])):  # Iterate over each zero position

            final_score += find_trailhead_score(array, zeros_in_array[1][i], zeros_in_array[0][i], 0)  # Calculate the score for each zero position
            
        print(final_score)  # Print the final score