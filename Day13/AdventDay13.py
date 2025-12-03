if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input13.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        final_sum = 0

        button_A, button_B, prize = [], [], []

        nb_A_pressed = 0
        nb_B_pressed = 0

        current_x = 0
        current_y = 0

        # Process input lines in groups of four
        for i in range(0,len(lines),4):
            # Replace '+', '=' and ',' with spaces for easier splitting
            lines[i] = lines[i].replace('+',' ').replace(',',' ')
            lines[i+1] = lines[i+1].replace('+',' ').replace(',',' ')
            lines[i+2] = lines[i+2].replace('=',' ').replace(',',' ')
            
            # Extract integers from the lines
            button_A = [int(x) for x in lines[i].split() if x.isdigit()]
            button_B = [int(x) for x in lines[i+1].split() if x.isdigit()]
            prize = [int(x) for x in lines[i+2].split() if x.isdigit()]

            # Calculate the number of times button B can be pressed without exceeding the prize coordinates
            nb_B_pressed = prize[0]//button_B[0]

            # Limit the number of button B presses to 100
            if(nb_B_pressed>100):
                nb_B_pressed = 100
            
            # Initialize the number of times button A is pressed
            nb_A_pressed = 0

            # Initialize current coordinates based on button B presses
            current_x = nb_B_pressed*button_B[0]
            current_y = nb_B_pressed*button_B[1]

            # Iterate while button B presses are positive and button A presses are within limit
            while(nb_B_pressed>0 and nb_A_pressed<=100):

                # Check if current coordinates match the prize coordinates
                if(current_x==prize[0] and current_y==prize[1]):
                    # Update the final sum based on the number of button presses
                    final_sum += nb_A_pressed*3 + nb_B_pressed
                    break

                # Check if current coordinates exceed the prize coordinates
                elif(current_x>prize[0] or current_y>prize[1]):
                    # Decrease button B presses and update current coordinates
                    current_x -= button_B[0]
                    current_y -= button_B[1]
                    nb_B_pressed -=1
                
                # If current coordinates are less than prize coordinates, press button A
                else:
                    # Press button A and update current coordinates
                    nb_A_pressed +=1
                    current_x += button_A[0]
                    current_y += button_A[1]

        print(final_sum)
                