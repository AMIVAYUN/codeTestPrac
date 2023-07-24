import java.io.*;
import java.nio.Buffer;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static HashMap< String, Integer > map = new HashMap<>();


    public static void main( String[] args ) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
        while( sc.hasNextLine() ){
            String s = sc.nextLine();
            int val = map.getOrDefault( s , 0 );

            val += 1;
            map.put( s, val );

        }


        if( map.size() > 0 ){
            Object[] keys = map.keySet().stream().map( String::new ).toArray();
            Arrays.sort( keys );
            int sum = 0;
            for( Object key : keys ){
                int val = map.get( key );
                sum += val;
            }


            for( Object key : keys ){
                int val = map.get( key );

                System.out.printf( "%s %.4f\n", (String )key, ( (double)val / sum * 100 ) );
            }


        }


    }
}