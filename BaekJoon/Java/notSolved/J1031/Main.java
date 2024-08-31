package notSolved.J1031;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m, js[], hs[];

    static int[][] graph;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = stoi( token.nextToken() );
        m = stoi( token.nextToken() );

        js = new int[ n ];
        hs = new int[ m ];
        graph = new int[ n ][ m ];
        token = new StringTokenizer(bf.readLine() );

        for( int i = 0; i < n; i++ ){
            js[ i ] = stoi( token.nextToken() );
        }

        token = new StringTokenizer(bf.readLine() );

        for( int i = 0; i < m; i++ ){
            hs[ i ] = stoi( token.nextToken() );
        }

        boolean res = dfs( 0, 0 );

        if( res ){
            print();
        }else{
            System.out.println( -1 );
        }

    }

    public static boolean dfs( int x, int y ){

//        System.out.println( "x = " + x + " , y= " + y );


        if( x == n && y == 0 ){

//            print();
            return isEnd();
        }

        int nx = x;
        int ny = y + 1;

        if( ny == m ){
            nx = x + 1;
            ny = 0;
        }

        boolean res = dfs( nx, ny );
        if( res ) return true;

        if( js[ x ] > 0 && hs[ y ] > 0 ){
            graph[ x ][ y ] = 1;
            js[ x ] --;
            hs[ y ] --;



            res = dfs( nx, ny );
            if( res ) return true;

            graph[ x ][ y ] = 0;
            js[ x ] ++;
            hs[ y ] ++;


        }



        return false;
    }

    private static void print() {
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                System.out.print( graph[ i ][ j ]);
            }
            System.out.println();
        }
    }

    private static boolean isEnd() {

        for( int i = 0; i < n; i ++ ){
            if( js[ i ] != 0 ){
                return false;
            }
        }

        for( int j = 0; j < m; j ++ ){
            if( hs[ j ] != 0 ){
                return false;
            }
        }

        return true;
    }

    public static int stoi( String token ){
        return Integer.parseInt( token );
    }
}