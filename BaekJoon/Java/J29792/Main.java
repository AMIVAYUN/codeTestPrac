package J29792;


import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;


    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());
        int k = Integer.parseInt(token.nextToken());

        long[] characters = new long[ n ];

        for( int i = 0; i < n;  i ++ ){

            characters[ i ] = Long.parseLong( bf.readLine() );
        }
        int[] result = new int[ n ];
        Arrays.sort( characters );

        long[][] bosses = new long[ k ][ 2 ];
        for( int i = 0; i < k; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            bosses[ i ][ 0 ] = Long.parseLong(token.nextToken());
            bosses[ i ][ 1 ] = Long.parseLong(token.nextToken());
        }

        for( int i = 1; i < n + 1; i ++ ){
            int[][] table = new int[ k + 1 ][ 901 ];
            long power = characters[ i - 1 ];
            for( int j = 1; j < k + 1; j ++ ){

                long meso = bosses[ j - 1 ][ 1 ];
                long hp = bosses[ j - 1 ][ 0 ];

                long div = hp % power == 0 ? hp / power : hp / power + 1;

//                System.out.println( power + " : " + div );
                for( int time = 1; time < Math.min( div, 901 ); time++ ){
                    table[ j ][ time ] = table[ j - 1 ][ time ];
                }
                if( div > 900 ) continue;
                for(int time = (int) div; time < 901; time ++ ){
                    table[ j ][ time ] = (int) Math.max( table[ j - 1 ][ time ], table[ j - 1 ][(int) (time - div)] + meso );
                }



            }
//            for( int z = 0; z < k + 1; z ++ ) System.out.println( Arrays.toString( table[ z ] ) );
//            System.out.println( "--");
            result[ i - 1 ] = table[ k ][ 900 ];

        }

//        System.out.println( Arrays.toString( result ) );

        int cnt = 0;
        int ans = 0;
        for( int i = result.length - 1; i >= 0; i -- ){
            if( cnt == m ) break;
            ans += result[ i ];

            cnt++;
        }

        System.out.println( ans );

    }
}