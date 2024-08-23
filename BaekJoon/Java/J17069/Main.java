package J17069;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int n;
    static int[][] graph;
    static long[][][] dp;
    static int cnt;
//    static int[][][] dxys = { { { 0, 1, 0 }, { 1, 1, 1 } }, { { 0, 1, 0 }, { 1, 0, 2 }, { 1, 1, 1 } }, { { 1, 0, 2 }, { 1, 1, 1 } } };
    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        dp = new long[ n + 1 ][ n + 1 ][ 3 ];
        graph = new int[ n + 1 ][ n + 1 ];
        for( int i = 1; i <= n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 1; j <= n; j ++ ){
                graph[ i ][ j ] = stoi( token.nextToken() );
            }
        }

        dp[ 1 ][ 2 ][ 0 ] = 1;

        for( int x = 1; x <= n; x ++ ){
            for( int y = 3; y <= n; y ++ ){
                if( graph[ x ][ y ] == 1 ){
                    continue;
                }

                dp[ x ][ y ][ 0 ] = dp[ x ][ y - 1 ][ 0 ] + dp[ x ][ y - 1 ][ 1 ];
                if( !( graph[ x ][ y - 1 ] == 1 || graph[ x - 1 ][ y ] == 1 ) ){
                    dp[ x ][ y ][ 1 ] = dp[ x - 1 ][ y - 1 ][ 2 ] + dp[ x - 1 ][ y - 1 ][ 0 ] + dp[ x - 1 ][ y - 1 ][ 1 ];
                }

                dp[ x ][ y ][ 2 ] = dp[ x - 1 ][ y ][ 2 ] + dp[ x - 1 ][ y ][ 1 ];
            }
        }

//        System.out.println(dp[ n ]);
//        for( int x = 0; x <= n; x ++ ){
//            for( int y = 0; y <= n; y ++ ){
//                System.out.print( Arrays.toString( dp[ x ][ y ] ) + " " );
//            }
//            System.out.println();
//        }
        System.out.println( dp[ n ][ n ][ 0 ] + dp[ n ][ n ][ 1 ] + dp[ n ][ n ][ 2 ] );

    }
    //걍 가니깐 터짐 dp로 가야 될듯
//    private static void dfs( int x, int y, int direc ){
//        if( x == n - 1 && y == n - 1 ){
//            cnt++;
//            return;
//        }
//
//
//        for( int[] dxy : dxys[ direc ] ){
//            int nx = x + dxy[ 0 ];
//            int ny = y + dxy[ 1 ];
//
//            if( isRight( nx, ny ) ){
//                if( graph[ nx ][ ny ] != 1 ){


//                  dfs( nx, ny, dxy[ 2 ] );
//              }
//            }
//        }
//
//
//
//    }
    private static boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    private static int stoi( String token ){
        return Integer.parseInt( token );
    }
}