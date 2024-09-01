package J3079;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;



    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        int n = stoi( token.nextToken() );
        long m = stol( token.nextToken() );



        long[] arr = new long[ n ];
        long Mx = 0;
        for( int i = 0; i < n; i ++ ){
            arr[ i ] = stol( bf.readLine() );
        }
        long answer =  Long.MAX_VALUE;

        long lt = 0; long rt = Long.MAX_VALUE;

        while( lt <= rt ){
            long mid = ( lt + rt ) / 2;
            long sum = 0;
            for( int i = 0; i < n; i ++ ){
                if( sum >= m ) break;
                sum += mid / arr[ i ];

            }

//            System.out.println( mid + " " + sum + " " + m );

            if( sum >= m ){
                rt = mid - 1;
                answer = Math.min( answer, mid );
            }else{
                lt = mid + 1;
            }
        }

        System.out.println( answer );
    }
    public static long stol( String token ){
        return Long.parseLong( token );
    }

    public static int stoi( String token ){
        return Integer.parseInt( token );
    }
}