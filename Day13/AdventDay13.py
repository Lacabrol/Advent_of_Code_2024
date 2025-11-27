if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input13.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        final_sum = 0

        button_A, button_B, prize = [], [], []

        token_number = 0

        nb_A_pressed = 0
        nb_B_pressed = 0

        current_x = 0
        current_y = 0

        for i in range(0,len(lines),4):
            lines[i] = lines[i].replace('+',' ').replace(',',' ')
            button_A = [int(x) for x in lines[i].split() if x.isdigit()]
            print(button_A)
            lines[i+1] = lines[i+1].replace('+',' ').replace(',',' ')
            button_B = [int(x) for x in lines[i+1].split() if x.isdigit()]
            print(button_B)
            lines[i+2] = lines[i+2].replace('=',' ').replace(',',' ')
            prize = [int(x) for x in lines[i+2].split() if x.isdigit()]
            print(prize)
            nb_B_pressed = prize[0]//button_B[0]
            if(nb_B_pressed>100):
                nb_B_pressed = 100
            nb_A_pressed = 0

            current_x = nb_B_pressed*button_B[0]
            current_y = nb_B_pressed*button_B[1]
            print(f"Starting at position: ({current_x},{current_y}) with {nb_B_pressed} B pressed")

            while(nb_B_pressed>0 and nb_A_pressed<=100):
                print(f"Current position: ({current_x},{current_y}) with {nb_A_pressed} A pressed and {nb_B_pressed} B pressed")
                if(current_x==prize[0] and current_y==prize[1]):
                    final_sum += nb_A_pressed*3 + nb_B_pressed*1
                    break
                elif(current_x>prize[0] or current_y>prize[1]):
                    current_x -= button_B[0]
                    current_y -= button_B[1]
                    nb_B_pressed -=1
                else:
                    nb_A_pressed +=1
                    current_x += button_A[0]
                    current_y += button_A[1]

        print(final_sum)
                