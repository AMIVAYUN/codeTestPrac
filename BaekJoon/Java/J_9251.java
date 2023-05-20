import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class J_9251 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in) );
        String s1 = bf.readLine();
        String s2 = bf.readLine();

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();


        int length1 = s1.length();
        int length2 = s2.length();

        int[][] dp = new int[ length1 + 1 ][ length2 + 1 ];

        for( int i = 1; i < length1 + 1; i++ ){
            for( int j = 1; j < length2 + 1; j++ ){
                if( arr1[ i - 1 ] == arr2[ j - 1 ] ){
                    dp[ i ][ j ] = dp[ i - 1 ][ j - 1 ] + 1;
                }else{
                    dp[ i ][ j ] = Math.max( dp[ i - 1 ][ j ], dp[ i ][ j - 1 ] );
                }

            }


        }

        System.out.println( dp[ length1 ][ length2 ]);


    }




}
