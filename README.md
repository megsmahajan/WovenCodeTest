# WovenCodeTest

We first take a string as an input from Command Line. The Sting needs to be in the form, "F2,L1,B2" and so on.
The robot starts moving in open space from point (0,0). To keep uniformity in the position of the robot, we change the row and column values w.r.t. a 2D matrix assuming it has negative indices.
We make the commands consitant and create one String with only characters. (eg. F1,L1,B2 -> FLBB)
This makes it easy to parse the single uniform string and perform direction changes.

Since there are 4 directions, as we turn left or right, we add 1 unit to the direction and mod it by 4 to get where the robot is facing to make decisions about either incrementing or decrementing row or column.

Output 1: We will get the final position of the Robot after following all the moving instructions.

Since we start with 0,0 there is a possibility that the robot will move into negative co-ordinates. However, the distance of this point from 0,0 will always be same as the distance of the absolute value of these co-ordinates from 0,0.

Therefore, we define a matrix including the abs. value of the end position of the robot and 0,0 and find the smallest distance from 0,0 to that point using BFS.

In BFS, all cells having shortest path as 1 are visited first, followed by their adjacent cells having shortest path as 1+1=2 and so on. In BFS, the first occurance of the destination cell gives us the result and we can stop our search.

How to run from Command Line:

Run the following command: python (Your local directory path)/WovenCodeTest/DistanceFromStart.py 

This command will ask you to enter Directions after successful execution.

Sample Input: String of the form: F1,R1,B2,L1,B3 

Sample Output: Final position:  (2, -2) 
               Shortest path from source to destination has length:  4

Test 1: Any other input other than this form will not execute the code further. (Nulls, other string formats, integers)

Test 2: Check if robot can turn more than once to left or right in one move.

Test 3: Check the smallest path if the robot is at the origin.

Test 4: Check if robot moves only in 4 directions and not diagonally.
