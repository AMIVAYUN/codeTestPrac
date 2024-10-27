import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;

        HashMap< Integer, Integer > map = new HashMap<>();

        for( int t : tangerine ){
            map.put( t, map.getOrDefault( t, 0 ) + 1 );
        }

        Iterator<Integer> keys = map.keySet().iterator();
        PriorityQueue< int[] > pq = new PriorityQueue<>( ( e1, e2 ) -> {
            return Integer.compare( e2[ 1 ], e1[ 1 ] );
        });


        while( keys.hasNext()){
            int key = keys.next();
            pq.add( new int[]{ key, map.get( key ) } );
        }

        int cnt = 0;

        while( cnt < k ){
            int[] now = pq.poll();
            // System.out.println( Arrays.toString( now ) );
            cnt += now[ 1 ];
            answer++;
        }

        return answer;
    }
}