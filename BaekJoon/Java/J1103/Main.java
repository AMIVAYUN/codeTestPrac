package J1103;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m, graph[][], dp[][];


    static int[] dx = { -1, 0, 1, 0 }, dy = { 0, -1, 0, 1 };

    //무한번을 안읽음;
    static boolean visit[][];
    static boolean infinite = false;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        n = stoi( token.nextToken() );
        m = stoi( token.nextToken() );

        graph = new int[ n ][ m ];
        dp = new int[ n ][ m ];
        visit = new boolean[ n ][ m ];

        for( int i = 0; i < n; i ++ ){
            String row = bf.readLine();
            Arrays.fill( dp[ i ], -1 );
            for( int j = 0; j < m; j ++ ){

                char c = row.charAt( j );

                if( c == 'H' ){
                    graph[ i ][ j ] = -1;
                    dp[ i ][ j ] = 0;
                    continue;
                }

                int k = c - '0';

                graph[ i ][ j ] = k;
            }
        }

        visit[ 0 ][ 0 ] = true;
        dfs( 1, 0, 0 );

        System.out.println( infinite ? -1 : answer );
    }

    public static void dfs( int depth, int x, int y ){
//        System.out.println( x + "," + y );
        if( infinite ) return;
//        System.out.println( depth + " " + x + " " + y);
        answer = Math.max( answer, depth );

        int dist = graph[ x ][ y ];
//        dp[ x ][ y ] = 1;

//        int subCnt = 0;
        for( int i = 0; i < 4; i ++ ){
            int nx = x + ( dx[ i ] * dist );
            int ny = y + ( dy[ i ] * dist );

            if( isRight( nx , ny ) && dist != -1 && depth + 1 > dp[ nx ][ ny ] ){
                if( visit[ nx ][ ny ] ){
                    infinite = true;
                    return;
                }
                dp[ nx ][ ny ] = depth + 1;
                visit[ nx ][ ny ] = true;
                dfs( depth + 1, nx, ny );
                visit[ nx ][ ny ] = false;

            }
        }

//        dp[ x ][ y ] += subCnt ;

//        System.out.println( x + " , " + y + " == " + dp[ x ][ y ] );
//        return dp[ x ][ y ];
    }

    public static int stoi( String token ){
        return Integer.parseInt( token );
    }

    public static boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < m && graph[ x ][ y ] != -1;
    }
}