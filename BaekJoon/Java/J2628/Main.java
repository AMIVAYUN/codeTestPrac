package J2628;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static StringBuilder sb;

    static int[][] graph ;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int n = Integer.parseInt(token.nextToken() ); int m = Integer.parseInt(token.nextToken() );
        int k = Integer.parseInt( bf.readLine() );

        ArrayList< Integer > rows = new ArrayList<>();
        ArrayList< Integer > cols = new ArrayList<>();

        rows.add( 0 ); rows.add( n );
        cols.add( 0 ); cols.add( m );


        for( int i = 0; i < k; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int c = Integer.parseInt(token.nextToken() );
            int node = Integer.parseInt(token.nextToken() );

            if( c == 1 ){
                rows.add( node );
            }else{
                cols.add( node );
            }
        }
        int Mx = 0;
        Collections.sort( rows );
        Collections.sort( cols );

        for( int i = 1; i < rows.size(); i ++ ){

            for( int j = 1; j < cols.size(); j ++ ){
                Mx = Math.max( Mx, (rows.get( i ) - rows.get( i - 1 )) * ( cols.get( j ) - cols.get( j - 1 ) ) );
            }
        }

        System.out.println( Mx );
    }
}