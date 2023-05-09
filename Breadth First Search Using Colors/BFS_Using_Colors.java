//Breadth First Search Using Colors
package com.mycompany.mavenproject2;

import java.util.*;

public class BFS_Using_Colors {

    public static void main(String[] args) {
        int[][] adjMatrix = {{0, 1, 1, 0, 1},
                            {1, 0, 1, 0, 1},
                            {1, 1, 0, 1, 0},
                            {0, 0, 1, 0, 1},
                            {1, 1, 0, 1, 0}};
        bfs(adjMatrix, 0);
    }

    public static void bfs(int[][] adjMatrix, int source) {
        int n = adjMatrix.length;
        String[] color = new String[n];
        int[] prev = new int[n];
        int[] d = new int[n];

        // initialize
        for (int i = 0; i < n; i++) {
            color[i] = "WHITE";
            prev[i] = -1;
            d[i] = Integer.MAX_VALUE;
        }

        Queue<Integer> q = new LinkedList<>();
        color[source] = "GREY";
        d[source] = 0;
        prev[source] = -1;
        q.add(source);

        while (!q.isEmpty()) {
            int u = q.poll();
            System.out.print(u + " ");
            for (int v = 0; v < n; v++) {
                if (adjMatrix[u][v] == 1 && color[v] == "WHITE") {
                    color[v] = "GREY";
                    d[v] = d[u] + 1;
                    prev[v] = u;
                    q.add(v);
                }
            }
            color[u] = "BLACK";
        }
    }
}

