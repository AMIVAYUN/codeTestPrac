package J2116;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] dices;

    static boolean[] visit;

    static int Mx = 0;
    static int n;
    public static void main(String[] args) throws IOException {

        n = Integer.parseInt( bf.readLine() );
        dices = new int[ n ][ 6 ];
        visit = new boolean[ n ];
        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );

            int a = Integer.parseInt(token.nextToken() );
            int b = Integer.parseInt(token.nextToken() );
            int c = Integer.parseInt(token.nextToken() );
            int d = Integer.parseInt(token.nextToken() );
            int e = Integer.parseInt(token.nextToken() );
            int f = Integer.parseInt(token.nextToken() );

            dices[ i ] = new int[]{ a, b, c, f, d, e };

        }

        for( int bottom = 0; bottom< 6; bottom ++ ){
            find( 0, dices[ 0 ][ bottom ], 0 );

        }

        System.out.println( Mx );

    }

    private static void find( int depth, int prevTop, int sum ) {
        if( depth == n ){
            Mx = Math.max( sum, Mx );
            return;
        }

        int bottom = 0;

        for( bottom = 0; bottom < 6; bottom ++ ){
            if( dices[ depth ][ bottom ] == prevTop ){
                break;
            }
        }
        int posMx = getMx( depth, bottom );
        int top = dices[ depth ][ ( bottom + 3 ) % 6 ];

        find( depth + 1, top, sum + posMx );






    }

    static int getMx( int depth, int bottom ){
        int localMx = 0;
        for( int i = 0; i < 6; i ++ ){
            if( i == bottom || ( i == ( bottom + 3 ) % 6 ) ){
                continue;
            }
            localMx = Math.max( localMx, dices[ depth ][ i ] );
        }
        return localMx;
    }
}