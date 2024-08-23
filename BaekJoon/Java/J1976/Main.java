package J1976;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m;

    static int parents[];

    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        m = stoi( bf.readLine() );
        parents = new int[ n ];
        for( int i = 0 ; i < n; i ++ ){
            parents[ i ] = i;
        }

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );

            for( int j = 0; j < n; j ++ ){

                int k = stoi( token.nextToken() );
                if( k == 1 ) union( i, j );
            }
        }
        token = new StringTokenizer( bf.readLine() );
        int start = find( stoi( token.nextToken() ) - 1 );
        for( int i = 1 ; i < m; i ++ ){
            int value = find( stoi( token.nextToken() ) - 1 );
            if( start != value ){
                System.out.println("NO");
                return;
            }

        }
        System.out.println("YES");
        return;
    }

    private static void union(int i, int k) {
        int pi = find( i );
        int pk = find( k );

        if( pi > pk ){
            parents[ pi ] = pk;
        }else {
            parents[ pk ] = pi;
        }
    }

    private static int find(int i) {
        if( parents[ i ] != i ){
            parents[ i ] = find( parents[ i ] );
        }
        return parents[ i ];
    }

    public static int stoi( String t ){
        return Integer.parseInt( t );
    }
}