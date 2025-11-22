if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input9.txt", "r") as f:
        line = f.readlines()  # Read all lines from the file into a list

        # Process the first line of the file
        line=line[0].strip()
        new_line=[]

        for x in range(len(line)):
            # Create a new list with containing the index and the integer value
            if(x%2==0):
                new_line.append([x//2,int(line[x])])
            # Mark odd indices with -1 as a placeholder
            else:
                new_line.append([-1,int(line[x])])
                
        # Initialize variables for processing the new_line list
        final_sum=0
        position_in_tab=sum([x[1] for x in new_line])-1
        match_found=False

        # Process the new_line list until it is empty
        while len(new_line)>0:
            
            # If the last element is a placeholder, adjust position and remove it
            if new_line[-1][0]==-1:
                position_in_tab-=new_line[-1][1]
                new_line.pop(-1)
            
            # If the last element is not a placeholder, try to find a match
            else:
                for index in range (len(new_line)):
                    # Check if the current element is a placeholder
                    if new_line[index][0]==-1:
                        # Check for matches based on the second value
                        if(new_line[index][1]==new_line[-1][1]):
                            # Swap the elements if a match is found
                            new_line[-1], new_line[index] = new_line[index], new_line[-1]
                            # Mark that a match has been found
                            match_found=True
                            break

                        # Handle the case where the current element's second value is more than the last element's second value
                        elif(new_line[index][1]>new_line[-1][1]):
                            # Insert a new element with the adjusted second value
                            new_line.insert(index+1,[new_line[index][0],new_line[index][1]-new_line[-1][1]])
                            # Adjust the current element's second value
                            new_line[index][1]=new_line[-1][1]
                            # Swap the elements
                            new_line[-1], new_line[index] = new_line[index], new_line[-1]
                            # Mark that a match has been found
                            match_found=True
                            break

                # If no match was found, update the final sum and remove the last element
                if not match_found:
                    for j in range (new_line[-1][1]):
                        final_sum+=new_line[-1][0]*position_in_tab
                        position_in_tab-=1

                    new_line.pop(-1)
                # Reset the match_found flag for the next iteration
                match_found=False
                
        # Print the final computed sum
        print(final_sum)
