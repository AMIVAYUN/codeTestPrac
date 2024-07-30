package PM.GPS;

import java.util.*;
import java.io.*;
class Solution {
    /**

     이동 가능한 경로로 만드는 최소 오류 수정 횟수를 구하여라
     도로는 양방향

     n = 200인데 완전 탐색이 가능할까? ㄴㄴ 심지어 도로 갯수는 최대 만개이다.

     중요한 점 중 하나가 gps_log의 시작과 끝은 고정이라는 것
     일단 edge_list를 2차원 그래프로 나타내자

     탐색하면서 가지치는 걸론 시간 초과를 줄이지 못한다.

     dp로 접근해보자

     dp[ a ][ b ] = a depth에서 b 까지 가는데 gps_log 기준 최소 오류 수정 횟수라 가정.

     */
    int[][] graph;
    int answer = Integer.MAX_VALUE;
    int n, m, k, gps_log[];
    ArrayList<Integer>[] lst;
    boolean[] visited;

    int[][] dp;

    public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
        this.n = n;
        this.m = m;
        this.k = k;
        this.gps_log = gps_log;
        this.lst = new ArrayList[ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ) lst[ i ] = new ArrayList<>();
        visited = new boolean[ n + 1 ];
        graph = new int[ n + 1 ][ n + 1 ];
        for( int[] edge: edge_list ){
            graph[ edge[ 0 ] ][ edge[ 1 ] ] = 1;
            graph[ edge[ 1 ] ][ edge[ 0 ] ] = 1;
            lst[ edge[ 0 ] ].add( edge[ 1 ] );
            lst[ edge[ 1 ] ].add( edge[ 0 ] );
        }

        if( k == 2 ){
            if( graph[ gps_log[ 0 ] ][ gps_log[ 1 ] ] != 1 ) return -1;
            else return 0;
        }
        visited[ gps_log[ 0 ] ] = true;
        // dfs( 0, gps_log[ 0 ], 0 );

        dp = new int[ k ][ n + 1 ];

        for( int i = 0; i < k; i ++ ) Arrays.fill( dp[ i ], 10001 );

        dp[ 0 ][ gps_log[ 0 ] ] = 0;

        for( int depth = 1; depth < k; depth ++ ){
            for( int node = 1; node <= n; node ++ ){
                for( int canBe : lst[ node ] ){
                    if( node != gps_log[ depth ] ){
                        dp[ depth ][ node ] = Math.min(  dp[ depth - 1 ][ canBe ] + 1, dp[ depth ][ node ] );
                    }else{
                        dp[ depth ][ node ] = Math.min(  dp[ depth - 1 ][ canBe ], dp[ depth ][ node ] );
                    }

                }
            }
        }




        // if( answer == Integer.MAX_VALUE ) return -1;
        if( dp[ k - 1 ][ gps_log[ k - 1 ] ] == 10001 ) return -1;
        return dp[ k - 1 ][ gps_log[ k - 1 ] ];
    }

    public void dfs( int depth, int pos, int diffCnt ){
        // System.out.println( depth + " ::= " + pos + "diff = " + diffCnt );
        if( depth + 1 == k ){
            if( pos == gps_log[ k - 1 ] ){
                answer = Math.min( answer, diffCnt );
            }
            return;
        }

        if( diffCnt > answer ) return;

        for( int next: lst[ pos ] ){
            if( !visited[ next ] ){
                visited[ next ] = true;

                if( gps_log[ depth + 1 ] != next ){
                    dfs( depth + 1, next, diffCnt + 1 );
                }else{
                    dfs( depth + 1, next, diffCnt );
                }

                visited[ next ] = false;
            }

        }
    }
}