package J2206;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n, m;

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    static int graph[][], visit[][][], dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 };

    static int Mn = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        m = Integer.parseInt( token.nextToken() );

        graph= new int[ n ][ m ];

        visit = new int[ n ][ m ][ 2 ];

        for( int i = 0; i < n; i ++ ){
            String row = bf.readLine();
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = row.charAt( j ) - '0';
                visit[ i ][ j ][ 0 ] = Integer.MAX_VALUE;
                visit[ i ][ j ][ 1 ] = Integer.MAX_VALUE;
            }
        }
        visit[ 0 ][ 0 ][ 0 ] = 1;

//        dfs( false, 1, 0, 0 ); // T.O
        bfs();
        int res = Math.min( visit[ n - 1 ][ m - 1 ][ 0 ], visit[ n - 1 ][ m - 1 ][ 1 ] );
        System.out.println( res != Integer.MAX_VALUE ? res : -1 );


//        for( int i = 0; i < n; i ++ ){
//            for( int j = 0; j < m; j ++ ){
//                System.out.print( "[ " + visit[ i ][ j ][ 0 ] + " " + visit[ i ][ j ][ 1 ] + " ]" );
//            }
//            System.out.println();
//        }

    }
    static class Pos{
        @Override
        public String toString() {
            return "Pos{" +
                    "x=" + x +
                    ", y=" + y +
                    ", cnt=" + cnt +
                    ", alreadyBroken=" + alreadyBroken +
                    '}';
        }

        int x,y,cnt;
        boolean alreadyBroken;

        public Pos(int x, int y, int cnt, boolean alreadyBroken) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.alreadyBroken = alreadyBroken;
        }
    }

    /*
    C.O
    6 6
000000
011111
011111
010100
010110
000110


     */
    static void bfs(){


        ArrayDeque< Pos > dq = new ArrayDeque<>();
        dq.add( new Pos( 0, 0, 1, false ) );

        while( !dq.isEmpty() ){

            Pos now = dq.poll();

            if( now.cnt > visit[ now.x ][ now.y ][ now.alreadyBroken ? 1 : 0 ] ){
                continue;
            }
//            System.out.println( now );
            for( int i = 0; i < 4; i ++ ){
                int nx = now.x + dx[ i ];
                int ny = now.y + dy[ i ];

                if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                    if( graph[ nx ][ ny ] == 0 ){
                        if( visit[ nx ][ ny ][ now.alreadyBroken ? 1 : 0 ] > now.cnt + 1 ){
                            visit[ nx ][ ny ][ now.alreadyBroken ? 1 : 0 ] = now.cnt + 1;
                            dq.add( new Pos( nx, ny, now.cnt + 1, now.alreadyBroken ) );
                        }
                    }else{
                        if( !now.alreadyBroken ){
                            if( visit[ nx ][ ny ][ 1 ] > now.cnt + 1 ){
                                visit[ nx ][ ny ][ 1 ] = now.cnt + 1;
                                dq.add( new Pos( nx, ny, now.cnt + 1, true ) );
                            }
                        }
                    }
                }
            }
        }

    }

    static void dfs( boolean alreadyBroken, int cnt, int x, int y ){

        if( x == n - 1 && y == m - 1 ){
            Mn = Math.min( cnt, Mn );
            return;
        }

        if( Mn < cnt ){
            return;
        }


        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];

            if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                if( graph[ nx ][ ny ] == 0 ){
                    if( visit[ nx ][ ny ][ 0 ] > cnt + 1 ){
                        visit[ nx ][ ny ][ 0 ] = cnt + 1;
                        dfs( alreadyBroken, cnt + 1, nx, ny );
                    }
                }else{

                    if( !alreadyBroken ){
                        if( visit[ nx ][ ny ][ 1 ] > cnt + 1 ){
                            visit[ nx ][ ny ][ 1 ] = cnt + 1;
                            dfs( true, cnt + 1, nx, ny );
                        }
                    }
                }
            }
        }


    }
}
