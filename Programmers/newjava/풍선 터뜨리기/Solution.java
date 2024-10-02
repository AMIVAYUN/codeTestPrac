import java.io.*;
import java.util.*;

class Solution {
    /*

    죽는 놈-> 내 양쪽 최소가 나보다 작으면 나는 그냥 죽었다.

    연산의 간단화 n ** 2 말고 좌로 prefix 우로 prefix 구하면 되지 않을까?
    */
    public int solution(int[] a) {
        int answer = 0;
        int n = a.length;
        int[] lprefix = new int[ n ]; int[] rprefix = new int[ n ];

        lprefix[ 0 ] = a[ 0 ];
        rprefix[ n - 1 ] = a[ n - 1 ];

        for( int i = 1; i < n; i ++ ){
            lprefix[ i ] = Math.min( lprefix[ i - 1 ], a[ i ] );
            rprefix[ n - i - 1 ] = Math.min( rprefix[ n - i ], a[ n - i - 1 ] );
        }


        answer = 2;

        for( int i = 1; i < n - 1; i ++ ){
            if( lprefix[ i - 1 ] < a[ i ] && rprefix[ i + 1 ] < a[ i ] ){
                continue;
            }
            answer++;
        }

        return answer;
    }
}