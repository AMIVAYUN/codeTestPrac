package J1245;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int[][] graph;
    static boolean[][] visit;
    static boolean[][] visit2;
    static int[] dx = { 0, 0, -1, 1, -1, 1, -1, 1  };
    static int[] dy = { 1, -1, 0, 0, -1, -1, 1, 1 };
    static int n, m;
    static int cnt;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        m = Integer.parseInt( token.nextToken() );
        graph = new int[ n ][ m ];
        visit = new boolean[ n ][ m ];
        visit2 = new boolean[ n ][ m ];

        for( int x = 0; x < n; x ++ ){
            token = new StringTokenizer( bf.readLine() );

            for( int y = 0; y < m; y ++ ){
                graph[ x ][ y ] = Integer.parseInt( token.nextToken( ) );
            }
        }


        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < m; y ++ ){
                if( !visit[ x ][ y ] && graph[ x ][ y ] > 0 ){
                    visit[ x ][ y ] = true;
                    bfs( x, y );
                }
            }
        }

        System.out.println( cnt );


    }

    private static void bfs(int sx, int sy) {
        ArrayDeque< Node > dq = new ArrayDeque<>();
        ArrayList< Node > arrlst = new ArrayList< Node >();
        Node startNode = new Node( sx, sy, graph[ sx ][ sy ] );
        arrlst.add( startNode );


        dq.add( startNode );

        while( !dq.isEmpty() ){
           Node now = dq.poll();
           int x = now.x;
           int y = now.y;

           for( int i = 0; i < 8; i ++ ){
               int nx = x + dx[ i ];
               int ny = y + dy[ i ];
               if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                   if( !visit[ nx ][ ny ] && graph[ nx ][ ny ] > 0 ){
                       visit[ nx ][ ny ] = true;
                       Node next = new Node( nx, ny, graph[ nx ][ ny ] );
                       dq.add( next );
                       arrlst.add( next );
                   }
               }
           }
        }

        Collections.sort( arrlst );
        ArrayDeque< Node > lstdq = new ArrayDeque<>( arrlst );
        while( !lstdq.isEmpty() ){
            Node top = lstdq.poll();
            if( visit2[ top.x ][ top.y ] ) continue;
            visit2[ top.x ][ top.y ] = true;
            bfs2( top );
            cnt++;
        }



    }

    private static void bfs2(Node top) {
        ArrayDeque< Node > dq = new ArrayDeque<>();
        dq.add( top );
        while( !dq.isEmpty() ){
            Node now = dq.poll();
            int x = now.x;
            int y = now.y;
            int h = now.h;

            for( int i = 0; i < 8; i ++ ) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if( !visit2[ nx ][ ny ] && graph[ nx ][ ny ] <= h && graph[ nx ][ ny ] > 0 ){
                        visit2[ nx ][ ny ] = true;
                        dq.add( new Node( nx, ny, graph[ nx ][ ny ] ) );
                    }
                }
            }

        }

    }

    static void printVisit(){
        for( int x = 0; x < n; x ++ ){
            System.out.println(Arrays.toString( visit[ x ] ) );
        }
    }
    static class Node implements Comparable<Node>{
        int x, y, h;

        public Node(int x, int y, int h) {
            this.x = x;
            this.y = y;
            this.h = h;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "x=" + x +
                    ", y=" + y +
                    ", h=" + h +
                    '}';
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare( o.h, this.h );
        }
    }
}