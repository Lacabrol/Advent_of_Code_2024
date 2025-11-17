if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        rules = {}
        current_rule = None
        correct_update=True
        final_sum = 0

        for line in lines:
            if '|' in line:
                current_rule = line.strip().split('|')

                if (current_rule[0]) in rules:
                    rules[current_rule[0]].append(int(current_rule[1]))
                else:
                    rules[current_rule[0]] = [int(current_rule[1])]

                    
            elif line!='\n':   

                line=[int(x) for x in line.strip().split(',')]
                n = len(line)
                for i in range(n - 1):

                    min_idx = i

                    for j in range(i + 1, n):
                        if line[min_idx] in rules[str(line[j])]:
                            correct_update=False
                            min_idx = j

                    line[i], line[min_idx] = line[min_idx], line[i]

                if not(correct_update):
                    final_sum+=line[len(line)//2]
                    correct_update=True

        print(final_sum)
