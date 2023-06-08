import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class J_11403 {

    public static int[] bfs( ArrayList< ArrayList< Integer > > graph, int n, int idx ){
        int[] visit = new int[ n ];
        Queue< Integer > q = new LinkedList<>();

        for( int i: graph.get( idx ) ){
            q.add( i );
            visit[ i ] = 1;
        }

        while ( !q.isEmpty() ){
            int next = q.remove();

            for( int next_ : graph.get( next ) ){
                if( visit[ next_ ] == 0 ){
                    visit[ next_ ] = 1;
                    q.add( next_ );
                }
            }
        }






        return visit;
    }



    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in) );
        int n = Integer.parseInt( bf.readLine() );
        ArrayList< ArrayList< Integer > > graph = new ArrayList<>();

        for( int i = 0; i < n; i ++ ){
            String[] str0 = bf.readLine().split( " " );
            graph.add( new ArrayList<>() );
            ArrayList<Integer> now = graph.get( i );
            int[] arr = Arrays.stream(str0).mapToInt( Integer::parseInt ).toArray();

            for( int j = 0 ; j < n; j ++ ){
                if( arr[ j ] == 1 ){
                    now.add( j );
                }
            }

        }
        int[][] answer = new int[ n ][ n ];

        for( int i = 0; i < n; i ++ ){
            answer[ i ] = bfs( graph, n, i );
        }






        for( int[] row : answer ){
            for( int r: row ){
                System.out.print( r + " ");
            }
            System.out.println();
        }






    }




}
