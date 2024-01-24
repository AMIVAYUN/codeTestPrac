package J11049;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    static long Mn = Long.MAX_VALUE;

    static long[][] matrix;
    static long[][] memo;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt( bf.readLine() );
        memo = new long[ n ][ n ];
        matrix = new long[ n ][ 2 ];

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            matrix[ i ][ 0 ] = Long.parseLong( token.nextToken() );
            matrix[ i ][ 1 ] = Long.parseLong(token.nextToken() );

        }

        for( int i = 0; i < n - 1; i ++ ){
            memo[ i ][ i + 1 ] = matrix[ i ][ 0 ] * matrix[ i ][ 1 ] * matrix[ i + 1 ][ 1 ];
        }
    }






}
