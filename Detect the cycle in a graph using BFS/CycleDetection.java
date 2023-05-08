import java.util.*;

public class CycleDetection{
    
    public boolean detectCycle(int start, int[][] adjMat) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] v = new boolean[adjMat.length];
        q.add(start);
        v[start] = true;
        while(!q.isEmpty()) {
            int CN = q.poll();
            for(int n = 0; n < adjMat.length; n++) {
                if(adjMat[CN][n] == 1) {
                    if(!v[n]) {
                        v[n] = true;
                        q.add(n);
                    } else if(n != 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    public static void main(String[] args) {
        int[][] adjMat = {   {0, 1, 0, 0},
                             {0, 0, 1, 0},
                             {0, 0, 0, 1},
                             {1, 0, 0, 0}};
        CycleDetection CD = new CycleDetection();
        boolean cycleExists = CD.detectCycle(0, adjMat);
        if(cycleExists) {
            System.out.println("Cycle detected!");
        } else {
            System.out.println("No cycle detected.");
        }
    }
}
