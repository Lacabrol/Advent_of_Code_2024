import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input9.txt", "r") as f:
        line = f.readlines()  # Read all lines from the file into a list

        # Convert the first line to a list of integers
        line = [int(x) for x in line[0].strip()]

        # Initialize variables for processing the line
        new_line=[]
        number=0
        final_sum=0

        for i in range(len(line)):
            # Process even indices by adding the current number multiple times
            if i%2==0:
                new_line+=[str(number)]*line[i]
                number+=1

            # Process odd indices by adding spaces
            else:
                new_line+=['.']*line[i]

        # Convert the new line to a numpy array
        array=np.array(new_line)
        # Get positions of digits in the array
        digit_positions = np.where(array != '.')[0]

        for i in range(len(array)):

            # If there is a space at the current position
            if array[i] == '.':

                array[i] = array[digit_positions[-1]]  # Assign the last digit to the space
                array[digit_positions[-1]] = '.'  # Set the last digit position to space
                digit_positions = np.delete(digit_positions, -1)  # Remove the last digit position

            # Add the product of the digit and its index to the final sum
            final_sum+=int(array[i])*i

            # Check if there are no more digits left to process
            if np.where(array[i+1:] !='.')[0].size == 0:
                break
            
        # Print the final sum
        print(final_sum)
