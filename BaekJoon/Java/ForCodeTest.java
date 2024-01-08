

import java.util.*;

public class ForCodeTest {

    //다중 조건 정렬
    public static void main( String[] args ){
        int cnt = 10;
        List< Test > lst = new ArrayList<>();
        for( int i = 1 ; i < 10; i++ ){
            Test n = new Test( i, cnt-- );
            lst.add( n );
        }

        System.out.println( lst.toString() );
        lst.sort( Comparator.comparing( Test::getB ).thenComparing( Test::getA ) );
        // 배열 다중 조건
        for( Test t : lst ){
            System.out.println( t.toString() );
        }

        int[][] array = { { 1, 5 }, { 2, 4 }, { 3, 3 }, { 4, 2 }, { 5, 1} };

        Arrays.sort( array, Comparator.comparingInt( (int[] o) -> o[ 1 ]  ).thenComparing( ( int[] o ) -> o[ 0 ]) );


        PriorityQueue< Integer > heap = new PriorityQueue<>();


        Queue< Integer > q = new LinkedList<>();



    }



    public static class Test{
        int a;
        int b;

        public Test( int a, int b ){
            this.a = a;
            this.b = b;
        }

        public int getA() {
            return a;
        }

        public int getB() {
            return b;
        }
        @Override
        public String toString(){
            return a + " " + b;
        }
    }

}

