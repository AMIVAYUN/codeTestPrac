package J1946;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class MyOldCode {
	public static void main( String[] args ) throws Exception{
        Scanner sc = new Scanner( System.in );
        int T = sc.nextInt();

        for( int i = 0; i < T; i ++ ){
            int b = sc.nextInt();

            List< Integer[] > members = new ArrayList< Integer[] >();


            for( int j = 0; j < b; j ++ ){

                int idx0, idx1;
                idx0 = sc.nextInt();
                idx1 = sc.nextInt();

                Integer[] next = new Integer[2];

                next[ 0 ] = idx0;
                next[ 1 ] = idx1;

                members.add( next );





            }

            Collections.sort(members, new Comparator<Integer[]>() {
                @Override
                public int compare(Integer[] o1, Integer[] o2) {
                    return o1[ 0 ] - o2[ 0 ];
                }
            });
            int answer = 1;
            Integer[] start = members.remove( 0 );
            

            
            int Min = start[ 1 ];
            for( Integer[] l : members ){
                if( Min > l[ 1 ] ){
                    Min = l[ 1 ];
                    answer += 1;
                }
            }

            System.out.println( answer );



        }




    }
}
