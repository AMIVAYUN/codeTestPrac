package J2470;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int Mn = Integer.MAX_VALUE;

    static int n, nums[];

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );

        token = new StringTokenizer( bf.readLine() );

        nums = new int[ n ];

        for( int i = 0; i < n; i ++ ){
            nums[ i ] = Integer.parseInt( token.nextToken() );
        }

        Arrays.sort( nums );
        int[] ans = new int[]{ 0 , n - 1 };
        int lt = 0, rt = n - 1;

        while( lt < rt ){
//            System.out.println( lt + ": " + rt );
            int mid = ( nums[ lt ] + nums[ rt ] );

            if( Math.abs( mid ) < Mn ){
                Mn = Math.abs( mid );
                ans[ 0 ] = lt; ans[ 1 ] = rt;
                continue;
            }

            if( mid >= 0 ){
                rt--;
            }else{
                lt++;
            }

        }


        System.out.println( nums[ ans[ 0 ] ] + " " + nums[ ans[ 1 ] ] );


    }
}
