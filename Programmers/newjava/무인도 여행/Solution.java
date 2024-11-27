import java.util.*;
class Solution {
    int[][] graph;
    boolean[][] visit;
    ArrayList< Integer> lst = new ArrayList<>();
    int n, m;
    public int[] solution(String[] maps) {
        n = maps.length;
        m = maps[ 0 ].length();
        graph = new int[ n ][ m ];
        visit = new boolean[ n ][ m ];

        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                char c = maps[ i ].charAt( j );
                if( c == 'X' ){
                    graph[ i ][ j ] = 0;
                }else{
                    graph[ i ][ j ] = c - '0';
                }

            }
        }

        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( !visit[ i ][ j ] && graph[ i ][ j ] > 0 ){
                    visit[ i ][ j ] = true;
                    int k = bfs( i, j );
                    lst.add( k );
                }
            }
        }

        if( lst.size() == 0 ){
            return new int[]{ -1 };
        }

        int[] answer = new int[ lst.size() ];
        for( int i = 0; i < lst.size(); i ++ ){
            answer[ i ] = lst.get( i );
        }

        Arrays.sort( answer );
        return answer;
    }

    int[] dx = { -1, 1, 0, 0 };
    int[] dy = { 0, 0, -1, 1 };
    public int bfs( int sx, int sy ){
        int sum = graph[ sx ][ sy ];
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ sx, sy } );

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ]; int y = now[ 1 ];
            for( int i = 0; i < 4; i++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( isRight( nx, ny ) ){
                    if( !visit[ nx ][ ny ] && graph[ nx ][ ny ] > 0 ){
                        sum += graph[ nx ][ ny ];
                        visit[ nx ][ ny ] = true;
                        dq.add( new int[]{ nx, ny } );
                    }

                }
            }

        }

        return sum;
    }

    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < m;
    }
}