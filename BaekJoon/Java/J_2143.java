import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

public class J_2143 {

    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        long T = Integer.parseInt( bf.readLine() );

        int N = Integer.parseInt( bf.readLine() );
        ArrayList< Long > A = (ArrayList<Long>) Arrays.stream(bf.readLine().split(" ")).map(i -> Long.parseLong( i ) ).collect(Collectors.toList());
        long[] a = A.stream().filter( i -> i != null ).mapToLong( i -> i ).toArray();
        int M = Integer.parseInt( bf.readLine() );
        ArrayList< Long > B = (ArrayList<Long>) Arrays.stream(bf.readLine().split(" ")).map(i -> Long.parseLong( i ) ).collect(Collectors.toList());
        long[] b = B.stream().filter( i -> i != null ).mapToLong( i -> i ).toArray();


        long[] prefix_A = new long[ N + 1 ];
        long[] prefix_B = new long[ M + 1 ];
        prefix_A [ 0 ] = 0;
        prefix_B [ 0 ] = 0;


        for( int idx = 1; idx < N + 1 ; idx ++ ){
            prefix_A[ idx ] = prefix_A[ idx - 1 ] + a[ idx - 1 ];
        }
        for( int idx = 1; idx < M + 1 ; idx ++ ){
            prefix_B[ idx ] = prefix_B[ idx - 1 ] + b[ idx - 1 ];
        }


        HashMap< Long, Long > map = new HashMap<>();

        for( int i = 0; i < N; i ++ ){

            for( int obj = i + 1; obj < N + 1 ; obj++ ){
                Long target = prefix_A[ obj ] - prefix_A[ i ];
                Long cnt = map.getOrDefault( target, new Long( 0 ) );

                map.put( target, cnt + 1 );
            }
        }

        int answer = 0;
        for( int i = 0; i < M; i ++ ) {

            for (int obj = i + 1; obj < M + 1; obj++) {

                Long target = prefix_B[ obj ] - prefix_B[ i ];
                Long acnt = map.getOrDefault( T - target, new Long( 0 ) );

                answer += acnt;



            }
        }
        System.out.println( answer );
    }
}
