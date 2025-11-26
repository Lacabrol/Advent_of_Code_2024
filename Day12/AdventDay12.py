import numpy as np

if __name__ == '__main__':
    with open("input12.txt") as f:

        array = np.array([list(line.strip()) for line in f.readlines()])

        # Initialize a visited array to keep track of visited positions
        visited = np.zeros_like(array, dtype=bool)

        # Initialize final score
        final_score, element, stack = 0, None, None
        region_size, perimeter = 0, 0
        neighbourx, neighboury = 0, 0

        # Iterate through each position in the array
        for y in range(array.shape[0]):
            for x in range(array.shape[1]):

                # If the position has not been visited
                if not(visited[y, x]):
                    # Get the element at the current position
                    element = array[y, x]
                    # Initialize stack for DFS
                    stack = [(x, y)]
                    region_size = 0
                    perimeter = 0

                    # Perform DFS to explore the region
                    while stack:
                        # Pop a position from the stack
                        x_stack, y_stack = stack.pop()

                        # If the position has not been visited
                        if not(visited[y_stack, x_stack]):
                            # Mark the position as visited
                            visited[y_stack, x_stack] = True
                            # Increment region size
                            region_size += 1

                            # Check all four neighboring positions
                            for delta_x, delta_y in [(1,0),(-1,0),(0,1),(0,-1)]:
                                neighbour_x, neighbour_y = x_stack+delta_x, y_stack+delta_y

                                # If the neighbor is out of bounds, increment perimeter
                                if not (0 <= neighbour_x < array.shape[1] and 0 <= neighbour_y < array.shape[0]):
                                    perimeter += 1

                                # If the neighbor is a different element, increment perimeter
                                elif array[neighbour_y, neighbour_x] != element:
                                    perimeter += 1     

                                # If the neighbor is the same element and not visited, add to stack
                                elif not visited[neighbour_y, neighbour_x]:
                                    stack.append((neighbour_x, neighbour_y))

                    # Update final score with the contribution from the current region
                    final_score += region_size * perimeter

        # Print the final score
        print(final_score)
