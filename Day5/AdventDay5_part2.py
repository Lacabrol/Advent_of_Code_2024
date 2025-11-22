if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        rules = {}
        current_rule = None
        correct_update=True
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
                n = len(line)
                for i in range(n - 1):
                    # Selection sort algorithm to reorder the sequence based on rules
                    min_idx = i

                    for j in range(i + 1, n):
                        # Compare elements based on rules to find the minimum index
                        if line[min_idx] in rules[str(line[j])]:
                            correct_update=False
                            min_idx = j
                    # Swap the found minimum element with the first element
                    line[i], line[min_idx] = line[min_idx], line[i]
                
                # If the sequence is not correctly ordered according to the rules, update the final sum
                if not(correct_update):
                    final_sum+=line[len(line)//2]
                    correct_update=True

        print(final_sum)
