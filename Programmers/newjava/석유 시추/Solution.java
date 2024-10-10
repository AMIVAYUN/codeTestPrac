import java.util.*;
class Solution {
    int n, m;
    boolean[][] visited;
    int[] inside, land[];
    int[] dx = { 0, 0, -1, 1 }, dy = { -1, 1, 0, 0 };
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[ 0 ].length;
        inside = new int[ m ];
        visited = new boolean[ n ][ m ];
        this.land = land;
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( !visited[ i ][ j ] && land[ i ][ j ] == 1 ){
                    visited[ i ][ j ] = true;
                    bfs( i, j );
                }
            }
        }
        for( int i = 0; i < m; i ++ ){
            answer = Math.max( inside[ i ], answer );
        }
        return answer;
    }

    public void bfs( int sx, int sy ){
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ sx, sy } );
        HashSet<Integer> ys = new HashSet<>();
        ys.add( sy );
        int cnt = 1;
        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];


            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];
                if( isRight( nx, ny ) ){
                    if( !visited[ nx ][ ny ] && land[ nx ][ ny ] == 1 ){
                        visited[ nx ][ ny ] = true;
                        dq.add( new int[]{ nx, ny } );
                        cnt++;
                        ys.add( ny );
                    }
                }
            }
        }
        for( int y : ys ){
            inside[ y ] += cnt;
        }

    }

    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < m;
    }
}