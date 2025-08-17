from collections import deque

# Define the 2D graph (grid)
graph = [
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1]
]


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #possible moves, collect from manual

rows, cols = len(graph), len(graph[0])
topological_order = []
visited = set()

def dfs(start_x, start_y):
    stack = [(start_x, start_y)]  # Stack for DFS
    while stack: #while stack is not empty
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))  
            topological_order.append((x, y))  

            for dx, dy in directions:
                nx, ny = x + dx, y + dy #check all direction
                if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 1 and (nx, ny) not in visited: #if valid square/node
                    stack.append((nx, ny)) #stack for future travarse

# Call DFS from all traversable nodes
for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 1 and (i, j) not in visited:
            dfs(i, j)

topological_order.reverse()# Reverse to get correct topological order

print("Topological Order of Node Traversal:")
print(" -> ".join(f"({x}, {y})" for x, y in topological_order))
