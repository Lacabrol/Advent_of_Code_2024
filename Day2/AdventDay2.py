if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input2.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        final_sum = 0
        safe=True
        increase_or_decrease=0
        for line in lines:
            line = line.split()
            increase_or_decrease = int(line[1]) - int(line[0])
            for i in range (0,len(line)-1):
                difference = int(line[i+1]) - int(line[i])
                if (abs(difference)>3 or (increase_or_decrease<0 and difference>0) or (increase_or_decrease>0 and difference<0)or increase_or_decrease==0 or difference==0):
                    safe=False
                    break
            if safe: 
                final_sum += 1
            safe=True
        print(final_sum)