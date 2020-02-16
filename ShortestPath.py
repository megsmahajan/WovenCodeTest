# Import dependencies.
import numpy
import queue
from Node import *
import sys

class ShortestPath:

    # Defining row and column moves based on directions. Ref array: (Up,Left,Down,Right)
    # Defining matrix with source and destination
    def __init__(self, dest_x, dest_y):
        self.row = numpy.array([-1, 0, 0, 1])  # Incrementing rows wrt to Ref Array
        self.column = numpy.array([0, -1, 1, 0])  # Incrementing columns wrt Ref Array
        self.M = dest_x + 1
        self.N = dest_y + 1

    # Check if the move is valid withing the bounds of the array and the node isn't visited before.
    def is_valid(self, visited, row, column):
        return (row >= 0) and (row < self.M) and (column >= 0) and column < self.N and not visited[row][column]

    def bfs(self, matrix, i, j, x, y):  # x and y are destination indices in the matrix.
        # Defining visited array as boolean array.
        # We change values associated with a particular position as visited= True,
        # when we try to find path from src to destination node.

        visited = numpy.zeros((self.M, self.N), dtype=bool)
        # Use queue to store adjacent nodes.We also need to retrieve 1st inserted element of the queue.
        q = queue.Queue()
        visited[i][j] = True
        q.put(Node(i, j, 0))
        min_dist = sys.maxsize

        # 1. Iterating through the queue, adding nodes to the queue in all 4 directions.
        # 2. Incrementing distance of adjacent node from source node.
        while not q.empty():
            node = q.get()

            # i and j are initial positions (in this case, 0,0)
            i = node.x
            j = node.y
            dist = node.dist

            if i == x and j == y:  # if source indices equal destination, we have reached the destination. Return dist.
                min_dist = dist
                break

            # Check for all 4 possible movements from current cell.
            # Insert in queue if the move is valid.
            for k in range(4):
                if self.is_valid(visited, (i + self.row[k]), (j + self.column[k])):
                    visited[i + self.row[k]][j + self.column[k]] = True
                    q.put(Node(i + self.row[k], j + self.column[k], dist + 1))

        if min_dist != sys.maxsize:
            print("Shortest path from source to destination has length: ", min_dist)

        else:
            print("Destination cant be reached.")

