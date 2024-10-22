package PersonalStudy;

import java.util.*;

public class CollectionStudy {
    public static void main(String[] args) {
        Set set = new HashSet();
//        Map map = new HashMap();
        HashMap map = new HashMap();
        HashSet hset = new HashSet();
        int[][] arr = new int[][]{ { 1, 10 }, { 7,9 }, { 6, 8 } ,{ 10, 10 } };
        Arrays.sort( arr, ( e1, e2 ) -> {

            return Integer.compare( e1[ 0 ], e2[ 0 ] );
        } );
        Arrays.sort( arr, ( e1, e2 ) -> {

            return Integer.compare( e2[ 1 ], e1[ 1 ] );
        } );
        for( int[] ar : arr ){
            System.out.println( Arrays.toString( ar ) );
        }
    }
}
