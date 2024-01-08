package J9466;

import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();

    static int n,cnt;

    static int[] parents;

    static boolean[] visit;
    static boolean[] result;
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt( bf.readLine() );

        for( int i = 0; i < t; i ++ ){
            n = Integer.parseInt( bf.readLine() );
            parents = new int[ n ];
            visit = new boolean[ n ];
            result = new boolean[ n ];
            cnt = 0;
            token = new StringTokenizer( bf.readLine() ) ;
            for( int j = 0; j < n; j ++ ){
                int now = Integer.parseInt( token.nextToken() ) - 1;
                parents[ j ] = now;
//                if( parents[ j ] == j ){
//                    result[ j ] = true;
//                    cnt++;
//                }
            }

            for( int j = 0; j < n; j ++ ){
                dfs2( j );
            }

            sb.append( n-cnt ); sb.append("\n");

            /*
            SOLUTION1 T.O 내 로직은 가지치기가 불가능

            for( int j = 0; j < n; j ++ ){
                if( result[ j ] ){
                    continue;
                }
                visit = new boolean[ n ];
                visit[ j ] = true;
                if( !dfs( j, j ) ) {
                    visit[ j ] = false;
                }else{
                    for( int k = 0; k < n; k ++ ){
                        result[ k ] = visit[ k ] || result[ k ];
                    }
                }
            }



            int cnt = 0;
            for( int j = 0; j < n; j ++ ){
                if( !result[ j ] ){
                    cnt ++;
                }
            }


            sb.append( cnt ); sb.append("\n");

             */
        }

        System.out.println( sb );


    }
    // sol1 가지치기가 불가능한 DFS
    private static boolean dfs(int start, int now) {

        if( start == parents[ now ] ){
            return true;
        }
        int p = parents[ now ];
        if( !visit[ p ] && !result[ p ] ){
            visit[ p ] = true;
            if( !dfs( start, p ) ){
                return false;
            }
            return true;
        }

        return false;
    }

    private static void dfs2( int now ){
        if( visit[ now ] ){
            return;
        }

        visit[ now ] = true;
        int next = parents[ now ];

        if( !visit[ next ] ){
            dfs2( next );
        }else{
            if( !result[ next ] ){
                cnt++;
                for( int i = next; i != now; i = parents[ i ] ){
                    cnt++;
                }
            }
        }

        result[ now ] = true;
    }


}

