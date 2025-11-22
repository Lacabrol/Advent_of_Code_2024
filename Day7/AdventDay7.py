import math

def update_symbols(symbols):
    # Update the symbols list by toggling '+' and '*' to generate all combinations for a specific length
    if symbols[0] == '+':
        symbols[0] = '*'
    else:
        i=0
        while(symbols[i] == '*' and i < len(symbols)):
            symbols[i] = '+'
            i+=1
        symbols[i] = '*'
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
        
        # Define the operations for '+' and '*'
        symbol_operations = {'+': lambda x, y: x + y,
                             '*': lambda x, y: x * y}
        
        for line in lines:
            line = line.strip().split(':')
            
            # Parse the goal and numbers from the input line
            goal = int(line[0])
            numbers = [int(x) for x in line[1].split()]

            # Initialize the symbols list with all '+' operations
            symbols = ['+']*(len(numbers)-1)

            # Check if the product of numbers equals the goal
            if(math.prod(numbers) == goal):
                final_sum += goal

            else:
                # Iterate through all combinations of '+' and '*' symbols
                while(symbols.count('*') < len(symbols)):
                    # Initialize the current calculation with the first number
                    current_sum = numbers[0]

                    # Calculate the current calculation based on the symbols and numbers
                    for i in range(len(symbols)):
                        current_sum = symbol_operations[symbols[i]](current_sum, numbers[i+1])

                    # Check if the current calculation matches the goal and break if it does
                    if(current_sum == goal):
                        final_sum += goal
                        break

                    # Update symbols to the next combination
                    symbols = update_symbols(symbols)
                    
                    
        print(final_sum)
