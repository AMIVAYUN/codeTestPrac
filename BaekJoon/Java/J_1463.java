package workshoptest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.*;
//1463

public class Main {
    public static int count;
    public static int[] dp;
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int N =  Integer.parseInt( bf.readLine() );


        dp = new int[ N + 1 ];
        Arrays.fill( dp, 10000000 );
        dp[ 0 ] = 0; dp[ 1 ] = 0;


        for( int i = 1; i < N + 1; i ++ ) {
            if( i * 3 < N + 1 ) {
                dp[ i * 3 ] = Math.min( dp[ i * 3 ], dp[ i ] + 1 );
            }

            if( i * 2 < N + 1 ) {
                dp[ i * 2 ] = Math.min( dp[ i * 2 ], dp[ i ] + 1 );
            }
            if( i + 1 < N + 1 ) {
                dp[ i + 1 ] = Math.min( dp[ i + 1 ], dp[ i ] + 1 );
            }

        }

        System.out.println( dp[ N ] );


    }





}