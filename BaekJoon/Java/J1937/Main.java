package J1937;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int answer = 0;
    static int n, graph[][], memo[][], dx[] = { 0, 0, -1, 1 }, dy[] = { 1, -1, 0, 0 };

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );
        graph = new int [ n ][ n ];
        memo = new int[ n ][ n ];
        for( int i = 0; i < n; i ++ ){
            String[] line = bf.readLine().split(" ");
            for( int j = 0; j < n; j ++ ){
                int num = Integer.parseInt( line[ j ] );
                graph[ i ][ j ] = num;
            }
        }
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < n; j ++ ){
                if( memo[ i ][ j ] == 0 ) {
                    dfs(i, j, graph[i][j]);
                }
            }
        }

        System.out.println(answer);

    }

    public static int dfs( int x, int y, int now ){

        int Mx = 0;
        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];
            if( isRight( nx, ny ) ){
                if( graph[ nx ][ ny ] > now ){
                    if( memo[ nx ][ ny ] == 0 ){
                        Mx = Math.max( Mx, dfs( nx, ny, graph[ nx ][ ny ] ) );
                    }else{
                        Mx = Math.max( memo[ nx ][ ny ], Mx );
                    }
                }
            }
        }
        memo[ x ][ y ] = Mx + 1;
        answer = Math.max( memo[ x ][ y ], answer );
        return memo[ x ][ y ];
    }

    public static boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}