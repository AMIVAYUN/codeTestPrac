import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class J_24463 {
    public static int[] dx = { -1, 1, 0, 0 };
    public static int[] dy = { 0, 0, -1, 1 };
    public static boolean flag = false;
    public static char[][] graph;
    public static int[][] visit;
    public static void dfs( int[] now, int[] end,int n, int m ){
        if( flag ){
            return;
        }
        int x, y;
        x = now[ 0 ]; y = now[ 1 ];
        if( x == end[ 0 ] && y == end[ 1 ] ){

            flag = true;
            return;
        }


        for( int i = 0 ; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];

            if( 0<= nx && nx < n && 0<= ny && ny < m ){
                if( visit[ nx ][ ny ] != 1 && graph[ nx ][ ny ] != '+' && flag == false){
                    visit[ nx ][ ny ] = 1;
                    graph[ nx ][ ny ] = '.';
                    dfs(new int[]{ nx, ny }, end, n, m );
                    visit[ nx ][ ny ] = 0;
                    if( !flag ){
                        graph[ nx ][ ny ] = '@';
                    }


                }
            }
        }





    }
    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        Object[] a = Arrays.stream( bf.readLine().split(" ") ).map( Integer::parseInt).toArray();
        int n = (int)a[ 0 ];
        int m = ( int )a[ 1 ];
        int[] start = new int[ 2 ], end = new int[ 2 ];
        graph = new char[ n ][ m ];
        boolean flag = true;
        for( int i = 0; i < n; i ++ ){
            char[] arr = bf.readLine().toCharArray();

            for( int j = 0; j < m; j ++ ){
                if( arr[ j ] == '.' ){
                    if( ( i == 0 || i == n - 1 ) ){
                        if( flag ){
                            start[ 0 ] = i; start[ 1 ] = j;
                            flag =false;
                        }else{
                            end[ 0 ] = i; end[ 1 ] = j;
                        }
                    }else if( j == 0 || j == m - 1 ){
                        if( flag ){
                            start[ 0 ] = i; start[ 1 ] = j;
                            flag = false;
                        }else{
                            end [ 0 ] = i; end[ 1 ] = j;
                        }
                    }

                    arr[ j ] = '@';
                }
            }
            graph[ i ] = arr;
        }


        int x0 = 0; int x1 = n - 1; int y0 = 0; int y1 = m - 1;




        visit = new int[ n ][ m ];
        visit[ start[ 0 ] ][ start[ 1 ] ] = 1;
        dfs( start, end, n, m );
        graph[ start[ 0 ] ][ start[ 1 ] ] = '.';

        StringBuilder builder = new StringBuilder();
        for( int i = 0; i < n; i ++ ){
            builder.append( graph[ i ] );
            builder.append("\n" );

        }

        System.out.println( builder );

    }


}
