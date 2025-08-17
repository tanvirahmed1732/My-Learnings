def iddfs(graph, start, goal):

    for depth in range(len(graph)): #increase depth limits 1 by 1
        visited = set()
        stack = [(start, 0)]  # (start node, depth), here assuming the depth is 0 where we starting from.
        path = []  # Keep track of visited nodes

        while stack: #while stack is nor empty
            node, cdepth = stack.pop() 

            if cdepth > depth:
                continue  # Skip if the node is deeper than the depth limit

            if node == goal:
                path.append(node)
                return depth, path  # Return as soon as goal is found

            if node not in visited: #if the node is new to visit
                visited.add(node)
                path.append(node)  #store the visiting order.

                # Add neighbors to the stack with depth+1
                for n in range(len(graph)):
                    if graph[node][n] == 1 and n not in visited:
                        stack.append((n, cdepth + 1))

    return None, [] #if there is no goal found after visiting all depth and all of the nodes

def read_graph(path):
    with open(path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

# start
path = r"d:\Code\GitHub\Practice\Python Practice\Lab Reports\CSE-316 AI Lab\Lab 4\graph.txt"
start = int(input("Enter the start node (integer): "))
goal = int(input("Enter the goal node (integer): "))

# Read graph and run IDDFS
graph = read_graph(path)
level, order = iddfs(graph, start, goal)

if level is not None:
    print(f"Goal found at level {level}.")
    print("Order of nodes visited:", order)
else:
    print("Goal not found.")

"""     0
       / \
      1   2
     / \   \
    3   4   5
           /
          6
"""