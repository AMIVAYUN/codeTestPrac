import java.util.*;
class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;

        ArrayDeque< int[] > del = new ArrayDeque<>();
        ArrayDeque< int[] > pic = new ArrayDeque<>();

        for( int i = n - 1; i >= 0; i -- ){
            int de = deliveries[ i ];
            int pi = pickups[ i ];
            if( de != 0 ){
                del.add( new int[]{ i + 1, deliveries[ i ] } );
            }
            if( pi != 0 ){
                pic.add( new int[]{ i + 1, pickups[ i ] } );
            }

        }

        while( !del.isEmpty() || !pic.isEmpty() ){
            int delCnt = 0, picCnt = 0;
            int distmx = 0;
            while( delCnt < cap && !del.isEmpty() ){
                int[] next = del.poll();
                if( delCnt + next[ 1 ] > cap ){
                    next[ 1 ] -= ( cap - delCnt );
                    delCnt = cap;
                    del.addFirst( next );
                }else{
                    delCnt += next[ 1 ];
                }
                distmx = Math.max( distmx, next[ 0 ] );
            }

            while( picCnt < cap && !pic.isEmpty() ){
                int[] next = pic.poll();
                if( picCnt + next[ 1 ] > cap ){
                    next[ 1 ] -= ( cap - picCnt );
                    picCnt = cap;
                    pic.addFirst( next );
                }else{
                    picCnt += next[ 1 ];
                }
                distmx = Math.max( distmx, next[ 0 ] );
            }

            answer += ( (long)distmx ) * 2;
        }
        return answer;
    }
}