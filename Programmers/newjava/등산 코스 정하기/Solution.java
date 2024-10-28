import java.util.*;
class Solution {

    HashMap< Integer, HashMap<Integer, Integer >> map = new HashMap<>();
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = {};

        for( int i = 0; i <= n; i ++ ){
            map.put( i, new HashMap<>() );
        }

        for( int i = 0; i < paths.length; i ++ ){
            int a = paths[ i ][ 0 ];
            int b = paths[ i ][ 1 ];
            int c = paths[ i ][ 2 ];

            HashMap<Integer,Integer> target1 = map.get( a );
            HashMap<Integer,Integer> target2 = map.get( b );

            target1.put( b, c );
            target2.put( a, c );
        }


        dijkstra( n, gates, summits );
        answer = new int[ 2 ];
        answer[ 0 ] = Integer.MAX_VALUE; answer[ 1 ] = Integer.MAX_VALUE;
        // System.out.println( Arrays.toString( dists ) );
        Arrays.sort( summits );
        for( int top : summits ){
            if( dists[ top ] < answer[ 1 ] ){
                answer[ 0 ] = top;
                answer[ 1 ] = dists[ top ];
            }
        }


        return answer;
    }
    public int[] dists;
    public void dijkstra( int n, int[] gates, int[] summits ){
        boolean[] isTop = new boolean[ n + 1 ];
        for( int top : summits ) isTop[ top ] = true;
        dists = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );
        PriorityQueue< int[] > pq = new PriorityQueue<>( (e1, e2 ) -> {
            return Long.compare( e1[ 1 ], e2[ 1 ] );
        });
        for( int gate : gates ){
            pq.add( new int[]{ gate, 0});
            dists[ gate ] = 0;
        }

        while( !pq.isEmpty() ){
            int[] now = pq.poll();

            int idx = (int) now[ 0 ];
            int cost = now[ 1 ];

            if( dists[ idx ] < cost || isTop[ idx ]) continue;

            for( int next: map.get( idx ).keySet() ){
                int ncost = Math.max( map.get( idx ).get( next ), cost );

                if( dists[ next ] > ncost ){
                    dists[ next ] = ncost;
                    pq.add( new int[]{ next, ncost });
                }
            }
        }
        for( int gate : gates ){

            dists[ gate ] = Integer.MAX_VALUE;
        }
    }
}