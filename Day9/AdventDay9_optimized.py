if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input9.txt", "r") as f:
        line = f.readlines()  # Read all lines from the file into a list

        # Convert the first line to a list of integers
        line = [int(x) for x in line[0].strip()]

        # Initialize variables for processing the line
        number=0
        final_sum=0
        last_number=len(line)//2
        iteration_last_number=line[-1]
        position_in_tab=0
        i=0
        # Process the line based on the current number and position
        while number <= last_number :

            # Iterate through the line while the current number is less than or equal to the last number
            if number == last_number:
                # Handle the case when the current number is the last number
                line[i]=iteration_last_number

            # Process even indices by adding the current number multiple times
            if i%2==0:
                for j in range (line[i]):
                    final_sum+=number*position_in_tab
                    position_in_tab+=1
                number+=1
                
                i+=1

            # Handle odd indices by skipping spaces
            else:

                # Process the case when the iteration last number is greater than the current line value
                if (iteration_last_number>line[i]):   
                    for j in range(line[i]):
                        final_sum+=last_number*position_in_tab
                        position_in_tab+=1
                    iteration_last_number-=line[i]
                    i+=1

                # Process the case when the iteration last number is less than or equal to the current line value
                else :
                    for j in range(iteration_last_number):
                        final_sum+=last_number*position_in_tab
                        position_in_tab+=1

                    # Update the line and iteration variables for the next iteration
                    line[i]-=iteration_last_number
                    # Remove the last two elements from the line
                    del line[-2:]
                    # Update the iteration of the last number and last number for the next iteration
                    iteration_last_number=line[-1]
                    last_number-=1
            
        print(final_sum)
