import java.util.*;
import java.io.*;

public class J_17609 {
    public static boolean isPseudo( char[] array, int lt, int rt ){

        while( lt <= rt ){
            if( array[ lt ] != array[ rt ] ){
                return false;
            }
            lt += 1; rt -= 1;
        }

        return true;
    }
    public static int isPalin( char[] array ){
        int length = array.length;

        int lt = 0; int rt = length - 1;

        while( lt <= rt ){

            if( array[ lt ] == array[ rt ] ){
                lt += 1; rt -= 1;

            }
            else{
                if( isPseudo( array, lt + 1 , rt ) | isPseudo( array, lt, rt - 1 ) ){
                    return 1;
                }else{
                    return 2;
                }
            }
        }

        return 0;
    }
    public static void main( String[] args ) throws IOException {

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        int T = Integer.parseInt( bf.readLine() );

        for( int i = 0; i < T; i++ ){
            char[] str0 = bf.readLine().toCharArray();
            System.out.println( isPalin( str0 ));
        }
    }
}
