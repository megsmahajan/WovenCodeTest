import re

def main():
    directions = input("Directions: ")
    each_position = directions.split(",")
    final_directions = ''
    for d in each_position:
        m = re.split('(\d+)', d)
        final_directions = final_directions + (m[0] * int(m[1]))

    #print(final_directions)

    N = 0
    E = 1
    S = 2
    W = 3

    dir = N
    x =0
    y =0

    # Traverse the path given for robot
    for move in final_directions:

        # Find current move

        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

        # If move is forward or backward, then change x or y according to the current direction
        else:  # if move == 'G'
            if dir == N and move == "F":
                y -= 1
            elif dir == N and move == "B":
                y+=1
            elif dir == E and move == "F":
                x += 1
            elif dir == E and move == "B":
                x-=1
            elif dir == S and move == "F":
                y += 1
            elif dir == S and move == "B":
                y-=1
            elif dir == W and move == "F":
                x -= 1
            elif dir == W and move == "B":
                x +=1

    print ("Final position: ", (x,y))


if __name__ == '__main__':
    main()