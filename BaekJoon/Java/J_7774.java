package shop.ssafy9study.ssafy9study.configuration;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.*;
public class J_7774 {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        /**
         * 첫 번째 멀티탭은 표준 A 플러그를 사용 하고, 표준 B 콘센트를 여러 개 가지고 있다.
         두 번째 멀티탭은 표준 B 플러그를 사용 하고, 표준 A 콘센트를 여러 개 가지고 있다.
         *
         */
        //init
        BufferedReader bf = new BufferedReader( new InputStreamReader(System.in ) );
        int[] nm = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
        int n = nm[ 0 ]; int m = nm[ 1 ];

        int[] ns = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();
        int[] ms = Arrays.stream( bf.readLine().split( " " ) ).mapToInt( Integer::parseInt ).toArray();

        Arrays.sort( ms );
        Arrays.sort( ns );
        Queue< Integer > mq = new LinkedList();
        Queue< Integer > nq = new LinkedList();
        int sum = 0;
        //초기화 플러그는 하나



        if( ms.length == 0 || ns.length == 0 ) {
            System.out.println( 1 );
            return;
        }

//		nq.add( ns[ ns.length - 1 ] );




        //내림차순
        for( int i = ns.length - 1; i > -1; i -- ) {

            nq.add( ns[ i ] );
        }
        for( int i = ms.length - 1; i > -1; i -- ) {

            mq.add( ms[ i ] );
        }
        int aplug = 1; int bplug = 0;

        //solve

        int cnt = 0;
        //A플러그는 한개씩만 꽂고 B플러그는 최대한 많이 꽂는다.
        while( !mq.isEmpty() && cnt < 2) {


            while( bplug > 0 && !mq.isEmpty() ) {
                int next = mq.remove();
                aplug += next;
                bplug -= 1;
                cnt = 0;
            }

            if( !nq.isEmpty() && !mq.isEmpty() && bplug == 0 ) {
                int next = nq.remove();
                aplug -= 1;
                bplug += next;
            }
            cnt += 1;



        }

        System.out.println( aplug );






    }




}


