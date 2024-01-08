package J12865;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static ArrayList< int[] > arrlst = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int[] NK = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
        int [][] dp = new int[ NK[ 0 ] + 1 ][ NK[ 1 ] + 1 ];
        for( int i = 0; i < NK[ 0 ]; i ++ ) {
            int[] node = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
            int x = node[ 0 ];
            int y = node[ 1 ];
            ArrayList< Integer > row = new ArrayList<>();
            arrlst.add( new int[] { x, y } );
        }

        Collections.sort( arrlst, ( e1, e2 ) -> {
            if( e1[ 0 ] == e2[ 0 ] ) {
                return Integer.compare( e1[ 1 ], e2[ 1 ] );
            }
            return Integer.compare( e1[ 0 ], e2[ 0 ] );
        });


        for( int i = 1; i < NK[ 0 ] + 1; i++ ) {
            int[] row = arrlst.get( i - 1 );
            int w = row[ 0 ]; int v = row[ 1 ];
            for( int j = 0; j < NK[ 1 ] + 1; j++ ) {
                if( dp[ i ][ j ] < dp[ i - 1 ][ j ] ) {
                    dp[ i ][ j ] = dp[ i - 1 ][ j ];
                }

                if( j + w < NK[ 1 ] + 1 ) {
                    dp[ i ][ j + w ] =Math.max( dp[ i ][ j + w ], dp[ i - 1 ][ j ] + v );
                }


            }
        }


        System.out.println( dp[ NK[ 0 ] ][ NK[ 1 ] ] );






    }

}
//Show less
//
//amiva
//11:14 AM
//package workshoptest;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//
//import java.util.*;
//
//public class Main {
//    public static StringBuilder builder = new StringBuilder();
//    public static void main(String[] args) throws IOException {
//        // TODO Auto-generated method stub
//
//        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
//        int N =  Integer.parseInt( bf.readLine() );
//
//
//        permutations( N );
//
//        System.out.println( builder );
//
//    }
//
//
//    public static ArrayList< Integer > permutations( int n ) {
//
//        ArrayList< Integer > numlst = new ArrayList<>();
//
//        for( int i = 1; i < n + 1; i++ ) {
//            numlst.add( i );
//        }
//
//        Queue< Stack< Integer > > q = new LinkedList<Stack<Integer>>();
//
//        for( int i = 1; i < n + 1; i ++ ) {
//            Stack< Integer > row = new Stack<>();
//            row.add( i );
//            q.add( row );
//        }
//        while( !q.isEmpty() ) {
//
//            Stack< Integer > row = q.poll();
//
//            if( row.size() == n ) {
//                for( int r : row ) {
//                    builder.append( r + " " );
//                }
//                builder.append( "\n" );
//                continue;
//            }
//
//            for( int i = 1; i < n + 1; i ++ ) {
//                if( row.contains( i ) ) {
//                    continue;
//                }
//
//                Stack< Integer > temp = (Stack<Integer>) row.clone();
//                temp.add( i );
//                q.add( temp );
//
//
//            }
//
//
//
//        }
//
//
//
//        return null;
//
//    }
//
//}
//Show less
//
//amiva
//11:27 AM
//
//
//
//
//
//
//
//package workshoptest;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//
//import java.util.*;
////1463
//
//public class Main {
//    public static ArrayList< int[] > arrlst = new ArrayList<>();
//    public static void main(String[] args) throws IOException {
//        // TODO Auto-generated method stub
//
//        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
//        int[] NK = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
//        int [][] dp = new int[ NK[ 0 ] + 1 ][ NK[ 1 ] + 1 ];
//        for( int i = 0; i < NK[ 0 ]; i ++ ) {
//            int[] node = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
//            int x = node[ 0 ];
//            int y = node[ 1 ];
//            ArrayList< Integer > row = new ArrayList<>();
//            arrlst.add( new int[] { x, y } );
//        }
//
//        Collections.sort( arrlst, ( e1, e2 ) -> {
//            if( e1[ 0 ] == e2[ 0 ] ) {
//                return Integer.compare( e1[ 1 ], e2[ 1 ] );
//            }
//            return Integer.compare( e1[ 0 ], e2[ 0 ] );
//        });
//
//
//        for( int i = 1; i < NK[ 0 ] + 1; i++ ) {
//            int[] row = arrlst.get( i - 1 );
//            int w = row[ 0 ]; int v = row[ 1 ];
//            for( int j = 0; j < NK[ 1 ] + 1; j++ ) {
//                if( dp[ i ][ j ] < dp[ i - 1 ][ j ] ) {
//                    dp[ i ][ j ] = dp[ i - 1 ][ j ];
//                }
//
//                if( j + w < NK[ 1 ] + 1 ) {
//                    dp[ i ][ j + w ] =Math.max( dp[ i ][ j + w ], dp[ i - 1 ][ j ] + v );
//                }
//
//
//            }
//        }
//
//
//        System.out.println( dp[ NK[ 0 ] ][ NK[ 1 ] ] );
//
//
//
//
//
//
//    }
//
//}