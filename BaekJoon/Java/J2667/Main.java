package J2667;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf =  new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb =  new StringBuilder();

    static StringTokenizer token;

    static int n, dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 }, graph[][];

    static boolean[][] visit;
    static ArrayList< Integer > parts = new ArrayList<>();



    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );
        graph = new int[ n ][ n ];
        visit = new boolean [ n ][ n ];
        for( int i = 0; i < n; i ++ ){
            String row = bf.readLine();

            for( int j = 0; j < n; j ++ ){

                if( '0' == row.charAt( j ) ){
                    graph[ i ][ j ] = 0;
                }else{
                    graph[ i ][ j ] = 1;
                }
            }

        }

        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < n; y ++ ){
                if( !visit[ x ][ y ] && graph[ x ][ y ] == 1 ){
                    visit[ x ][ y ] = true;
                    int cnt = dfs( x, y );
                    parts.add( cnt );
                }
            }
        }
        Collections.sort( parts );
        System.out.println( parts.size() );
        parts.stream().forEach( i -> {
            System.out.println( i );
        });



    }

    private static int dfs( int x, int y ) {

        int cnt = 0;
        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];
            if( nx >= 0 && nx < n && ny >= 0 && ny < n ){
;
                if( graph[ nx ][ ny ] == 1 && !visit[ nx ][ ny ] ){
                    visit[ nx ][ ny ] = true;
                    cnt += dfs( nx, ny );
                }
            }
        }

        return cnt + 1;

    }

}
