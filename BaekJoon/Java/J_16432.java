import java.io.*;
import java.util.*;
public class J_16432 {
    public static int[][] visit;
    public static int N;
    public static boolean flag = false;
    public static HashMap< Integer, int[] > map;
    public static void dfs( int day, Stack< Integer > stack ){
        if( flag ){
            return;
        }
        if( day == N ){

            for( int i : stack ){
                System.out.println( i );
            }
            flag = true;
            return;
        }

        int[] today = map.get( day );

        for( int rice : today ){
            if( visit[ day ][ rice ] > 0 ){
                continue;
            }
            if( !stack.isEmpty() && stack.peek() == rice ){
                continue;
            }
            stack.add( rice );
            visit[ day ][ rice ] = 1;
            dfs( day + 1, stack );
            stack.pop();
        }


    }
    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        N = Integer.parseInt( bf.readLine() );
        visit = new int[ N ][ 10 ];
        map = new HashMap<>();

        for( int i = 0; i < N; i++ ){

            String[] arg = bf.readLine().split( " " );

            Integer[] lst = Arrays.stream(arg).map( Integer::parseInt ).toArray( Integer[]::new );
            int[] dayRice = new int[ lst[ 0 ] ];

            for( int j = 0; j < lst[ 0 ]; j ++ ){
                dayRice[ j ] = lst[ j + 1 ];
            }

            map.put( i , dayRice );


        }

        Stack< Integer > stack = new Stack<>();
        dfs( 0, stack );

        if( !flag ){
            System.out.println( -1 );
        }
    }
}
