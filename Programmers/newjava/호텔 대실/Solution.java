import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        ArrayList< int[] > lst = new ArrayList<>();

        for( String[] bt : book_time ){
            lst.add( new int[]{ getTime( bt[ 0 ] ), getTime( bt[ 1 ] ) } );
        }

        Collections.sort( lst, ( e1, e2 ) -> {
            if( e1[ 0 ] == e2[ 0 ] ){
                return Integer.compare( e1[ 1 ], e2[ 1 ] );
            }
            return Integer.compare( e1[ 0 ], e2[ 0 ] );
        });

        PriorityQueue< Integer > pq = new PriorityQueue<>();

        int n = book_time.length;

        for( int[] bt : lst ){
            int startTime = bt[ 0 ];
            int endTime = bt[ 1 ];

            if( !pq.isEmpty() && pq.peek() <= startTime ){
                pq.poll();
                pq.add( endTime + 10 );
            }else{
                pq.add( endTime + 10 );
            }
        }


        return pq.size();
    }

    public int getTime( String time ){
        String[] ss = time.split(":");
        return Integer.parseInt( ss[ 0 ] ) * 60 + Integer.parseInt( ss[ 1 ] );
    }
}