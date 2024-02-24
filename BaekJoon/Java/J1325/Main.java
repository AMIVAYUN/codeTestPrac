package J1325;

import java.io.*;
import java.util.*;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static BufferedWriter bw = new BufferedWriter( new OutputStreamWriter( System.out ) );
    //    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int Mx = 0;
    static ArrayList< Integer > answer;

    static ArrayList<Integer>[] graph;

    static boolean[] visit;

    static int[] result;

    //A가 B 신뢰하면 B를 해킹시 A도 해킹 가능.
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int n = Integer.parseInt( token.nextToken() );
        int m = Integer.parseInt( token.nextToken() );
        graph = new ArrayList[ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ){
            graph[ i ] = new ArrayList<>();
        }
        for( int i = 0; i < m; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int b = Integer.parseInt( token.nextToken() );
            int a = Integer.parseInt( token.nextToken() );
            graph[ a ].add( b );
        }

        result = new int[ n + 1 ];

        for( int i = 1; i < n + 1; i ++ ){
            visit = new boolean[ n + 1 ];
            dfs( i, i );
            Mx = Math.max( result[ i ] , Mx );
//            Queue< Integer > q = new ArrayDeque<>();
//            q.add( i );
//            boolean visit[] = new boolean[ n + 1 ];
//            visit[ i ] = true;
//            int cnt = 1;
//            while( !q.isEmpty() ){
//                int pos = q.poll();
//
//                for( int next : graph[ pos ] ){
//                    if( visit[ next ] == false ){
//                        visit[ next ] = true;
//                        cnt += 1;
//                        q.add( next );
//                    }
//                }
//
//            }
//            result[ i ] = cnt;
//            Mx = Math.max( cnt, Mx );

        }
        StringBuilder sb = new StringBuilder();
        for( int i = 1; i < n + 1; i ++ ){
            if( result[ i ] == Mx ){
                sb.append(i).append(" ");
//                bw.write( i + " " );
            }
        }
        System.out.println( sb );


    }

    private static void dfs( int start, int now ) {
        visit[ now ] = true;
        for( int next: graph[ now ] ){
            if( visit[ next ] ) {
                continue;
            }
            visit[ next ] = true;
            result[ start ]++;
            dfs( start, next );

        }
    }

    static void binaryInsert( ArrayList<Integer> lst, int a ){
        int lt = 0; int rt = lst.size() - 1;
        if( lst.get( lt ) > a ){
            lst.add( 0, a );
            return;
        }

        if( lst.get( rt ) < a ){
            lst.add( a );
            return;
        }
        int ans = 0;
        while( lt <= rt ){
            int mid = ( lt + rt ) / 2;
            if( lst.get( mid ) >= a ){
                lt = mid + 1;
                ans = mid;
            }else{
                rt = mid - 1;
            }

        }

        lst.add( ans, a );

    }


}