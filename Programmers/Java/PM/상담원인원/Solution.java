package PM.상담원인원;

import java.util.*;
import java.io.*;
class Solution {
    //그리디 아니면 완탐일텐데 일단 완탐 가보자
    int n, k;
    ArrayList<int[]>[] procReq;
    int answer = Integer.MAX_VALUE;
    public int solution(int k, int n, int[][] reqs) {

        this.k = k;
        this.n = n;
        this.procReq = new ArrayList[ k ];
        for( int i = 0; i < k; i ++){
            this.procReq[ i ] = new ArrayList<int[]>();
        }

        for( int[] req: reqs ){
            this.procReq[ req[ 2 ] - 1 ].add( req );
        }

        getNumCombination( 0, n, new int[ k ] );
        return answer;
    }

    public void getNumCombination( int depth, int remain, int[] arr ){
        if( depth == k ){
            getMinReadyTime( arr );
            return;
        }
        if( depth == k - 1 && remain != 0 ){
            arr[ depth ] = remain;
            getNumCombination( depth + 1, 0, arr );
            return;
        }
        for( int i = 1; i <= remain; i ++ ){
            arr[ depth ] = i;
            getNumCombination( depth + 1, remain - i, arr );
        }
    }

    public void getMinReadyTime( int[] arr ){
        int remainTime = 0;

        for( int i = 0; i < k; i ++ ){
            PriorityQueue< int[] > pq = new PriorityQueue<>( ( p1, p2 ) -> Integer.compare( p1[ 0 ] + p1[ 1 ], p2[ 0 ] + p2[ 1 ] ) );

            if( procReq[ i ].size() <= arr[ i ] ) continue;


            for( int j = 0; j < arr[ i ]; j++ ){
                pq.add( procReq[ i ].get( j ) );
            }
            int start = arr[ i ];

            for( int f = start; f < procReq[ i ].size(); f ++ ){

                int[] target = pq.poll();

                if( target[ 0 ] + target[ 1 ] <= procReq[ i ].get( f )[ 0 ] ){
                    pq.add( procReq[ i ].get( f ) );
                }else{
                    remainTime += target[ 1 ] + target[ 0 ] - procReq[ i ].get( f )[ 0 ];
                    int[] next = new int[ 3 ];
                    next[ 0 ] = target[ 0 ] + target[ 1 ];
                    next[ 1 ] = procReq[ i ].get( f )[ 1 ];
                    next[ 2 ] = i;
                    pq.add( next );
                }

                // System.out.println( "inner:: " + f + ", " + remainTime );
            }

        }

        // System.out.println( Arrays.toString( arr ) + " : " + remainTime );

        answer = Math.min( answer, remainTime );


    }
}