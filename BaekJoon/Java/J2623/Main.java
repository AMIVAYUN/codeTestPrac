package J2623;


import java.io.*;
import java.util.*;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static ArrayList<Integer>[] graph;
    static int nodes[];
    static int n, m;
    static ArrayList< Integer > ans = new ArrayList<>();
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() ); m = Integer.parseInt( token.nextToken() );
        nodes = new int[ n + 1 ];
        graph = new ArrayList[ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ){
            graph[ i ] = new ArrayList<>();
        }
        for( int i = 0; i < m; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int k = Integer.parseInt( token.nextToken() );
            int prev = Integer.parseInt( token.nextToken() );
            for( int j = 0; j < k - 1; j ++ ){
                int a = Integer.parseInt( token.nextToken() );
                graph[ prev ].add( a );
                nodes[ a ]++;
                prev= a;
            }
        }

        topologySort();

        if( ans.size() == n ){
            for( int i : ans ){
                System.out.println( i );
            }
        }else{
            System.out.println( 0 );
        }


    }

    public static void topologySort(){
        Queue< Integer > q = new ArrayDeque<>();

        for( int i = 1; i < n + 1; i ++ ){
            if( nodes[ i ] == 0 ){
                q.add( i );
            }
        }

        while( !q.isEmpty() ){
            int pos = q.poll();

            ans.add( pos );

            for( int next: graph[ pos ] ){
                nodes[ next ]--;
                if( nodes[ next ] == 0 ){
                    q.add( next );
                }
            }

        }




    }
}