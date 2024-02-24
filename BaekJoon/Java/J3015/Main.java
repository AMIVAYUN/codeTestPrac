package J3015;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n;
    static long cnt;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );
        Person[] people = new Person[ n ];
        for( int i = 0; i < n; i ++ ) {
            people[ i ] = new Person( Integer.parseInt( bf.readLine() ) );
        }

        ArrayDeque< Person > dq = new ArrayDeque<>();


        for( int i = 0; i < n; i ++ ){
            //            System.out.println("now : " + people[ i ] );
            //            System.out.println( cnt + " " + dq.toString() );
            while( !dq.isEmpty() &&  dq.peekLast().stature <= people[ i ].stature ){
                //                System.out.println( dq.peekLast() + " " + people[ i ].stature );
                Person p = dq.pollLast();
                if( p.stature == people[ i ].stature ){
                    //                    people[ i ].cnt++; 더 반복될 수 있음

                    people[ i ].cnt += p.cnt;
                }
                cnt += p.cnt;


            }
            if( !dq.isEmpty() ){
                cnt ++;
            }

            dq.add( people[ i ] );
            //            System.out.println( cnt + " " + dq.toString() );

        }

        System.out.println( cnt );

    }

    static class Person{
        int stature;
        int cnt;

        public Person(int stature) {
            this.stature = stature;
            this.cnt = 1;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "stature=" + stature +
                    ", cnt=" + cnt +
                    '}';
        }
    }

}