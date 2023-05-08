/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.mavenproject2;

import java.util.*;

public class BFS {
    public static void main(String[] args) {
        int[][] graph = {{0, 1, 1, 0, 1},
                         {1, 0, 1, 0, 1},
                         {1, 1, 0, 1, 0},
                         {0, 0, 1, 0, 1},
                         {1, 1, 0, 1, 0}};
        int source = 0;
        bfs(graph, source);
    }
    
    public static void bfs(int[][] graph, int source) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[graph.length];
        visited[source] = true;
        queue.add(source);

        while (!queue.isEmpty()) {
            int u = queue.remove();
            System.out.print(u + " ");
            for (int v = 0; v < graph.length; v++) {
                if (graph[u][v] == 1 && !visited[v]) {
                    visited[v] = true;
                    queue.add(v);
                }
            }
        }
    }
}
