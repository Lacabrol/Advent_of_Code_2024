import re

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input3.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        final_sum, first_number, second_number, second_number_end, first_number_end, begin = 0, '', '', '', '', 0
        subword = "mul"
        subword_do = "do"
        new_sequence, positions_mul = [], []


        for line in lines:
            
            new_sequence = [match.start() for match in re.finditer(subword_do, line)]
            new_sequence.append(len(line))

            for pos_new_sequence in new_sequence:
                if begin != -1:

                    positions_mul = [match.start() for match in re.finditer(subword, line[begin:pos_new_sequence])]
                    for pos in positions_mul:
                        pos_mul = pos + begin
                        if(len(line)>pos_mul+len(subword)and line[pos_mul+len(subword)]=='(' ):

                            first_number_end = line.find(',', pos_mul)
                            second_number_end = line.find(')', first_number_end)
                            first_number = line[pos_mul+4:first_number_end].strip()
                            second_number = line[first_number_end+1:second_number_end].strip()

                            if(first_number.isnumeric() and second_number.isnumeric()):
                                final_sum += int(first_number) * int(second_number)
                if(pos_new_sequence!= new_sequence[-1]):
                    if len(line)> pos_new_sequence+len(subword_do)+2 and line[pos_new_sequence+len(subword_do):pos_new_sequence+len(subword_do)+2] == "()":

                        begin = pos_new_sequence + len(subword_do)

                    else:

                        begin = -1

                elif begin != -1:
                    
                    begin = 0

                            
        print(final_sum)