import java.util.*;
class Solution {
    /**
     목표: 최대한 안걸리는 선에서 많이 훔치기!

     결과는 A 도둑의 흔적의 최솟 값.

     완탐 pq까지 써봤지만 안뚫림 dp로 가보자.
     */

    int result[] = new int[ 2 ], info[][], n, m, l;
    boolean[] visit;
    int[][] dp;
    int mx = 121;
    public int solution(int[][] info, int n, int m) {
        int answer = mx;
        this.info = info;
        this.n = n;
        this.m = m;
        this.l = info.length;

        dp = new int[ l + 1 ][ m ];

        for( int i = 0; i <= l; i ++ ) Arrays.fill( dp[ i ], mx );


        dp[ 0 ][ 0 ] = 0;

        for ( int depth = 1; depth < l + 1; depth++ ){
            int A = info[ depth - 1 ][ 0 ];
            int B = info[ depth - 1 ][ 1 ];

            for ( int i = 0; i < m; i ++ ){
                dp[ depth ][ i ] = Math.min( dp[ depth ][ i ], dp[ depth - 1 ][ i ] + A );

                if( i + B < m ){
                    dp[ depth ][ i + B ] = Math.min( dp[ depth ][ i + B ], dp[ depth - 1 ][ i ] );
                }
            }
        }


        for( int i = 0; i < m; i ++ ){
            answer = Math.min( answer, dp[ l ][ i ] );
        }


        // this.visit = new boolean[ l ];
        // result[ 1 ] = -1;
        // Arrays.sort( info, (e1, e2 ) -> {
        //     if( e1[ 0 ] == e2[ 0 ] ){
        //         return Integer.compare( e1[ 1 ], e2[ 1 ] );
        //     }
        //     return Integer.compare( e2[ 0 ], e1[ 0 ] );
        // });
        //이러면 재귀호출 할 이유가 없지
        // dfs( 0, 0, 0, 0, l );

//         PriorityQueue< int[] > pq = new PriorityQueue<>( ( e1, e2 ) -> {

//             if( e1[ 0 ] == e2[ 0 ] ){
//                 return Integer.compare( e1[ 1 ], e2[ 1 ] );
//             }
//             return Integer.compare( e2[ 0 ], e1[ 0 ]);

//         });


//         pq.add( new int[]{ 0, 0, 0 } );

//         while( !pq.isEmpty() ){
//             int[] now = pq.poll();
//             int depth = now[ 0 ];
//             int aCount = now[ 1 ];
//             int bCount = now[ 2 ];

//             if( answer != -1 && answer < aCount ){
//                 continue;
//             }

//             if( depth == l ){
//                 if( answer == -1 || answer > aCount ){
//                     answer = aCount;
//                 }
//                 continue;
//             }

//             if( bCount + info[ depth ][ 1 ] < m ){
//                 pq.add( new int[]{ depth + 1, aCount, bCount + info[ depth ][ 1 ] } );
//             }

//             if( aCount + info[ depth ][ 0 ] < n ){
//                 pq.add( new int[]{ depth + 1, aCount + info[ depth ][ 0 ], bCount } );
//             }



//         }

        // System.out.println( Arrays.toString( result ) );
        return answer < mx && answer < n ? answer : -1 ;
    }



    public void dfs( int depth, int stealCount, int aCount, int bCount, int remain ){



        if( remain == 0 ){
            if( result[ 1 ] == -1 ){
                result[ 1 ] = aCount;
            }else if( aCount < result[ 1 ] ){
                result[ 1 ] = aCount;
            }
            return;
        }






        if( aCount + info[ depth ][ 0 ] < n ){

            dfs( depth + 1, stealCount + 1, aCount + info[ depth ][ 0 ], bCount, remain - 1 );

        }

        if( bCount + info[ depth ][ 1 ] < m ){

            dfs( depth + 1, stealCount + 1, aCount, bCount +  info[ depth ][ 1 ], remain - 1 );

        }


    }
}