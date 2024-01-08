import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.*;

public class J_9095 {
    public static int count;
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int N =  Integer.parseInt( bf.readLine() );


        for( int i = 0; i < N; i++ ) {
            count = 0;
            int n = Integer.parseInt( bf.readLine() );
            dfs( n, 0 );

            System.out.println( count );
        }

    }

    public static void dfs( int n, int sum ) {


        for( int i = 1; i < 4; i ++  ) {
            if( sum + i < n ) {
                dfs( n, sum + i );

            }else if( sum + i == n ) {
                count++;
            }
        }

    }



}