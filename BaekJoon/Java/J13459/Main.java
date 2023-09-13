package J13459;



import java.io.*;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int n, m;
    static char[][] graph;
    static int[] r, b, e;
    static boolean flag = false;
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt(token.nextToken() ); m = Integer.parseInt( token.nextToken() );

        graph = new char[ n ][ m ];
        for( int i = 0; i < n; i ++ ){
            String row = bf.readLine();
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = row.charAt( j );

                if( graph[ i ][ j ] == 'R' ){
                    r = new int[]{ i, j };
                }else if( graph[ i ][ j ] == 'B' ){
                    b = new int[]{ i, j };
                }else if( graph[ i ][ j ] == 'O' ){
                    e = new int[]{ i, j };
                }
            }
        }



        dfs( 0 );
        System.out.println( flag ? 1 : 0 );





    }
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    private static void dfs( int depth ) {

        if( isEnd() ){
            if( isRightEnd() ){
                flag = true;
            }
            return;
        }
        if( depth == 10 ){
            return;
        }

        int r_x = r[ 0 ]; int r_y = r[ 1 ];
        int b_x = b[ 0 ]; int b_y = b[ 1 ];


        for( int i = 0; i < 4; i ++ ){
            if( flag ) return;
            int[] nextR = move( r_x, r_y , i);
            int[] nextB = move( b_x, b_y, i );
            if( nextR[ 0 ] == nextB[ 0 ] && nextR[ 1 ] == nextB[ 1 ] && graph[ nextR[ 0 ] ][ nextR[ 1 ] ] != 'O' ){
                if( nextR[ 2 ] > nextB[ 2 ] ){
                    r[ 0 ] = nextR[ 0 ] - dx[ i ]; r[ 1 ] = nextR[ 1 ] - dy[ i ];
                    b[ 0 ] = nextB[ 0 ]; b[ 1 ] = nextB[ 1 ];
                }else{
                    r[ 0 ] = nextR[ 0 ]; r[ 1 ] = nextR[ 1 ];
                    b[ 0 ] = nextB[ 0 ] - dx[ i ]; b[ 1 ] = nextR[ 1 ] - dy[ i ];
                }
            }else{
                r[ 0 ] = nextR[ 0 ]; r[ 1 ] = nextR[ 1 ];
                b[ 0 ] = nextB[ 0 ]; b[ 1 ] = nextB[ 1 ];

            }

            dfs( depth + 1 );
            r[ 0 ] = r_x;
            r[ 1 ] = r_y;
            b[ 0 ] = b_x;
            b[ 1 ] = b_y;

        }

    }

    static int[] move( int i, int j, int dir){
        int x = i; int y = j; int cnt = 0;
        while( graph[ x + dx[ dir ] ][ y + dy[ dir ] ] != '#' && graph[ x ][ y ] != 'O' ){
            x += dx[ dir ];
            y += dy[ dir ];
            cnt++;
        }

        return new int[] { x, y, cnt };
    }

    private static boolean isRightEnd() {
        return ( r[ 0 ] == e[ 0 ] && r[ 1 ] == e[ 1 ] ) && !( b[ 0 ] == e[ 0 ] && b[ 1 ] == e[ 1 ] );
    }

    private static boolean isEnd() {
        return ( r[ 0 ] == e[ 0 ] && r[ 1 ] == e[ 1 ] ) || ( b[ 0 ] == e[ 0 ] && b[ 1 ] == e[ 1 ] );
    }
}
