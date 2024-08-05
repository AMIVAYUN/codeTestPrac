package PM.캠핑;

import java.util.*;
class Solution {
    /*
        n이 5천개

        x y는 전부 Int의 범위 내임

        쌍 전체 개수니깐 걍 구해보자
    */
    public int solution(int n, int[][] data) {
        int answer = 0;

        Arrays.sort( data, ( e1, e2 ) -> {
            if( e1[ 0 ] == e2[ 0 ] ){
                return Integer.compare( e1[ 1 ], e2[ 1 ] );
            }
            return Integer.compare( e1[ 0 ], e2[ 0 ] );
        });
        // for( int i = 0; i < n; i ++ ){
        //     System.out.print( Arrays.toString( data[ i ] ) + " ");
        // }
        // System.out.println();
        for( int i = 0; i < n; i ++ ){

            for( int j = i + 1; j < n; j ++ ){

                // x나 y가 0이 된다.
                if( data[ i ][ 0 ] == data[ j ][ 0 ] || data[ i ][ 1 ] == data[ j ][ 1 ] ){
                    continue;
                }

                boolean isInNothing = true;

                boolean isReverse = data[ i ][ 1 ] > data[ j ][ 1 ];

                for( int k = i + 1; k < n; k ++ ){
                    //우상단 좌하단
                    if( isReverse ){

                        if( data[ k ][ 0 ] > data[ i ][ 0 ] && data[ k ][ 0 ] < data[ j ][ 0 ] ){
                            if( data[ k ][ 1 ] < data[ i ][ 1 ] && data[ k ][ 1 ] > data[ j ][ 1 ] ){
                                isInNothing = false;
                                break;
                            }
                        }
                    }else{

                        if( data[ k ][ 0 ] > data[ i ][ 0 ] && data[ k ][ 0 ] < data[ j ][ 0 ] ){
                            if( data[ k ][ 1 ] > data[ i ][ 1 ] && data[ k ][ 1 ] < data[ j ][ 1 ] ){
                                isInNothing = false;
                                break;
                            }
                        }
                    }
                }
                if( isInNothing ) {
                    answer++;
                    // System.out.println( i + " , " + j );
                }
            }
        }

        return answer;
    }
}
