package J1325;


import java.io.*;
import java.util.*;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
//    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int Mx = 0;
    static ArrayList< Integer > answer;
    static ArrayList< ArrayList< Integer > > graph = new ArrayList<>();

    //A가 B 신뢰하면 B를 해킹시 A도 해킹 가능.
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int n = Integer.parseInt( token.nextToken() );
        int m = Integer.parseInt( token.nextToken() );
        for( int i = 0; i < n + 1; i ++ ){
            graph.add( new ArrayList<>() );
        }
        for( int i = 0; i < m; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int b = Integer.parseInt( token.nextToken() );
            int a = Integer.parseInt( token.nextToken() );
            graph.get( a ).add( b );
        }

        for( int i = 1; i < n + 1; i ++ ){
            Queue< Integer > q = new ArrayDeque<>();
            q.add( i );
            boolean visit[] = new boolean[ n + 1 ];
            visit[ i ] = true;
            int cnt = 1;
            while( !q.isEmpty() ){
                int pos = q.poll();

                for( int next : graph.get( pos ) ){
                    if( visit[ next ] == false ){
                        visit[ next ] = true;
                        cnt += 1;
                        q.add( next );
                    }
                }

            }
            if( cnt > Mx ){
                Mx = cnt;
                answer = new ArrayList<>();
                answer.add( i );
            }else if( cnt == Mx ){
                answer.add( i );
            }

        }

        Collections.sort( answer );

        for( int i: answer ){
            System.out.print( i + " " );
        }




    }
}