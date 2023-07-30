import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J_1182 {
    static int[] lst;
    static int ans = 0;
    static int N;
    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int[] arr = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
        N = arr[ 0 ]; int S = arr[ 1 ];

        lst = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();


        getResult( S, 0, 0 , false );
        if( S == 0 ){

        }
        System.out.println( ans );

    }

    public static void getResult( int S, int sum, int index, boolean isadded ){

        if( index == N ){
            if( sum == S && isadded ){
                ans += 1;
            }
            return;
        }



        getResult( S, sum + lst[ index ], index + 1, true );

        getResult( S, sum , index + 1, isadded || false );

    }
}
