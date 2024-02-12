package J2792;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int[] arr;

    static int Mx;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        int n = Integer.parseInt( token.nextToken( ));
        int m = Integer.parseInt( token.nextToken( ));
        arr = new int[ m ];
        for( int i = 0; i < m; i ++ ){
            arr[ i ] = Integer.parseInt( bf.readLine() );

        }

        int lt = 1; int rt = 1000000000;
        int ans = -1;
        while( lt <= rt ){
            int mid = ( (lt + rt) / 2 );
//            System.out.println( lt + " : " + rt );
//            System.out.println( mid + ": " + n );
            int cnt = 0;
            for( int i = 0; i < m; i ++ ){
                cnt += arr[ i ] % mid == 0 ? arr[ i ] / mid : arr[ i ] / mid + 1;
            }

            if( cnt > n ){

                lt = mid + 1;
            }else{
                ans = mid;
                rt = mid - 1;
            }

        }

        System.out.println( ans );

    }
}