package J17260;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    static int ans = 0;

    static int n, k, heights[];
    static boolean[] visited;

    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {

        token = new StringTokenizer( bf.readLine() );
        n = stoi( token.nextToken() );
        k = stoi( token.nextToken() ) - 1;
        heights = new int[ n ];
        visited = new boolean[ n ];
        token = new StringTokenizer( bf.readLine() );
        for( int i = 0; i < n; i ++ ){
            heights[ i ] = stoi( token.nextToken() );
        }
        graph = new ArrayList[ n ];

        for( int i = 0; i < n; i++ ){
            graph[ i ] = new ArrayList<>();
        }
        for( int i = 0; i < n - 1; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int x = stoi( token.nextToken() ) - 1;
            int y = stoi( token.nextToken() ) - 1;

            if( heights[x] == heights[y] ){
                graph[ x ].add( y );
                graph[ y ].add( x );
            }else{
                graph[ x ].add( y );
            }

        }
        visited[ 0 ] = true;

        for( int next: graph[ 0 ] ){
            if( heights[ next ] > heights[ 0 ] ) {
                continue;
            }
            visited[ next ] = true;
            dfs2( next, getNext2(BigDecimal.valueOf(heights[ 0 ]), BigDecimal.valueOf( heights[ next ] ) ) );
            visited[ next ] = false;
        }

        System.out.println( ans );
    }

    private static void dfs2( int pos, BigDecimal prev ) {
//        System.out.println( pos + " " + prev );
        if( pos == k ){
            ans = 1;
            return;
        }

        if( ans == 1 ) return;

        for( int next: graph[ pos ] ){
            if( ans == 1 ){
                return;
            }
            if( visited[ next ] ) continue;
            if( prev.compareTo( BigDecimal.valueOf( heights[ next ] ) ) <= 0 ){
                continue;
            }

            BigDecimal canBe = getNext2( prev, BigDecimal.valueOf(heights[ next ]));


            visited[ next ] = true;
            dfs2( next, canBe );
            visited[ next ] = false;


        }
    }

    public static void dfs( int now, double prev ){

//        System.out.println(Arrays.toString( visited ));
        if( now == k ){
            ans = 1;
            return;
        }

        if( ans == 1 ) return;

        for( int next: graph[ now ] ){
            if( ans == 1 ){
                return;
            }
            if( visited[ next ] ) continue;
            if( prev < heights[ next ] ){
                continue;
            }

            double canBe = getNext( prev, heights[ next ] );


            visited[ next ] = true;
            dfs( next, canBe );
            visited[ next ] = false;


        }


    }

    public static Integer stoi(String token){
        return Integer.parseInt( token );
    }
    public static double getNext( double height, int nextHeight ){
        return nextHeight + ( ( height - nextHeight ) / 2 );
    }

    private static BigDecimal getNext2(BigDecimal prev, BigDecimal next) {
        return prev.subtract( next ).divide( BigDecimal.valueOf( 2 ) ).add( next );
    }
}