from collections import deque
import random
n=int(input("Size of the grid: "))
ar=[]
o=int(input("number of obstacle: "))
while len(ar)<=o:
    a,b=random.choice(range(n)),random.choice(range(n))
    if (a,b) not in ar:
        ar+=[(a,b)]
graph = [[1]*n for _ in range(n)]  #a sample graph, copied from the manual
for i,j in ar:
    graph[i][j]=0
for i in range(n):
    print(graph[i])
sx=int(input("startx: "))
sy=int(input("starty: "))
gx=int(input("goalx: "))
gy=int(input("goaly: "))

start = (sx, sy)  # start point copied from the manual
goal = (gx, gy)   #gaol " " " "

def dfs(graph, start, goal):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # possible directions where the robot can go
    stack = [(start, [start])]  # storing the current position and path to reach that position
    visited = set()  # initialize a set to track visited positions

    while stack:  # while there are still nodes in the stack
        (x, y), path = stack.pop()  # pop the most recent element from the stack
        
        if (x, y) == goal:  # if the goal is found, return the path
            return path

        visited.add((x, y))  # mark the current position as visited

        for dx, dy in directions:  # traverse through all allowed directions
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and (nx, ny) not in visited:  # check if we can move to this position
                stack.append(((nx, ny), path + [(nx, ny)]))  # add the new position and updated path to the stack
                visited.add((nx, ny))  # mark the new position as visited

    return None  # if no path is found

def print_path(path):
    if path:  # if a path is found
        print("Path to goal:")
        print(" -> ".join(f"({x}, {y})" for x, y in path))  # print the path
        print(f"Number of moves required = {len(path) - 1}")  # print the number of moves (always length-1)
    else:  # if no path is found
        print("Goal cannot be reached from starting block")

path = dfs(graph, start, goal)  # call the dfs method
print_path(path)  # print the returned path
