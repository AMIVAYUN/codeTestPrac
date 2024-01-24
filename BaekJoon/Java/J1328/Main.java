package J1328;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( br.readLine() );

        int n = stoi( token.nextToken() );
        int l = stoi( token.nextToken() );
        int r = stoi( token.nextToken() );

        long[][][] memo = new long[ 101 ][ 101 ][ 101 ];

        memo[ 1 ][ 1 ][ 1 ] = 1;

        memo[ 2 ][ 2 ][ 1 ] = 1;
        memo[ 2 ][ 1 ][ 2 ] = 1;

        long mod = 1000000007;

        for( int i = 3; i <= n; i ++ ){
            for( int j = 1; j <= l; j ++ ){
                for( int k = 1; k <= r; k ++){
                    memo[ i ][ j ][ k ] += memo[ i - 1 ][ j - 1 ][ k ] % mod;
                    memo[ i ][ j ][ k ] += memo[ i - 1 ][ j ][ k - 1 ] % mod;
                    memo[ i ][ j ][ k ] += ( memo[ i - 1 ][ j ][ k ] * ( i - 2 ) ) % mod;
                    memo[ i ][ j ][ k ] %= mod;
                }

            }
        }

        System.out.println( memo[ n ][ l ][ r ] );


    }

    static Integer stoi( String tk ){
        return Integer.parseInt( tk );
    }
}
