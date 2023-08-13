package J1654;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer token;
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static long lines[];
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int K = Integer.parseInt( token.nextToken() );
        int N = Integer.parseInt( token.nextToken() );

        lines = new long[ K ];
        long Mx = 0;
        for( int i = 0; i < K; i ++ ){
            lines[ i ] = Integer.parseInt( bf.readLine() );
            Mx = Math.max( lines[ i ], Mx );

        }
        if( N == 1 ){
            System.out.println( lines[ 0 ] );
            return;
        }

        long lt = 1; long rt = Mx + 1;
        long ans = -1;
        while( lt <= rt ){
            long mid = ( lt + rt ) / 2;

            if( getSum( mid ) >= N ){
                lt = mid + 1;
                ans = Math.max( mid, ans );
            }else{
                rt = mid - 1;
            }


        }
        System.out.println( ans );



    }

    static int getSum( long target ){
        int sum = 0;

        for( long i : lines ){
            sum += ( i ) / target;
        }

        return sum;
    }
}
