import java.util.*;
import java.io.*;
class Solution {
    /*

        각 지역 -> 유일한 번호로 구분
        두 지역 통과 소요 시간 고정1
        부대원은 최단 시간 부대 복귀가 목표

        주어진 source 순서대로 부대 복귀 최단 시간을 산출해서 반환할 것.

        그냥 destination으로 다잌스트라 돌리면 끝.

    */
    // int[][] graph;
    ArrayList<Integer>[] graph;
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = {};
        // graph = new int[ n + 1 ][ n + 1 ];
        // for( int i = 0; i < n + 1; i ++ ){
        //     Arrays.fill( graph[ i ], -1 );
        // }
        graph = new ArrayList[ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ) graph[ i ] = new ArrayList<>();

        for( int[] road: roads ){
            int x = road[ 0 ];
            int y = road[ 1 ];
            // graph[ x ][ y ] = 1;
            // graph[ y ][ x ] = 1;
            graph[ x ].add( y );
            graph[ y ].add( x );

        }
        int[] res = dijkstra( n, destination );

        answer = new int[ sources.length ];
        int idx = 0;
        for( int i : sources ){
            answer[ idx++ ] = res[ i ] != Integer.MAX_VALUE ? res[ i ] : -1;
        }
        return answer;
    }

    public int[] dijkstra( int n, int start ){
        int[] result = new int[ n + 1 ];
        Arrays.fill( result, Integer.MAX_VALUE );
        result[ start ] = 0;
        PriorityQueue< int[] > pq = new PriorityQueue<>( ( e1, e2 ) -> Integer.compare( e1[ 1 ], e2[ 1 ] ) );
        pq.add( new int[]{ start, 0 } );

        while( !pq.isEmpty() ){

            int[] pos = pq.poll();


            if( pos[ 1 ] > result[ pos[ 0 ] ] ){
                continue;
            }

            for( int i : graph[ pos[ 0 ] ] ){
                int cost = pos[ 1 ] + 1;
                if( result[ i ] > cost ){
                    result[ i ] = cost;
                    pq.add( new int[]{ i, cost } );
                }
            }

//             for( int i = 0; i < n + 1; i ++ ){
//                 if( i == pos[ 0 ] ) continue;
//                 if( graph[ pos[ 0 ] ][ i ] == -1 ) continue;
//                 int cost = pos[ 1 ] + 1;

//                 if( result[ i ] > cost ){
//                     result[ i ] = cost;
//                     pq.add( new int[]{ i, cost } );
//                 }

            // }
        }

        return result;
    }
}