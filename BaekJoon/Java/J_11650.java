import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class J_11650 {
    public static ArrayList< int[] > lst;
    public static int N;



    public static void main( String[] args ) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        lst = new ArrayList<>();
        N = Integer.parseInt(bf.readLine());
        for( int i = 0; i < N; i ++ ){
            int[] abs= Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt).toArray();
            int a = abs[ 0 ];
            int b = abs[ 1 ];
            int[] next = { a, b };
            lst.add( next );
        }
        Collections.sort( lst, (a, b ) -> {
            if( a[ 0 ] == b[ 0 ] ){
                return Integer.compare( a[ 1 ], b[ 1 ] );
            }
            return Integer.compare( a[ 0 ], b[ 0 ] );
        });

        for( int[] val: lst ){
            int x = val[ 0 ]; int y = val[ 1 ];
            System.out.println( x + " " + y );
        }
    }
}
