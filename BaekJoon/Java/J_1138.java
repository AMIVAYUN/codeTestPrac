import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collectors;

class Main{
    static HashMap< Integer, ArrayList<Integer> > map = new HashMap<>();
    static Stack< Integer > stack = new Stack<>();
    static int[] visit;

    static boolean flag = false;

    public static void main( String[] args ) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        int N = Integer.parseInt( bf.readLine() );
        int[] lst = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
        ArrayList< Integer > result = new ArrayList<>();
        result.add( N );
        for( int i = N - 1; i > 0; i -- ){
            int cnt = lst[ i - 1 ];
            int temp = 0;
            if( temp == cnt ){
                result.add( 0, i );
                continue;
            }
            for( int j = 0; j < result.size(); j ++ ){
                int k = result.get( j );
                if( k > i ){
                    temp++;
                }

                if( temp == cnt ){
                    result.add( j + 1, i );
                    break;
                }


            }


        }

        StringBuilder builder = new StringBuilder();
        for( int i : result ){
            builder.append( i + " " );
        }
        System.out.println( builder);





    }









}