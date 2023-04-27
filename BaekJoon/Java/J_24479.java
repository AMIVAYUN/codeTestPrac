import java.util.ArrayList;
import java.util.*;
import java.io.*;
public class J_24479 {

    public static void main( String[] args ) throws Exception{

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        String[] str0 = bf.readLine().split(" ");

        int N, R, root;

        N = Integer.parseInt(str0[ 0 ] );
        R = Integer.parseInt( str0[ 1 ] );
        root = Integer.parseInt( str0[ 2 ] );
        int[] visit = new int[ N + 1 ];
        ArrayList< ArrayList<Integer>> graph_2d = new ArrayList<>();

        for( int i = 0; i < N + 1; i++){
            graph_2d.add( new ArrayList<>() );
        }

        for( int i = 0; i < R; i ++ ){
            String[] next = bf.readLine().split( " " );
            int A = Integer.parseInt( next[ 0 ] ); int B = Integer.parseInt( next[ 1 ] );
            ArrayList<Integer> Alst, Blst;
            Alst = graph_2d.get( A );
            Blst = graph_2d.get( B );

            Alst.add( B );
            Blst.add( A );

        }

        Stack< Integer > stack = new Stack<>();

        int count = 1;
        stack.add( root );

        while( !stack.isEmpty() ){
            int now = stack.pop();

            if( visit[ now ] > 0){
                continue;
            }

            visit[ now ] = count++;

            ArrayList< Integer > nexts = graph_2d.get( now );
            Collections.sort( nexts, Collections.reverseOrder());
            for( int next : nexts ){
                if( visit[ next ] < 1 ){
                    stack.add( next );
                }
            }
        }


        for( int idx = 1; idx < visit.length; idx ++ ){
            System.out.println( visit[ idx ] );
        }

    }
}
