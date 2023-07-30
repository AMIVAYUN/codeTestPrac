import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J_1937{
    public static int[][] dxy = { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };
    public static int[][] graph;
    public static int Mx = 0;
    public static int N;

    public static int[][] visit;
    public static int[][][] visitDepth;
    public static void main( String[] args ) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        graph = new int[ N ][ N ];
//        visitDepth = new int[ N * N ][ N ][ N ]; 메모리 아웃
        visit = new int[ N ][ N ];
        for (int i = 0; i < N; i++) {
            int[] row = Arrays.stream(bf.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            graph[i] = row;
        }
        int cnt = 0;
        for( int x = 0; x < N; x ++ ){
            for( int y = 0; y < N; y ++ ){

                if( visit[ x ][ y ] == 0 ){
                    dfs2( graph[ x ][ y ], x, y );
                }

                Mx = Math.max( visit[ x ][ y ], Mx );



            }
        }

        for( int[] row : visit ){
            System.out.println( Arrays.toString( row ) );
        }

        System.out.println( Mx );
    }
    public static int dfs2( int now, int x, int y ){
        if( visit[ x ][ y ] == 0 ){
            visit[ x ][ y ] = 1;
        }
        for( int i = 0; i < 4; i ++ ){
            int nx = x + dxy[ i ][ 0 ];
            int ny = y + dxy[ i ][ 1 ];


            if( isRight( nx, ny ) ){
                if( graph[ nx ][ ny ] > now ){
                    if( visit[ nx ][ ny ] == 0 ){
                        dfs2( graph[ nx ][ ny ]  , nx, ny );
                    }
                    visit[ x ][ y ] = Math.max( visit[ x ][ y ] , 1 + visit[ nx ][ ny ] );

                }
            }
        }

        return visit[ x ][ y ];





    }
    //34% TimeOut
    public static void dfs( int now, int count, int x, int y ){

        for( int i = 0; i < 4; i ++ ){
            int nx = x + dxy[ i ][ 0 ];
            int ny = y + dxy[ i ][ 1 ];


            if( isRight( nx, ny ) ){
                if( graph[ nx ][ ny ] > now ){
                    dfs( graph[ nx ][ ny ] , count + 1 , nx, ny );
                }
            }
        }





        Mx = Math.max( Mx, count );
        return;

    }

    public static boolean isRight( int x, int y ){


        return x >= 0 && x < N && y >= 0 && y < N;
    }
}