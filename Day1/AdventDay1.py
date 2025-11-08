if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input1.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        left_column = sorted([int(line.split()[0]) for line in lines])
        right_column = sorted([int(line.split()[1]) for line in lines])
        final_sum = 0
        for i in range(len(left_column)): final_sum += abs(left_column[i] - right_column[i])
        print(final_sum)