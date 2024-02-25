package J12869;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int n;
    static int[][] pattern = {{ 9, 3, 1 }, { 9, 1, 3 }, { 3, 9, 1 }, { 3, 1, 9 }, { 1, 9, 3 }, { 1, 3, 9 } };
    static int[] scv;
    static int[][][] dp;
    static int Mn = Integer.MAX_VALUE;


    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        scv = new int[ 3 ];
        token = new StringTokenizer( bf.readLine() );
        for( int i = 0; i < n; i ++ ){
            scv[ i ] = stoi( token.nextToken() );
        }

        dp = new int[ 61 ][ 61 ][ 61 ];

        for( int i = 0; i < 61; i ++ ){
            for( int j = 0; j < 61; j ++ ){
                Arrays.fill( dp[ i ][ j ], Integer.MAX_VALUE );
            }
        }

        if( n == 1 ){
            System.out.println( scv[ 0 ] % 9 == 0 ? scv[ 0 ] / 9 : scv[ 0 ] / 9 + 1 );
            return;
        }

        dfs( scv, 0 );

        System.out.println( Mn );

    }
    public static void dfs( int[] scv, int depth ){

        int one = scv[ 0 ];
        int two = scv[ 1 ];
        int three = scv[ 2 ];

        if( Mn <= depth ){
            return;
        }

        if( dp[ one ][ two ][ three ] <= depth ){
            return;
        }

        dp[ one ][ two ][ three ] = depth;

        if( one == 0 && two == 0 && three == 0 ){
            Mn = Math.min( Mn, depth );
            return;
        }

        for( int i = 0; i < 6; i++ ){
            int nextOne = one - pattern[ i ][ 0 ]; nextOne = nextOne < 0 ? 0 : nextOne;
            int nextTwo = two - pattern[ i ][ 1 ]; nextTwo = nextTwo < 0 ? 0 : nextTwo;
            int nextThree = three - pattern[ i ][ 2 ]; nextThree = nextThree < 0 ? 0 : nextThree;

            dfs( new int[] { nextOne, nextTwo, nextThree }, depth + 1 );
        }

    }
    public static int stoi( String token ){
        return Integer.parseInt( token );
    }
}
