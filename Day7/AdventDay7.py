import math

def update_symbols(symbols):
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
        final_sum = 0
        goal, numbers = 0, []
        symbol_operations = {'+': lambda x, y: x + y,
                             '*': lambda x, y: x * y}
        symbols = []
        last_plus = -1
        current_sum = 0
        
        for line in lines:
            line = line.strip().split(':')
            goal = int(line[0])
            numbers = [int(x) for x in line[1].split()]
            symbols = ['+']*(len(numbers)-1)
            if(math.prod(numbers) == goal):
                final_sum += goal
            else:

                while(symbols.count('*') < len(symbols)):
                    current_sum = numbers[0]
                    for i in range(len(symbols)):
                        current_sum = symbol_operations[symbols[i]](current_sum, numbers[i+1])
                    if(current_sum == goal):
                        final_sum += goal
                        break
                    # Update symbols
                    symbols = update_symbols(symbols)
                    
                    
        print(final_sum)
