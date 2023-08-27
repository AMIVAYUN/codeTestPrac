package J14502;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int[][] graph;
    static int Mx = 0;
    static int[][] dxy = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int n, m;
    static int choosed[][];
    static int virusCnt;
    static ArrayList< Virus > vis;
    static class Virus{
        int x;
        int y;

        public Virus( int x, int y ) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        m = Integer.parseInt( token.nextToken() );
        virusCnt = 0;
        graph = new int[ n ][ m ];
        choosed = new int[ m ][ 2 ];
        vis = new ArrayList<>();
        for( int i = 0; i < n; i ++ ) {
            token = new StringTokenizer( bf.readLine() );

            for( int j = 0; j < m; j ++ ) {
                graph[ i ][ j ] = Integer.parseInt( token.nextToken() );
                if( graph[ i ][ j ] == 2 ) {
                    vis.add( new Virus( i, j ) );
                    virusCnt++;
                }
            }
        }


        getComb( 0 );
        System.out.println( Mx );
    }

    static int[][] deepCopyAndVirusSetting(){


        int[][] subGraph = new int[ n ][ m ];
        for( int i = 0; i < n; i ++ ) {
            for( int j = 0; j < m; j ++ ) {
                subGraph[ i ][ j ] = graph[ i ][ j ];

            }
        }

        return subGraph;
    }

    static void getComb( int depth ) {


        if( depth == 3 ) {
            int[][] subGraph = deepCopyAndVirusSetting();

            int result = getResult( subGraph );
            if( result != -1 ) {
                Mx = Math.max ( Mx, result );
            }

            return;
        }


        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( graph[ i ][ j ] == 0 ){
                    graph[ i ][ j ] = 1;
                    getComb( depth + 1 );
                    graph[ i ][ j ] = 0;
                }

            }
        }
    }

    static class Pos{
        int x;
        int y;
        int cnt;
//        boolean isDeActivated = false;
//        int whenActivated = 0;
        public Pos( int x, int y, int cnt ) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }

        public String toString() {
            return "{ " + this.x + " " + this.y + " " + this.cnt + " " +/* this.isDeActivated + " " + this.whenActivated +*/ " } ";
        }
    }
    static boolean isRight( int x, int y ) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
    private static int getResult(int[][] subGraph) {

        Queue< Pos > q = new ArrayDeque<>();
        int[][] visit = new int[ n ][ m ];
        for( int[] row: visit ) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        for( Virus v : vis ){
            q.add( new Pos( v.x, v.y, 0 ) );
        }

        while( !q.isEmpty() ) {
            Pos now = q.poll();

            int x = now.x;
            int y = now.y;


                for( int i = 0; i < 4; i ++ ) {
                int nx = x + dxy[ i ][ 0 ];
                int ny = y + dxy[ i ][ 1 ];
                if( isRight( nx, ny ) ) {
                    if( subGraph[ nx ][ ny ] != 1 ) {
                        if( visit[ nx ][ ny ] > now.cnt + 1 ) {
                            Pos next = new Pos( nx, ny, now.cnt + 1 );
                            subGraph[ nx ][ ny ] = 2;
                            visit[ nx ][ ny ] = now.cnt + 1;
                            q.offer( next );
                        }
                    }
                }
            }



        }

        return isRightGraph(subGraph);



    }




    static int isRightGraph( int[][] subGraph ) {
        int cnt = 0;
        for( int i = 0; i < n; i ++ ) {
            for( int j = 0; j < m; j ++ ) {
                if( subGraph[ i ][ j ] == 0 ) {
                    cnt++;
                }
            }
        }

        return cnt;
    }

}