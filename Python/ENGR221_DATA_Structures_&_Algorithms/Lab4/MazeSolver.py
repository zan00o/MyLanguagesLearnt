"""
/*/////////////////////////////////////////////
//   Title:     MazeSolver.py
//   Author:    Ryan L. 
//   Description: building the solver for a maze object
*//////////////////////////////////////////////
"""
from .SearchStructures import Stack, Queue
from .Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        # ~~~~~~~~
        # Write your tileIsVisitable() implementation here
        # ~~~~~~~~
        #checks if the tile is both not a wall and has not been visited before
        #print(self.maze.contents[row][col])
        if (row >= self.maze.num_rows or row < 0) or (col >= self.maze.num_cols or col < 0):
            return False
        if (self.maze.contents[row][col].isWall() == True):
            return False
        if (self.maze.contents[row][col].visited() == True):
            return False
        
        return True
        
        

    def solve(self):
        # ~~~~~~~~
        # Write your solve() implementation here
        # ~~~~~~~~
        self.ss.add(self.maze.start)
        while not self.ss.isEmpty():
            current = self.ss.remove()
            current.visit()
            if current == self.maze.goal:
                self.ss.add(current)
                return current
            
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Up, Down, Right, Left
            for i, j in reversed(directions):
                if self.tileIsVisitable(current.getRow() + i, current.getCol() + j):
                    next_tile = self.maze.contents[current.getRow() +i ][current.getCol() + j]
                    next_tile.setPrevious(current)
                    self.ss.add(next_tile)

        return None

     # Add any other helper functions you might want here
    
    def getPath(self):
        # ~~~~~~~~
        # Write your getPath() implementation here
        # ~~~~~~~~
        path = []
        g = self.maze.goal
        c = g.getPrevious()
        
        while c is not None and c != self.maze.start:
            path.append(c)
            c = c.getPrevious()

        path.append(self.maze.start)

        return path[::-1]


        

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    '''''
    for i in range(3):
        for j in range(3):
            print(i,j)
            print(solver.tileIsVisitable(i,j))
    print("-------------")
'''''
    print(solver.solve())
    # Print the solution found
    #solver.getPath()
    solver.printSolution()