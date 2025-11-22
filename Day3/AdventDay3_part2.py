import re

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input3.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum, first_number, second_number, second_number_end, first_number_end, begin = 0, '', '', '', '', 0
        subword = "mul"
        subword_do = "do"
        new_sequence, positions_mul = [], []


        for line in lines:
            # Find all positions of the substring "do" in the current line
            new_sequence = [match.start() for match in re.finditer(subword_do, line)]
            # Append the length of the line to the list of positions
            new_sequence.append(len(line))

            for pos_new_sequence in new_sequence:
                # Not processing if last instruction is "don't"
                if begin != -1:
                    # Find all positions of the substring "mul" in the current segment of the line
                    positions_mul = [match.start() for match in re.finditer(subword, line[begin:pos_new_sequence])]
                    for pos in positions_mul:
                        # Adjust position relative to the entire line
                        pos_mul = pos + begin
                        # Check if the substring "mul" is followed by an opening parenthesis
                        if(len(line)>pos_mul+len(subword)and line[pos_mul+len(subword)]=='(' ):
                            # Extract the substrings inside the parentheses
                            first_number_end = line.find(',', pos_mul)
                            second_number_end = line.find(')', first_number_end)
                            first_number = line[pos_mul+4:first_number_end].strip()
                            second_number = line[first_number_end+1:second_number_end].strip()
                            # Check if both extracted substrings are numeric
                            if(first_number.isnumeric() and second_number.isnumeric()):
                                final_sum += int(first_number) * int(second_number)

                # Determine the beginning of the next segment
                if(pos_new_sequence!= new_sequence[-1]):
                    # Check if the "do" instruction is followed by "()" and not "n't()"
                    if len(line)> pos_new_sequence+len(subword_do)+2 and line[pos_new_sequence+len(subword_do):pos_new_sequence+len(subword_do)+2] == "()":
                        # Set begin to the position after "do()"
                        begin = pos_new_sequence + len(subword_do)+2
                    # If "do" is followed by "n't()", set begin to -1 to skip processing
                    else:

                        begin = -1
                # Reset begin to 0 if it was set to -1 and we are a new segment is starting
                elif begin != -1:
                    
                    begin = 0
                            
        print(final_sum)