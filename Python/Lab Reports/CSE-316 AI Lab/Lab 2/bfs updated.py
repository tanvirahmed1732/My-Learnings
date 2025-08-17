from collections import deque


graph = [
    [0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1]
] #a sample graph, copied from the manual

start = (0, 1) #start point copied from the manual
goal = (4, 4) #gaol " " " "

def bfs(graph, start, goal):
    directions = [(0, -1),(1, 0), (-1, 0), (0, 1)] #possible directions where the robot can go
    queue = deque([(start, [start])]) #storing the visited square and path to reach to that square/position
    visited = set() #initialize a set

    while queue: #while the que is not empty
        (x, y), path = queue.popleft() #retreive elements form the Q
        
        if (x, y) == goal: #if the gaol is found just return the path that we need to print.
            return path

        visited.add((x, y)) #if the square is not the goal 

        for dx, dy in directions: #traverst through all allowed direction
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and (nx, ny) not in visited: #check is it possible to go that direction
                queue.append(((nx, ny), path + [(nx, ny)])) #append to the Q with the path.
                visited.add((nx, ny)) #mark as visited the new square/child square

    return None #if there is no goal found

def print_path(path):
    if path: #if path is not none
        print("Path to goal:")
        print(" -> ".join(f"({x}, {y})" for x, y in path)) #print the path
        print(f"Number of moves required = {len(path) - 1}") #print the number of moves. it always less than 1 from the length
    else: #if path is none
        print("Goal cannot be reached from starting block")


path = bfs(graph, start, goal) #call the bfs method
print_path(path) #print the returned path.