package J6603;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] arr;
    static int n;
    static boolean[] visit;
    public static void main(String[] args) throws IOException {
        while( true ){
            token = new StringTokenizer( bf.readLine() );
            n = stoi(token.nextToken());
            if( n == 0 ){
                break;
            }
            arr = new int[ n ];
            visit = new boolean[ n ];
            int idx = 0;
            while( token.hasMoreTokens() ){
                int k = stoi( token.nextToken() );
                arr[ idx++ ] = k;
            }
//            System.out.println( lst.toString() );
            dfs( 0, 0 );

            System.out.println();

        }
    }

    private static void dfs(int depth, int start ) {
//        System.out.println( pos + " " + depth );
        if( depth == 6 ){
            StringBuilder sb = new StringBuilder();
            for( int i = 0; i < n; i ++ ){
                if( visit[ i ] ) sb.append( arr[ i ] ).append( " " );
            }
            System.out.println( sb );

            return;
        }

        for( int i = start; i < n; i ++ ){
            visit[ i ] = true;
            dfs( depth + 1, i + 1 );
            visit[ i ] = false;
        }
    }

    public static int stoi( String token ){
        return Integer.parseInt( token );
    }
}