package PM.경주로_건설;

import java.util.*;

class Solution {
    public int[][][] visit;
    public int[][] graph;
    public int[] dx = { 0, 1, -1, 0 };
    public int[] dy = { 1, 0, 0, -1 };
    public void dfs( int N, int[] now, int cnt, int dir ){
        int x, y;
        x = now[ 0 ];
        y = now[ 1 ];

        for( int i = 0; i < 4 ; i++ ){
            int nextdir = ( dir + i ) % 4;

            int nx = x + dx[ nextdir ];
            int ny = y + dy[ nextdir ];



            int bias = 0;
            if( nextdir == dir ){
                bias = 100;
            }else{
                bias = 600;
            }

            if( 0 <= nx && nx < N && 0 <= ny && ny < N ){
                if( graph[ nx ][ ny ] == 0 ){
                    if( visit[ nx ][ ny ][ nextdir ] > cnt + bias ){
                        visit[ nx ][ ny ][ nextdir ] = cnt + bias;
                        int[] next = { nx, ny };
                        dfs( N, next, cnt + bias, nextdir );
                    }
                }
            }
        }
    }
    public int solution(int[][] board) {
        int answer = 0;
        int N = board[ 0 ].length;
        visit = new int[ N ][ N ][ 4 ];
        graph = board;

        for( int x = 0; x < N; x ++ ){
            for( int y = 0; y < N; y ++ ){
                if( x == y && x == 0 ){
                    continue;
                }
                Arrays.fill( visit[ x ][ y ], 700 * N * N );
            }
        }
        int[] start = { 0, 0 };

        dfs( N, start, 0, 0 );
        dfs( N, start, 0, 1 );
        return Arrays.stream( visit[ N - 1 ][ N - 1 ] ).max().getAsInt();
    }
}