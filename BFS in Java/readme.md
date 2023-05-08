BFS in Java
Breadth first search in java using link list


Explanation:

We create a 2D array graph to represent the graph where graph[i][j] = 1 indicates that there is an edge between nodes i and j.
We initialize the source node source as 0 and call the bfs() function with graph and source as arguments.
In the bfs() function, we create a Queue to hold the nodes to be visited and a boolean array visited to keep track of the visited nodes. We mark the source node as visited and add it to the queue.
We then enter a while loop that continues until the queue is empty.
Inside the loop, we dequeue a node u from the front of the queue and print it to the console.
We then iterate over all the neighbors v of u and check if they are unvisited and there exists an edge between u and v.
If a neighbor v is unvisited, we mark it as visited, add it to the queue, and continue with the next neighbor.
If all the neighbors of u have been visited, we dequeue the next node from the queue and repeat the process until the queue is empty.
The output of this program will be the order in which the nodes are visited during the BFS traversal, starting from the source node.
