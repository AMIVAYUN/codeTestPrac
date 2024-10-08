import java.util.*;
class Solution {

    int answer = Integer.MAX_VALUE, n = 0;
    int numSize = 0;
    boolean[] visit, graph[];
    public int solution(int n, int[][] wires) {
        n = wires.length;

        for( int i = 0; i < n; i ++ ){
            numSize = Math.max( numSize, wires[ i ][ 0 ] );
            numSize = Math.max( numSize, wires[ i ][ 1 ] );
        }

        numSize += 1;

        visit = new boolean[ numSize ];
        graph = new boolean[ numSize ][ numSize ];
        for( int i = 0; i < n; i ++ ){
            int[] vert = wires[ i ];
            int a = vert[ 0 ]; int b = vert[ 1 ];
            graph[ a ][ b ] = true;
            graph[ b ][ a ] = true;
        }

        for( int cut = 0; cut < n; cut ++ ){
            visit = new boolean[ numSize ];
            int a = wires[ cut ][ 0 ]; int b = wires[ cut ][ 1 ];
            graph[ a ][ b ] = false; graph[ b ][ a ] = false;
            visit[ 1 ] = true;
            int amx = bfs( 1, numSize, visit );

            // System.out.println( cut + " " + amx + " numSize = " + numSize );

            int bmx = numSize - amx - 1;
            answer = Math.min( Math.abs( bmx - amx ), answer );
            graph[ a ][ b ] = true; graph[ b ][ a ] = true;

        }


        return answer;
    }

    public int bfs( int start, int mx, boolean[] visit ){
        ArrayDeque< Integer > dq = new ArrayDeque<>();
        dq.add( start );
        int cnt = 1;
        while( !dq.isEmpty() ){
            int pos = dq.poll();

            for( int i = 1; i < mx; i ++ ){
                if( !visit[ i ] && graph[ pos ][ i ] ){
                    visit[ i ] = true;
                    cnt++;
                    dq.add( i );
                }
            }

        }

        return cnt;
    }
}