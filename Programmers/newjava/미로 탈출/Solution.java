import java.util.*;
class Solution {
    int n,m;
    int sx,sy,ex,ey,rx,ry;
    int[][] graph;
    public int solution(String[] maps) {
        int answer = 0;
        n = maps.length;
        m = maps[ 0 ].length();

        graph = new int[ n ][ m ];
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                char c = maps[ i ].charAt( j );
                graph[ i ][ j ] = 1;

                if( c == 'S' ){

                    sx = i;
                    sy = j;

                }else if( c == 'L' ){

                    rx = i;
                    ry = j;

                }else if( c == 'E' ){
                    ex = i;
                    ey = j;

                }
                else if( c == 'X' ){
                    graph[ i ][ j ] = 0;
                }
            }
        }
        // System.out.println( sx + " " + sy + " " + rx + " " + ry + " " + ex + " " + ey + " " );
        int sr = bfs( sx, sy, rx, ry );
        int re = bfs( rx, ry, ex, ey );

        return sr != -1 && re != -1 ? sr + re : -1;
        // return bfs( sx, sy, rx, ry ) + bfs( rx, ry, ex, ey );
        // return answer;
    }
    int[] dx = { -1, 1, 0, 0 }, dy = { 0, 0, -1, 1 };
    public int bfs( int sx, int sy, int ex, int ey ){
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        dq.add( new int[]{ sx, sy, 0 } );
        boolean[][] visit = new boolean[ n ][ m ];
        visit[ sx ][ sy ] = true;

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];
            int cnt = now[ 2 ];

            if( x == ex && y == ey ){
                return cnt;
            }

            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];
                if( isRight( nx, ny ) ){
                    if( !visit[ nx ][ ny ] && graph[ nx ][ ny ] != 0 ){
                        visit[ nx ][ ny ] = true;
                        dq.add( new int[]{ nx, ny, cnt + 1 } );
                    }
                }
            }
        }
        return -1;
    }
    boolean isRight( int x, int y ){
        return x < n && x >= 0 && y < m && y >= 0;
    }
}