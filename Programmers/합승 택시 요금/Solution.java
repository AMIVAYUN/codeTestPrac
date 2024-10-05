import java.util.*;
import java.io.*;
class Solution {
    /**
     다잌스트라 그런데 한 큐에 다 곁들인
     */

    public int[][] graph;
    public int[][] dists;
    public int n;
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = 0;
        graph = new int[ n ][ n ];

        this.n = n;
        for( int[] fare: fares ){
            int x = fare[ 0 ] - 1;
            int y = fare[ 1 ] - 1;
            int fee = fare[ 2 ];

            graph[ x ][ y ] = fee;
            graph[ y ][ x ] = fee;
        }

        dijkstra();
        s --;
        a --;
        b --;
        answer = dists[ s ][ a ] + dists[ s ][ b ];
        for( int i = 0; i < n; i ++ ){
            if( i == s ) continue;
            answer = Math.min( answer, dists[ s ][ i ] + dists[ i ][ a ] + dists[ i ][ b ] );

        }

        return answer;
    }

    public void dijkstra(){

        dists = new int[ n ][ n ];

        PriorityQueue< int[] > pq = new PriorityQueue<>( ( e1, e2 ) -> {
            return Integer.compare( e1[ 1 ], e2[ 1 ] );
        });

        for( int i = 0; i < n; i ++ ){
            Arrays.fill( dists[ i ], Integer.MAX_VALUE );
            dists[ i ][ i ] = 0;
            int[] start = new int[]{ i, 0, i };
            pq.add( start );
        }


        while( !pq.isEmpty() ){
            int[] now = pq.poll();
            int pos = now[ 0 ];
            int cost = now[ 1 ];
            int origin = now[ 2 ];

            if( dists[ origin ][ pos ] < cost ) continue;

            for( int i = 0; i < n; i ++ ){
                if( graph[ pos ][ i ] == 0 ) continue;
                int nextCost = cost + graph[ pos ][ i ];
                if( nextCost < dists[ origin ][ i ] ){
                    dists[ origin ][ i ] = nextCost;
                    pq.add( new int[]{ i, nextCost, origin } );

                }
            }
        }

        // return dists;
    }
}