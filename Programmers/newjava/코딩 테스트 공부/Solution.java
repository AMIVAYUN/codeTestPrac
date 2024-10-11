import java.util.*;
class Solution {

    public int mn = Integer.MAX_VALUE;
    private int[][] problems;
    private int n;
    private boolean[] visit;
    private int mx = 301;
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;

        /**
         알고력과 코딩력 필요

         100 depth는 너무 깊다.
         */

        this.problems = problems;
        this.n = problems.length;

        int[][] dp = new int[ 301 ][ 301 ];

        int mxa = 0, mxc = 0;
        for( int[] p: problems ){
            mxa = Math.max( mxa, p[ 0 ] );
            mxc = Math.max( mxc, p[ 1 ] );
        }

        if( mxa <= alp && mxc <= cop ){ return 0; }

        if( mxa <= alp ) alp = mxa;

        if( mxc <= cop ) cop = mxc;


        for( int i = 0; i < 301; i ++ ){
            Arrays.fill( dp[ i ], Integer.MAX_VALUE );
        }

        dp[ alp ][ cop ] = 0;



        for( int i = alp; i <= mxa; i ++ ){
            for( int j = cop; j <= mxc; j ++ ){

                dp[ i + 1 ][ j ] = Math.min( dp[ i + 1 ][ j ], dp[ i ][ j ] + 1 );
                dp[ i ][ j + 1 ] = Math.min( dp[ i ][ j + 1 ], dp[ i ][ j ] + 1 );

                for( int[] p: problems ){
                    int alreq = p[ 0 ];
                    int coreq = p[ 1 ];
                    int alrwd = p[ 2 ];
                    int corwd = p[ 3 ];
                    int cost = p[ 4 ];

                    if( i >= alreq && j >= coreq ){
                        int nexti = Math.min( mxa, i + alrwd );
                        int nextj = Math.min( mxc, j + corwd );

                        dp[ nexti ][ nextj ] = Math.min( dp[ nexti ][ nextj ], dp[ i ][ j ] + cost );
                    }

                }
            }
        }

        return dp[ mxa ][ mxc ];

    }



}