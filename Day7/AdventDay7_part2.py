def update_symbols(symbols):
    # Define the operations in order
    ops = ['+', '*', '||']
    # Initialize index
    i = 0
    while i < len(symbols):
        # Get the current operation index
        current = ops.index(symbols[i])
        # Check if we can increment this position
        if current < 2:   
            symbols[i] = ops[current + 1]
            return symbols
        else:
            # Reset to first operation and carry over
            symbols[i] = ops[0]  
            i += 1
    return symbols
 

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input7.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum = 0
        goal, numbers = 0, []
        symbols = []
        last_plus = -1
        current_sum = 0
        done = False
        new_symbols = []
        
        # Initialize the symbols list with all operations
        symbol_operations = {'+': lambda x, y: x + y,
                             '*': lambda x, y: x * y,
                             '||': lambda x, y: int(str(x) + str(y))}
        
        
        for line in lines:
            line = line.strip().split(':')

            # Parse the goal and numbers from the input line
            goal = int(line[0])
            numbers = [int(x) for x in line[1].split()]

            # Initialize the symbols list with all '+' operations
            symbols = ['+']*(len(numbers)-1)

            # Check if the numbers concatenated equal the goal
            if(''.join(line[1].split())== str(goal)):
                final_sum += goal

            # If not equal, try different combinations of operations
            else:

                done = False
                # Try different combinations of operations until done
                while(not done):
                    # Initialize current sum
                    current_sum = numbers[0]

                    # Calculate the current calculation based on the symbols and numbers
                    for i in range(len(symbols)):
                        current_sum = symbol_operations[symbols[i]](current_sum, numbers[i+1])

                    # Check if the current calculation matches the goal and break if it does
                    if(current_sum == goal):
                        final_sum += goal
                        break

                    # Update symbols
                    new_symbols = update_symbols(symbols.copy())

                    # Check if we have cycled through all combinations
                    if symbols == new_symbols or new_symbols == ['+'] * len(symbols):

                        # If we have returned to the initial state, stop the loop
                        done = True
                        
                    # Update symbols for the next iteration
                    symbols = new_symbols            
                    
        print(final_sum)
