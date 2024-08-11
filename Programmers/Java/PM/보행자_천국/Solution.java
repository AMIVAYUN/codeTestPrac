package PM.보행자_천국;

import java.util.*;
class Solution {
    int MOD = 20170805;
    /**
     0 0 0      0 1 1
     0 0 0  ->  1 2 3
     0 0 0      1 3 6

     dp[ i ][ j ] = dp[ i - 1 ][ j ] + dp[ i ][ j - 1 ];

     요점은 2를 어떻게 처리하냐 인 것.


     **/

    int[][][] dp;
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;

        // 0은  i - 1 로 부터 1은 j - 1로 부터
        dp = new int[ m + 1 ][ n + 1 ][ 2 ]; // ArrayIndexOut 대비.

        int mod = 20170805;

        int top = 0, left = 1;

        for( int x = 0; x < m; x ++ ){
            if( cityMap[ x ][ 0 ] == 1 ) break;
            dp[ x ][ 0 ][ top ] = 1;
        }

        for( int y = 0; y < n; y ++ ){
            if( cityMap[ 0 ][ y ] == 1 ) break;
            dp[ 0 ][ y ][ left ] = 1;
        }


        for( int x = 1; x < m; x ++ ){
            for( int y = 1; y < n; y ++){
                if( cityMap[ x ][ y ] != 1 ){
                    int fromTop = dp[ x - 1 ][ y ][ top ];
                    if( cityMap[ x - 1 ][ y ] == 0 ){
                        fromTop = ( fromTop + dp[ x - 1 ][ y ][ left ] ) % mod;
                    }
                    int fromLeft = dp[ x ][ y - 1 ][ left ];
                    if( cityMap[ x ][ y - 1 ] == 0 ){
                        fromLeft = ( fromLeft + dp[ x ][ y - 1 ][ top ] ) % mod;
                    }
                    dp[ x ][ y ][ top ] = fromTop;
                    dp[ x ][ y ][ left ] = fromLeft;
                }
            }
        }

//         if( cityMap[ 0 ][ 1 ] != 1 ){
//             dp[ 0 ][ 1 ] = new int[]{ 0, 1 };
//         }
//         if( cityMap[ 1 ][ 0 ] != 1 ){
//             dp[ 1 ][ 0 ] = new int[]{ 1, 0 };
//         }

//         for( int x = 0; x < m; x ++ ){
//             for( int y = 0; y < n; y ++ ){


//                 if( ( x== 0 && y == 0)){
//                     continue;
//                 }

//                 // System.out.println( x + ", " + y );

//                 int sum = ( dp[ x ][ y ][ 0 ] + dp[ x ][ y ][ 1 ] ) % mod;
//                 int fromTop = dp[ x ][ y ][ 0 ] % mod;
//                 int fromLeft = dp[ x ][ y ][ 1 ] % mod;

//                 if( cityMap[ x ][ y ] == 0 ){
//                     dp[ x + 1 ][ y ][ 0 ] = ( dp[ x + 1 ][ y ][ 0 ] + sum ) % mod;
//                     dp[ x ][ y + 1 ][ 1 ] = ( dp[ x ][ y + 1 ][ 1 ] + sum ) % mod;
//                 }else if( cityMap[ x ][ y ] == 1 ){
//                     continue;
//                 }else{
//                     dp[ x + 1 ][ y ][ 0 ] = ( dp[ x + 1 ][ y ][ 0 ] + fromTop ) % mod;
//                     dp[ x ][ y + 1 ][ 1 ] = ( dp[ x ][ y + 1 ][ 1 ] + fromLeft ) % mod;
//                 }
//             }
//         }

        // for( int i = 0; i < m; i ++ ){
        //     for( int j = 0; j < n; j ++ ){
        //         System.out.print( Arrays.toString( dp[ i ][ j ] ) + ", " );
        //     }
        //     System.out.println();
        // }

        return ( (dp[ m - 1 ][ n - 1 ][ top ] + dp[ m - 1 ][ n - 1 ][ left ] ) % mod );
    }
}