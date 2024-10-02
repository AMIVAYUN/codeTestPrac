import java.util.*;
import java.io.*;
class Solution {
    public int n;
    public boolean[][][] visited;

    public int[] dx = new int[]{ 0, 0, -1, 1 };
    public int[] dy = new int[]{ 1, -1, 0, 0 };

    /*

        사방 + 회전 4방

    */

    public int[][] rdx = new int[][]{ { 0, 0, -1, -1 }, { 0, 1, 0, 1 } };
    public int[][] rdy = new int[][]{ { 0, 1, 1, 0 }, { 0, 0, -1, -1 } };



    public int[][][] checkPos = new int[][][]{ { { 1, 1 }, { 1, 0 }, { -1, 0 }, { -1, 1 } }, { { 1,1 }, { 0, 1 }, { 1, -1 }, { 0, -1 } } };

    public int solution(int[][] board) {
        int answer = 0;
        this.n = board.length;
        visited = new boolean[ n ][ n ][ 2 ];

        visited[ 0 ][ 0 ][ 0 ] = true;
        int[] robot = new int[]{ 0, 0, 0, 0 };

        ArrayDeque<int[]> dq = new ArrayDeque<>();
        dq.add( robot );

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];
            int dir = now[ 2 ];
            int cnt = now[ 3 ];

            if( x == n - 1 && y == n - 1 ){
                System.out.println( Arrays.toString( now ) );
                answer = cnt;
                break;
            }

            if( ( ( dir == 0 ? x : x + 1 ) == n - 1 ) && (  ( dir == 0 ? y + 1 : y ) == n - 1 ) ){
                // System.out.println( "ans = " +  Arrays.toString( now ) );
                // for( int i = 0; i < n; i ++ ){
                //     for( int j = 0; j < n; j ++ ){
                //         System.out.print( Arrays.toString( visited[ i ][ j ] ) + " ");
                //     }
                //     System.out.println();
                // }
                answer = cnt;
                break;
            }

            for( int i = 0; i < 4 ; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                int nx2 = dir == 0 ? nx : nx + 1;
                int ny2 = dir == 0 ? ny + 1 : ny;

                if( isRight( nx, ny ) && isRight( nx2, ny2 ) ){
                    if( !visited[ nx ][ ny ][ dir ] && board[ nx ][ ny ] != 1 && board[ nx2 ][ ny2 ] != 1 ){
                        // System.out.println(" next = " + nx + ", " + ny + ", dir = " + dir  + " cnt = " + ( cnt  + 1 ) );
                        visited[ nx ][ ny ][ dir ] = true;
                        dq.add( new int[]{ nx, ny, dir, cnt + 1 } );
                    }
                }
            }

            for( int i = 0; i < 4; i ++ ){
                int nextDir = dir ^ 1;
                int nx = x + rdx[ dir ][ i ];
                int ny = y + rdy[ dir ][ i ];

                int nx2 = nextDir == 0 ? nx : nx + 1;
                int ny2 = nextDir == 0 ? ny + 1 : ny;

                int wallx = x + checkPos[ dir ][ i ][ 0 ];
                int wally = y + checkPos[ dir ][ i ][ 1 ];

                if( isRight( nx, ny ) && isRight( nx2, ny2 ) && isRight( wallx, wally ) ){
                    if( !visited[ nx ][ ny ][ nextDir ] && board[ nx ][ ny ] != 1 && board[ nx2 ][ ny2 ] != 1 && board[ wallx ][ wally ] != 1 ){

                        // System.out.println(" next = " + nx + ", " + ny + ", dir = " + nextDir  + " cnt = " + ( cnt + 1 ) );
                        visited[ nx ][ ny ][ nextDir ] = true;
                        dq.add( new int[]{ nx, ny, nextDir, cnt + 1 } );
                    }
                }
            }

        }


        return answer;
    }

    private boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}