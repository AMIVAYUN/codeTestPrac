import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class J_1253 {
    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int N = Integer.parseInt( bf.readLine() );
        int answer = 0;
        String[] lst = bf.readLine().split(" ");
        Integer[] nums = Arrays.stream(lst).map( Integer::parseInt ).toArray( size -> new Integer[ size ] );
        Arrays.sort( nums );
        for( int i = 0; i < N; i ++ ){

            int left, right;

            left = 0;
            right = N - 1;

            while( left < right ){

                if( left == i ){
                    left += 1;
                    continue;
                }else if( right == i ){
                    right -= 1;
                    continue;
                }
                Integer sum_ =  nums[ left ] + nums[ right ];
                if( sum_.equals( nums[ i ] ) ){

                    answer += 1;
                    break;
                }
                else if( sum_ > nums[ i ] ){
                    right -= 1;
                }else{
                    left += 1;
                }



            }



        }

        System.out.println( answer );
    }
}
