package J18430;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main{
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    static int n, m, Mx;
    static int[][] graph;
    static int[][] temp;
    static int[][][] dxys = { { { -1, 0 }, { 0, 1 } }, { { 0, 1 }, { 1, 0 } }, { { 1, 0 }, { 0, -1 } }, { { 0, -1 }, { -1, 0 } } };
    static int idx = 0;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = stoi( token.nextToken() );
        m = stoi( token.nextToken() );

        graph = new int[ n ][ m ];
        temp = new int[ n ][ m ];

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer(bf.readLine());
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = stoi( token.nextToken() );
            }
        }

        visit = new boolean[ n ][ m ];

        dfs( 0, 0, 0 );


        System.out.println( Mx );

    }

    static void dfs( int x, int y, int cnt ){
//        System.out.println( x + " " + y );
//        print();
//        System.out.println("---------");
        Mx = Math.max( cnt, Mx );
        if( y == m ){
            return;
        }
        if( x == n ){
            if( y == m ){
                return;
            }
            dfs( 0, y + 1, cnt );
            return;
        }

        if( visit[ x ][ y ] ){
            dfs( x + 1, y, cnt );
            return;
        }

        for( int i = 0; i < 4; i ++ ){

            int[][] dxy = dxys[ i ];
            int nx1 = x + dxy[ 0 ][ 0 ];
            int ny1 = y + dxy[ 0 ][ 1 ];

            int nx2= x + dxy[ 1 ][ 0 ];
            int ny2 = y + dxy[ 1 ][ 1 ];

            if(isRight( nx1, ny1 ) && isRight( nx2, ny2 ) ){
                if( !visit[ nx1 ][ ny1 ] && !visit[ nx2 ][ ny2 ] ) {
                    temp[ nx1 ][ ny1 ] = idx;
                    temp[ nx2 ][ ny2 ] = idx;
                    temp[ x ][ y ] = idx;
                    idx ++;
                    visit[ x ][ y ] = true;
                    visit[nx1][ny1] = true;
                    visit[nx2][ny2] = true;
                    dfs( x + 1, y, cnt + graph[ nx1 ][ ny1 ] + graph[ nx2 ][ ny2 ] +( 2*graph[ x ][ y ] ) );
                    visit[nx1][ny1] = false;
                    visit[nx2][ny2] = false;
                    visit[ x ][ y ] = false;
                }




            }
        }
        dfs( x + 1, y, cnt );
    }

    static boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < m;
    }
    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    static void print(){
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                System.out.print( temp[ i ][ j ] + " ");
            }
            System.out.println();
        }
    }
}
