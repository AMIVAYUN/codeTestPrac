package PM;

import java.util.*;
class Solution {
    public static int[][] graph = new int[ 101 ][ 101 ];
    public static int[][] visit = new int[ 101 ][ 101 ];
    public static int[] dx = { 0, 0, -1, 1 };
    public static int[] dy = { 1, -1, 0, 0 };
    public void getRect( int x1,int y1,int x2,int y2 ){
        int[] xs = new int[ x2 - x1 + 1 ];
        int[] ys = new int[ y2 - y1 + 1];

        for( int i = x1; i < x2 + 1; i++ ){
            xs[ i - x1 ] = i;
        }

        for( int i = y1; i < y2 + 1; i++ ){
            ys[ i - y1 ] = i;
        }

        // x_cor , ys & xs , y_cor

        for( int i = x1; i < x2 + 1; i++ ){
            if( graph[ i ][ y1 ] != 2 ){
                graph[ i ][ y1 ] = 1;
            }
            if( graph[ i ][ y2 ] != 2 ){
                graph[ i ][ y2 ] = 1;
            }

        }

        for( int i = y1; i < y2 + 1; i ++ ){
            if( graph[ x1 ][ i ] != 2 ){
                graph[ x1 ][ i ] = 1;
            }
            if( graph[ x2 ][ i ] != 2 ){
                graph[ x2 ][ i ] = 1;
            }


        }

        for( int x = x1 + 1; x < x2; x++ ){
            for( int y = y1 + 1; y < y2; y++ ){
                graph[ x ][ y ] = 2;
            }
        }


    }
    public int bfs( int[]start, int[]end ){
        int answer = 10001;
        Queue< int[] > q = new LinkedList<>();
        int[] context = { 0, start[ 0 ], start[ 1 ] };

        q.add( context );
        visit[ start[ 0 ] ][ start[ 1 ] ] = 0;
        while( !q.isEmpty() ){
            int[] now = q.remove();
            int cnt, x, y;
            cnt = now[ 0 ];
            x = now[ 1 ];
            y = now[ 2 ];
            if( visit[ x ][ y ] < cnt ){
                continue;
            }

            if( x == end[ 0 ] && y == end[ 1 ] ){
                answer = Math.min( answer, cnt );
                continue;
            }

            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( 0<= nx && nx < 101 && 0<= ny && ny < 101 ){
                    if( visit[ nx ][ ny ] > cnt + 1 && graph[ nx ][ ny ] == 1 ){
                        int[] newcontext = { cnt + 1, nx, ny };
                        q.add( newcontext );
                        visit[ nx ][ ny ] = cnt + 1;
                    }
                }

            }



        }
        return answer / 2;

    }
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;

        for( int i = 0; i < 101; i ++ ){
            for( int j = 0; j < 101; j ++ ){
                visit[ i ][ j ] = 10102;
            }
        }

        characterX *= 2; characterY *= 2; itemX *= 2; itemY *= 2;

        for( int[] rect : rectangle ){
            int x1 = rect[ 0 ];
            int y1 = rect[ 1 ];
            int x2 = rect[ 2 ];
            int y2 = rect[ 3 ];

            x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2;

            getRect( x1, y1, x2, y2 );
        }

        int[] start = {  characterX,  characterY };
        int[] end = { itemX, itemY };

        return bfs( start, end );

    }
}