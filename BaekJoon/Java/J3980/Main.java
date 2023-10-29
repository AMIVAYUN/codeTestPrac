package J3980;


import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int Mx;
    static boolean visit[];
    static ArrayList<int[]>[] athletes;


    public static void main( String[] args ) throws IOException {
        int t = Integer.parseInt( bf.readLine() );

        for( int tc = 0; tc < t; tc ++ ){

            Mx = 0;
            athletes = new ArrayList[ 11 ];

            for( int i = 0; i < 11; i ++ ){
                athletes[ i ] = new ArrayList<>();
            }
            visit = new boolean[ 11 ];
            for( int i = 0; i < 11; i ++ ){
                token = new StringTokenizer( bf.readLine() );
                for( int j = 0; j < 11; j ++ ){
                    int val = Integer.parseInt( token.nextToken() );
                    if( val != 0 ){
                        athletes[ j ].add( new int[]{ i, val } );
                    }
                }
            }

            dfs( 0, 0 );

            System.out.println( Mx );



        }

    }


    static void dfs( int depth, int cnt ){
        if( depth == 11 ){
            Mx = Math.max( Mx, cnt );
            return;
        }



        for( int[] next: athletes[ depth ] ){
            int pos = next[ 0 ];
            int val = next[ 1 ];
            if( visit[ pos ] == false ){
                visit[ pos ] = true;
                dfs( depth + 1, cnt + val );
                visit[ pos ] = false;

            }
        }
    }
}