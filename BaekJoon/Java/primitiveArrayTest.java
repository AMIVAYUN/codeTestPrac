import java.util.Arrays;

public class primitiveArrayTest {
    public static void main( String[] args ){
        int[] a = new int[ 5 ];

        int[] b = new int [ 5 ];

        for( int i = 1; i < 6; i++ ){
            a[ i - 1 ] = i;
        }

        b = a;

        a[ 0 ] = 3;

        Arrays.stream(b).forEach( S -> System.out.println( S ) ); // 즉 자바에서 PRIMITIVE TYPE 배열도 -> 객체 이다.
    }
}
