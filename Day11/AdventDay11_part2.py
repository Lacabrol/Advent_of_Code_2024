from collections import Counter

if __name__ == '__main__':
    # Open the input file "input.txt" in read mode
    with open("input11.txt", "r") as f:

        lines = f.readlines() # Read all lines from the file into a list

        # Initialize variables
        final_sum = 0
        nums = []
        counter, next_counter = Counter(), Counter()
        first_half, second_half = '', ''

        for line in lines:
            nums = [int(x) for x in line.strip().split()]

            # Store counts instead of storing huge arrays
            counter = Counter(nums)

            # Process for 75 iterations
            for i in range(75):  
                next_counter = Counter()

                for number, count in counter.items():

                    # First case: if the number is '0'
                    if number == 0:
                        # Increment count for '1'
                        next_counter[1] += count

                    # Second case: if the length of the number is even
                    elif len(str(number)) % 2 == 0:
                        # Split number into two halves
                        first_half=str(number)[:len(str(number))//2]
                        second_half=str(number)[len(str(number))//2:]

                        # Increment counts for both halves
                        next_counter[int(first_half)] += count
                        next_counter[int(second_half)] += count

                    # Third case: if the length of the number is odd
                    else:
                        # Increment count for number multiplied by 2024
                        next_counter[number * 2024] += count

                # Update counter for next iteration
                counter = next_counter   

            # Add number of stones after 75 iterations
            final_sum += sum(counter.values())

        print(final_sum)
