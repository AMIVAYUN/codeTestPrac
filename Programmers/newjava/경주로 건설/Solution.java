import java.util.*;
import java.io.*;
class Solution {
    /*

        엄 비웹훼스 디퓌?

    */
    int[][] board, dp[];
    int n;
    int[][] dx = new int[][]{ { -1, 1 }, { 0, 0 } };

    int[][] dy = new int[][]{ { 0, 0 }, { -1, 1 } };


    public int solution(int[][] board) {
        int answer = 0;

        this.board = board;
        this.n = board.length;
        dp = new int[ n ][ n ][ 2 ];
        ArrayDeque<int[]>dq = new ArrayDeque();
        dq.add( new int[]{ 0, 0, 0, 0 } );
        dq.add( new int[]{ 0, 0, 1, 0 } );
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < n; j ++ ){
                Arrays.fill( dp[ i ][ j ], Integer.MAX_VALUE );
            }
        }
        dp[ 0 ][ 0 ][ 0 ] = 0;
        dp[ 0 ][ 0 ][ 1 ] = 0;
        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];
            int dir = now[ 2 ];
            int cost = now[ 3 ];

            // System.out.println( Arrays.toString( now ) );

            if( x == n - 1 && y == n - 1 ){
                continue;
            }

            for( int nextDir = 0; nextDir < 2; nextDir++ ){

                for( int i = 0; i < 2; i ++ ){
                    int nx = x + dx[ nextDir ][ i ];
                    int ny = y + dy[ nextDir ][ i ];
                    if( isRight( nx, ny ) ){
                        int nextCost = dir == nextDir ? cost + 100 : cost + 600;
                        if( board[ nx ][ ny ] != 1 && dp[ nx ][ ny ][ nextDir ] > nextCost ){
                            dp[ nx ][ ny ][ nextDir ] = nextCost;
                            dq.add( new int[]{ nx, ny, nextDir, nextCost } );
                        }
                    }
                }

            }

        }
        // for( int i = 0; i < n; i ++ ){
        //     System.out.println( Arrays.toString( dp[ i ] ) );
        // }
        return Math.min ( dp[ n - 1 ][ n - 1 ][ 0 ], dp [ n - 1 ][ n - 1 ][ 1 ] );
    }


    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n ;
    }
}