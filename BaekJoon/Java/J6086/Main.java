package J6086;

import CallbyRefTest.A;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] graph = new int[ 58 ][ 58 ], flow = new int[ 58 ][ 58 ];

    static ArrayList< Integer >[] edges = new ArrayList[ 58 ];


    static{
        for( int i = 0; i < 58; i ++ ){
            edges[ i ] = new ArrayList<>();
        }
    }


    static int n, parent[];

    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );

        for ( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );

            String x = token.nextToken();
            String y = token.nextToken();
            int val = stoi( token.nextToken() );

            graph[ x.charAt( 0 ) - 65 ][ y.charAt( 0 ) - 65 ] += val;
            graph[ y.charAt( 0 ) - 65 ][ x.charAt( 0 ) - 65 ] += val;

            edges[ x.charAt( 0 ) - 65 ].add( y.charAt( 0 ) - 65 );
            edges[ y.charAt( 0 ) - 65 ].add( x.charAt( 0 ) - 65 );

        }

        parent = new int[ 58 ];
        int total = 0;
        int start = 0, end = 25;

        ArrayDeque< Integer > dq;

        while( true ){
            dq = new ArrayDeque<>();
            parent[ start ] = start;
            Arrays.fill( parent, -1 );
            dq.add( start );

            while( !dq.isEmpty() && parent[ end ] == -1 ){
//                System.out.println( dq );
                int pos = dq.poll();
                for( int next : edges[ pos ]){
                    if( graph[ pos ][ next ] > 0 && graph[ pos ][ next ] - flow[ pos ][ next ] > 0 && parent[ next ] == -1 ){
                        dq.add( next );
                        parent[ next ] = pos;
                    }
                }
            }
            if( parent[ end ] == -1 ) break;
            int amount = Integer.MAX_VALUE;
            for( int i = end; i != start; i = parent[ i ] ){
                amount = Math.min( graph[ parent[ i ] ][ i ] - flow[ parent[ i ] ][ i ], amount );
            }

            for( int i = end; i != start; i = parent[ i ] ){
                flow[ parent[ i ] ][ i ] += amount;
                flow[ i ][ parent[ i ] ] -= amount;
            }

            total += amount;

        }

        System.out.println( total );
    }

    public static Integer stoi( String token ){
        return Integer.parseInt( token );
    }
}
