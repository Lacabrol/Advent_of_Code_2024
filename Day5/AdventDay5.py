if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        rules = {}
        current_rule = None

        correct=True
        final_sum = 0
        for line in lines:
            # Process each line to build rules or check correctness
            if '|' in line:
                current_rule = line.strip().split('|')

                # Build the rules dictionary
                if (current_rule[0]) in rules:
                    rules[current_rule[0]].append(int(current_rule[1]))
                else:
                    rules[current_rule[0]] = [int(current_rule[1])]

            # Check lines that are not empty and do not contain '|'
            elif line!='\n':   
                # Process lines that represent sequences to check correctness
                line=[int(x) for x in line.strip().split(',')]

                for i in range(1,len(line)):
                    # Check if any element in the current segment violates the rules
                    if (any(x in rules[str(line[i])] for x in line[0:i])):
                        correct=False
                        break
                
                # If the sequence is correct, add the middle element to the final sum
                if correct:
                    final_sum+=line[len(line)//2]
                    
                # Reset the correctness flag for the next sequence
                correct=True

        print(final_sum)
