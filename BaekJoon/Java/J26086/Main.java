package J26086;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int context = 0;
    static int n,q,k;

    /**
     *
     * @param args
     * @throws IOException
     *
     * $0 p$: 고유번호가
     * $p$인 업무를 스케줄러에 추가한다. 특별히 다른 명령이 없는 한, 새로 추가된 일은 스케줄러 상의 맨 앞에 추가된다. 즉, 고유번호 값에 상관없이 스케줄러에서 가장 먼저 처리되어야 하는 업무가 된다.
     *
     * $1$: 스케줄러에 들어있는 업무를 고유번호 값 기준으로 오름차순으로 정렬한다. 이 결과, 고유번호 값이 낮은 업무일수록 스케줄러의 앞에 배치된다.
     *
     * $2$: 스케줄러에 있는 업무 처리 순서를 뒤집는다. 즉, 스케줄러에 들어가 있는 업무들의 처리 순서가 반대가 된다.
     *
     * reverse =>   t t // f
     *              t f // t
     *              f t // t
     *              f f // f
     *
     *              즉 XOR연산
     *
     *              0이면 child가 뒤에 붙고
     *              1이면 child가 앞에 붙음
     */
    static int size = 0;
    static boolean counter[];


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        q = Integer.parseInt( token.nextToken() );
        k = Integer.parseInt( token.nextToken() );

        counter = new boolean[ n + 1 ];

        ArrayDeque< Integer > dq = new ArrayDeque<>();
        int pos = 0;

        for( int i = 0; i < q; i ++ ) {
            token = new StringTokenizer(bf.readLine());
            if (token.countTokens() == 1) {
                int cmd = Integer.parseInt(token.nextToken());
                if( cmd == 1 ){

                    while( !dq.isEmpty() ){
                        int value = dq.poll();
                        counter[ value ] = true;
                        size++;
                    }

                    dq.add( 0 );
                    context = 0;

                }else{
                    context ^= 1;
                }
            } else {
                token.nextToken();
                //정순
                if( context == 0 ){
                    dq.addFirst( Integer.parseInt( token.nextToken() ) );
                }else{
                    dq.addLast( Integer.parseInt( token.nextToken() ) );
                }
            }
        }

        int cnt = 1;
        int ans = context == 0 ? dq.peek() : dq.peekLast();
        System.out.println(dq.toString());
        while( cnt <= k ){
            int value = context == 0 ? dq.poll() : dq.pollLast();
//            System.out.println( cnt + " " + value );
            if( value == 0 ){
                int temp = context == 0 ? 1 : n ;
                while( temp < ( n + 1 ) && temp > 0 && cnt <= k  ){
//                    System.out.println( temp + " " + counter[ temp ] + cnt );
                    if( counter[ temp ] ){
                        ans = temp;
                        cnt ++;
                    }
                    temp += context == 0 ? 1 : -1;
                }
            }else{
                ans = value;
                cnt++;
            }

        }


        System.out.println( ans );
    }


}