package J11049;


import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
//    static String[][] patterns = { { "100", "1"}, { "01" } };

    static int[][] memo ;
    static int[][] matrix;

    public static void main( String[] args ) throws IOException {
        int n = Integer.parseInt( bf.readLine() );
        memo = new int[ n ][ n ];
        matrix = new int[ n ][ 2 ];

        for( int i= 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            matrix[ i ] = new int[]{ Integer.parseInt( token.nextToken() ),Integer.parseInt( token.nextToken() ) };
        }

        for( int cnt = 0; cnt < n - 1; cnt ++ ){
            for( int i = 0; i < n - 1 - cnt; i ++ ){
                int j = i + cnt + 1;
                memo[ i ][ j ] = Integer.MAX_VALUE;
                for( int k = i; k < j; k ++ ){
                    memo[ i ][ j ] = Math.min( memo[ i ][ j ], memo[i][k] + memo[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1] );
                }

            }
        }

        for( int i = 0; i < n; i ++ ) System.out.println(Arrays.toString( memo[ i ] ));

        System.out.println(memo[ 0 ][ n - 1 ] );

    }
}
