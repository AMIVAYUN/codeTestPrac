package J2669;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] graph = new int[ 100 ][ 100 ];



    public static void main(String[] args) throws IOException {
        for( int i = 0; i < 4; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int x1 = Integer.parseInt(token.nextToken() ); int y1 = Integer.parseInt(token.nextToken() );
            int x2 = Integer.parseInt(token.nextToken() ); int y2 = Integer.parseInt(token.nextToken() );

            for( int x = x1 - 1; x < x2 - 1; x ++ ){
                for( int y = y1 - 1; y < y2 - 1; y ++ ){
                    graph[ x ][ y ] = 1;
                }
            }
        }
        int cnt = 0;
        for( int x = 0; x < 100; x ++ ){
            for( int y = 0; y < 100; y ++ ){
                cnt += graph[ x ][ y ];
            }
        }
        System.out.println( cnt );
    }
}
