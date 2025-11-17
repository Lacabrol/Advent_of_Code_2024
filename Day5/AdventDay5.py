if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        rules = {}
        current_rule = None

        correct=True
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
                for i in range(1,len(line)):
                    if (any(x in rules[str(line[i])] for x in line[0:i])):
                        correct=False
                        break
                
                if correct:
                    final_sum+=line[len(line)//2]
                correct=True

        print(final_sum)
