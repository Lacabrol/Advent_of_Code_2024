if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input11.txt", "r") as f:

        line = f.readlines()  # Read all lines from the file into a list
        line = [int(x) for x in line[0].strip().split()]  # Get the first line and strip whitespace
        # Initialize variables
        next_line=[]

        # Process for 25 iterations
        for i in range(25):
            # Iterate over each number in the line
            for number in line:

                # First case: if the number is '0'
                if(number==0):
                    # Replace '0' with '1'
                    next_line.append(1)

                # Second case: if the length of the number is even
                elif(len(str(number))%2==0):
                    # Split the number into two halves
                    first_half=str(number)[:len(str(number))//2]
                    second_half=str(number)[len(str(number))//2:]

                    # Append the two halves to the next line
                    next_line.append(int(first_half))
                    next_line.append(int(second_half))

                # Third case: if the length of the number is odd
                else:
                    # Multiply the number by 2024 and append to the next line
                    next_line.append((number)*2024)

            # Update line for the next iteration
            line = next_line
            next_line = []

        print(len(line))