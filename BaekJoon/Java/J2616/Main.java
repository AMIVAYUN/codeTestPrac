package J2616;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    /**
     * @param args
     * @throws IOException
     *
     * 3대가 끌 수 있는 객차 수는 같다.
     *
     * 3대가 요점이고 연속적이라는 것
     * n * 3
     *
     * dp[ i ][ k ] 는 dp[ i - 1 ][ j ] + prefix[ k + 3 ] - prefix[ k ] ( 단 j < k )
     *
     */

    static int n, k, dp[][], prefix[];

    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        token = new StringTokenizer( bf.readLine() );
        prefix = new int[ n + 1 ];
        for( int i = 0; i < n; i ++ ){
            int j = stoi( token.nextToken() );
            if( i == 0 ){
                prefix[ i + 1 ] = j;
                continue;
            }
            prefix[ i + 1 ] = j + prefix[ i ];
        }

        k = stoi( bf.readLine() );
        dp = new int[ 4 ][ n + 1 ];
//        for( int i = k; i < n + 1; i ++ ){
//            dp[ 0 ][ i ] = prefix[ i ] - prefix[ i - k ];
//        }

//        for( int i = 1; i < 3; i ++ ){
//            for( int j = k; j < n + 1; j ++ ){
//                int base = prefix[ j ] - prefix[ j - k ];
//
//                for( int l = k; l <= j - k; l ++ ){
//                    dp[ i ][ j ] = Math.max( dp[ i - 1 ][ l ] + base, dp[ i ][ j ] );
//                }
//            }
////            System.out.println( Arrays.toString(dp[ i ] ) );
//        }

        for( int i = 1; i < 4; i ++ ){
            for( int j =  i * k; j < n + 1; j ++ ){
                int base = prefix[ j ] - prefix[ j - k ];
                dp[ i ][ j ] = Math.max( dp[ i ][ j - 1 ], dp[ i - 1 ][ j - k ] + base );

            }
//            System.out.println( Arrays.toString(dp[ i ] ) );
        }
//        int Mx = 0;
//        for( int i = 0; i < n+1; i ++){
//            Mx = Math.max( Mx, dp[ 2 ][ i ] );
//        }
//        System.out.println( Mx );

        System.out.println( dp[ 3 ][ n ] );
//        System.out.println( Arrays.toString( dp[ 2 ] ));
    }

    public static Integer stoi( String token ){
        return Integer.parseInt( token );
    }
}