package J2252;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, M, in[];
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        String[] line = bf.readLine().split(" ");
        N = Integer.parseInt( line[ 0 ] );
        M = Integer.parseInt( line[ 1 ] );
        in = new int[ N ];
        graph = new ArrayList[ N ];
        for( int i = 0; i < N; i ++ ){
            graph[ i ] = new ArrayList<>();
        }
        for( int i = 0; i < M; i++ ){
            String[] diff = bf.readLine().split( " " );
            int A = Integer.parseInt( diff[ 0 ] ) - 1;
            int B = Integer.parseInt( diff[ 1 ] ) - 1;
            graph[ A ].add( B );
            in[ B ] ++;
        }


        ArrayDeque< Integer > dq = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for( int i = 0; i < N; i++ ){
            if( in[ i ] == 0 ){
                dq.add( i );
                sb.append( ( i + 1 ) ).append(" ");
            }
        }

        while( !dq.isEmpty() ){
            int size = dq.size();
            for( int i = 0; i < size; i ++ ){
                int now = dq.poll();
                for( int next : graph[ now ] ){
                    in[ next ]--;
                    if( in[ next ] == 0 ){
                        dq.add( next );
                        sb.append( ( next + 1 ) + " " );
                    }
                }
            }

        }
        sb.delete( sb.length() - 1, sb.length() );
        System.out.println( sb );

    }

}
