package J2468;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static int[][] graph;

    static boolean[][] visit;

    static int cntMx = 1, height = 1, cnt = 0, dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 }, hiMx = 0;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt( bf.readLine() );

        graph = new int[ N ][ N ];
        for( int x = 0; x < N; x ++ ) {
            token = new StringTokenizer(bf.readLine());
            for (int y = 0; y < N; y++) {
                graph[ x ][ y ] = Integer.parseInt(token.nextToken());
                hiMx = Math.max( hiMx, graph[ x ][ y ] );
            }
        }


        for( ; height <= hiMx; height++ ){
            visit = new boolean[ N ][ N ];
            cnt = 0;
            for( int x = 0; x < N; x ++ ){
                for( int y = 0; y  < N; y ++ ){
                    if( graph[ x ][ y ] >= height && !visit[ x ][ y ] ){
                        visit[ x ][ y ] = true;
                        dfs( x, y );
                        cnt++;
                    }
                }
            }

            cntMx = Math.max( cntMx, cnt );


        }

        System.out.println( cntMx );

    }

    public static void dfs( int x, int y ){



        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];
            if( nx < 0 || nx >= N || ny < 0 || ny >= N ){
                continue;
            }
            if( !visit[ nx ][ ny ] && graph[ nx ][ ny ] >= height ){
                visit[ nx ][ ny ] = true;
                dfs( nx, ny );
            }
        }

    }
}