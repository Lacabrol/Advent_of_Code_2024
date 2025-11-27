def check_safety(trend, difference):
    # Check if the absolute difference exceeds 3
    if (abs(difference)>3 or (increase_or_decrease<0 and difference>0) or (increase_or_decrease>0 and difference<0)or increase_or_decrease==0 or difference==0):
        return False
    return True

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input2.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum = 0
        safe=True
        new_line = []
        # Negative, positive or stable trend
        increase_or_decrease=0
        for line in lines:
            line = line.split()
            # Determine the overall trend
            increase_or_decrease = int(line[1]) - int(line[0])
            for i in range (0,len(line)-1):
                # Calculate the difference between consecutive elements
                difference = int(line[i+1]) - int(line[i])
                # Check the safety conditions
                safe = check_safety(increase_or_decrease, difference)
                if not safe:
                    break
            # Update the final sum based on safety
            if safe: 
                final_sum += 1
            
            else:
                # Try removing one element to achieve safety
                safe=True
                # Check all possible removals
                for remove_index in range(len(line)):
                    new_line = line[:remove_index] + line[remove_index+1:]
                    # Determine the overall trend for the new line
                    increase_or_decrease = int(new_line[1]) - int(new_line[0])
                    # Check safety for the new line
                    for j in range (0,len(new_line)-1):
                        # Calculate the difference between consecutive elements
                        difference = int(new_line[j+1]) - int(new_line[j])
                        # Check the safety conditions
                        safe = check_safety(increase_or_decrease, difference)
                        if not safe:
                            break
                    
                    if safe:
                        final_sum += 1
                        break
                    
                    # Reset safe to True for the next removal attempt
                    safe=True
            
        print(final_sum)