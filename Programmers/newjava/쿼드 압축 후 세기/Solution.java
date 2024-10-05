import java.util.*;
import java.io.*;
class Solution {
    int n, startSize;
    public int[] solution(int[][] arr) {
        int[] answer = {};
        n = arr.length;
        startSize = n;


        ArrayDeque< int[] > dq = new ArrayDeque<>();

        dq.add( new int[]{ 0, 0, startSize } );
        int cnt0 = 0, cnt1 = 0;

        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < n; j ++ ){
                if( arr[ i ][ j ] == 0 ) cnt0++;
                else cnt1++;
            }
        }

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            // System.out.println( Arrays.toString( now ) );

            int x = now [ 0 ];
            int y = now [ 1 ];
            int size = now [ 2 ];





            int stan = arr[ x ][ y ];
            boolean flag = false;
            for( int i = x; i < x + size; i ++ ){
                for( int j = y; j < y + size; j ++ ){
                    if( arr[ i ][ j ] != stan ){
                        if( size / 2 != 1 ){
                            dq.add( new int[]{ x, y, size / 2 } );
                            dq.add( new int[]{ x + size / 2, y, size / 2 } );
                            dq.add( new int[]{ x, y + size / 2 , size / 2 } );
                            dq.add( new int[]{ x + size / 2, y + size / 2, size / 2 } );
                        }
                        // System.out.println(" its matter " + stan + " " + size );

                        flag = true;
                        break;
                    }
                }
                if( flag ) break;
            }



            if( !flag ){

                cnt0 = stan == 0 ? cnt0 - ( size * size ) + 1 : cnt0;
                cnt1 = stan == 1 ? cnt1 - ( size * size ) + 1 : cnt1;

            }


        }
        answer = new int[]{ cnt0, cnt1 };

        return answer;
    }
}