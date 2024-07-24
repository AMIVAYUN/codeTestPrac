package PM.합승택시요금;

import java.util.*;
import java.io.*;
class Solution {
    int n, s, a, b, graph[][];
    public int solution(int n, int s, int a, int b, int[][] fares) {
        /*
            택시비를 아낀다. -> 비슷한 경로의 어피치에게 합승 제안

            S가 시작점 A와 B가 도착지 -> 모두 귀가하는데 소요되는 예상 요금 정산

            1~n 지점

            방법은 크게 두가지로 나타낼 수 있다. -> 합승 O/X

            일단 다익스트라로 각 노드가 최소 거리를 알 필요는 있다.


        */
        this.n = n;
        this.s = s;
        this.a = a;
        this.b = b;
        this.graph = new int[ n + 1 ][ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ){
            Arrays.fill( graph[ i ], Integer.MAX_VALUE );
        }
        for( int[] fare: fares ){
            int sa = fare[ 0 ];
            int sb = fare[ 1 ];
            int c = fare[ 2 ];
            graph[ sa ][ sb ] = c;
            graph[ sb ][ sa ] = c;
        }

        int answer = 0;

        int startPoint[] = dijkstra( s );

        answer = startPoint[ a ] + startPoint[ b ];

        for( int i = 1; i < n + 1; i ++ ){
            if( i == s ) continue;
            int[] dists = dijkstra( i );
            answer = Math.min( answer, startPoint[ i ] + dists[ a ] + dists[ b ] );
        }

        return answer;
    }

    private int[] dijkstra( int start ){
        int[] dists = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );
        PriorityQueue< int[] > pq = new PriorityQueue<>( ( e1, e2 ) -> Integer.compare( e1[ 1 ], e2[ 1 ] ) );
        dists[ start ] = 0;
        pq.add( new int[]{ start, 0 } );
        while( !pq.isEmpty() ){
            int[] pos = pq.poll();
            int now = pos[ 0 ];
            int cost = pos[ 1 ];

            if( cost > dists[ now ] ){
                continue;
            }

            for( int i = 1; i < n + 1; i ++ ){
                int distCost = graph[ now ][ i ];
                if( distCost != Integer.MAX_VALUE ){
                    int nextCost = cost + graph[ now ][ i ];
                    if( nextCost < dists[ i ] ){
                        dists[ i ] = nextCost;
                        pq.add( new int[]{ i, nextCost } );
                    }
                }
            }
        }
        return dists;
    }
}