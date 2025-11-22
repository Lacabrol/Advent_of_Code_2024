import re

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input3.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum, first_number, second_number, second_number_end, first_number_end = 0, '', '', '', ''
        subword = "mul"
        positions = []

        for line in lines:
            # Find all positions of the substring "mul" in the current line
            positions = [match.start() for match in re.finditer(subword, line)]

            for pos in positions:
                # Check if the substring "mul" is followed by an opening parenthesis
                if(len(line)>pos+len(subword)and line[pos+len(subword)]=='(' ):
                    # Extract the substrings inside the parentheses
                    first_number_end = line.find(',', pos)
                    second_number_end = line.find(')', first_number_end)
                    first_number = line[pos+len(subword)+1:first_number_end]
                    second_number = line[first_number_end+1:second_number_end]

                    # Check if both extracted substrings are numeric
                    if(first_number.isnumeric() and second_number.isnumeric()):
                        final_sum += int(first_number) * int(second_number)

        print(final_sum)