# Import packages
import re
from ShortestPath import *
import numpy as np

def find_smallest_dist(final_directions):
    # Defining directions for the robot.
    N = 0
    E = 1
    S = 2
    W = 3

    # Initially, the robot will be facing North.
    dir = N

    # Defining starting position as 0,0.
    x = 0
    y = 0

    # Traverse the path given for robot
    for move in final_directions:

        # Find current move

        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

        # If move is forward or backward, then change x or y according to the current direction
        # Final stopping position of the robot is in a 2D Matrix and not in the co-ordinate system.
        else:
            if dir == N and move == "F":
                x -= 1
            elif dir == N and move == "B":
                x += 1
            elif dir == E and move == "F":
                y += 1
            elif dir == E and move == "B":
                y -= 1
            elif dir == S and move == "F":
                x += 1
            elif dir == S and move == "B":
                x -= 1
            elif dir == W and move == "F":
                y -= 1
            elif dir == W and move == "B":
                y += 1

    print("Final position: ", (x, y))

    # The final stopping position of the robot can be in negative space as the robot is moving freely in a 2D space.
    # But, the distance from the origin of any particular point in negative space is same as the absolute distance.

    # Passing absolute values of x,y co-ordinates to find the shortest path from the origin.
    ShortestPath(abs(x), abs(y)).bfs(np.zeros((abs(x) + 1, abs(y) + 1)), 0, 0, abs(x), abs(y))



def main():

    # Input from command line for a string of directions.
    directions = str(input("Directions: "))

    # Check if input is in the correct form. If yes, proceed with parsing the instructions
    # and finding the shortest path. If not, ask for correct input from the user.

    if re.search('[FRBL]\d+', directions):
        each_position = directions.split(",")
        final_directions = ''

        for d in each_position:
            m = re.split('(\d+)', d)
            final_directions = final_directions + (m[0] * int(m[1]))

        find_smallest_dist(final_directions)

    else:
        print("Please input in the form F1,B1...")

if __name__ == '__main__':
    main()