import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.io.*;
import java.util.*;

public class J_16198 {

    public static HashMap< String, Integer > map = new HashMap<>();
    public static int k = 0;
    public static List< Integer > Ns;

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int N = Integer.parseInt( bf.readLine() );

        Ns = Arrays.stream( bf.readLine().split( " " ) ).map( Integer::parseInt ).collect(Collectors.toList());




        dfs( N, 0 );

//        for( String key: map.keySet() ) {
//            int val = map.get( key );
//            System.out.println( key + " " + val );
//        }
        System.out.println( k );



    }



    public static void dfs( int N,int sum ) {
//        System.out.println( "route:"+ route + "sum: " + sum
//                );
//        for( int i : Ns ) {
//            System.out.print( i + " ");
//        }
        int n = N;
//        System.out.println();
        if( N == 2 ) {
            k = Math.max( k, sum );
            return;
        }
        /*String route_ = new String( route );*/
        for( int i = 1; i < n - 1; i ++ ) {

            int val = Ns.get( i );

            /*int check = map.getOrDefault(route, 0 );*/
            /*if( route.contains( String.valueOf( val ) ) && check > sum  ){
                continue;
            }
            route_ += String.valueOf( val );*/
            /*int bias = map.getOrDefault(route_, 0);*/
            int prev = Ns.get( i - 1);
            int next = Ns.get( i + 1 );
//            if( bias < prev * next + sum ) {
            /*map.put( route_, prev * next + sum );*/
//                System.out.println( "target index: " + i + " value: " + val );
            Ns.remove( i );
            dfs( N - 1,/* route_,*/ sum + prev * next );
//                route_ = route_.substring( 0, route_.length() -1 );
            Ns.add( i, val );

//            }



        }

    }

}