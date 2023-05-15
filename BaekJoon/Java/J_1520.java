import java.util.*;
import java.io.*;
public class J_1520 {

    public static int[][] graph;
    public static int[] dx = { -1, 1, 0, 0 };
    public static int[] dy = { 0, 0, -1, 1 };
    public static int[][] Memo;
    public static int N,M;
    public static int dfs( int[] now ){

        int x, y;

        x = now[ 0 ];
        y = now[ 1 ];


        if( x == N - 1 && y == M - 1 ){
            return 1;
        }


        int sum = 0;

        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];

            if( isOk( nx, ny ) ){
                if( graph[ x ][ y ] > graph[ nx ][ ny ] ){
                    int[] next = { nx, ny };
                    sum += dfs( next );
                }
            }
        }


        return sum;
    }

    public static int dfsMemo( int[] now ){

        int x, y;

        x = now[ 0 ];
        y = now[ 1 ];


        if( x == N - 1 && y == M - 1 ){
            Memo[ x ][ y ] = 1;
            return 1;
        }
        if( Memo[ x ][ y ] > -1 ){
            return Memo[ x ][ y ];
        }

        Memo[ x ][ y ] = 0;
        int sum = 0;

        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];

            if( isOk( nx, ny ) ) {
                if (graph[x][y] > graph[nx][ny]) {

                    int[] next = {nx, ny};
                    sum += dfsMemo(next);


                }
            }
        }
        Memo[ x ][ y ] = sum;

        return sum;
    }

    public static boolean isOk( int x, int y ){
        return x < N && x >= 0 && y < M && y >= 0;
    }


    public static void main( String[] args ) throws IOException {


        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        String[] s = bf.readLine().split(" ");

        N = Integer.parseInt( s[ 0 ] );
        M = Integer.parseInt( s[ 1 ] );
        Memo = new int[ N ][ M ];

        for( int i = 0; i < N; i ++ ){
            Arrays.fill( Memo[ i ], -1 );
        }

        graph = new int[ N ][ M ];
        int[] start = { 0, 0 };
        for( int i = 0; i < N; i++ ){
            String[] srow = bf.readLine().split(" ");

            for( int j = 0 ; j < M; j ++ ){
                graph[ i ][ j ] = Integer.parseInt( srow[ j ] );
            }


        }

        int answer = dfsMemo( start );
        /*
        for( int[] row : Memo ){
            for( int a: row ){
                System.out.print( a + " ");
            }
            System.out.println( );
        }

         */
        System.out.print( answer );


    }

    public static void s1main( String[] args ) throws IOException {


        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        String[] s = bf.readLine().split(" ");

        N = Integer.parseInt( s[ 0 ] );
        M = Integer.parseInt( s[ 1 ] );
        graph = new int[ N ][ M ];
        int[] start = { 0, 0 };
        for( int i = 0; i < N; i++ ){
            String[] srow = bf.readLine().split(" ");

            for( int j = 0 ; j < M; j ++ ){
                graph[ i ][ j ] = Integer.parseInt( srow[ j ] );
            }


        }

        int answer = dfs( start );


        System.out.print( answer );


    }

}
