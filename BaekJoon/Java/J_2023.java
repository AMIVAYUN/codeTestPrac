import java.io.*;
import java.util.*;

public class J_2023 {
    /**
     * 문제
     * 수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
     * 7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다!
     * 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
     * 수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.
     *
     *
     * 오름차순 >> 0 부터 반복문 진행
     */
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    //첫째 자리는 무조건 소수여야 한다. // 조건
    static int[] firstPrime = { 2, 3, 5, 7 };

    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        /**
         * 입출력 받기
         */
        int n = Integer.parseInt( bf.readLine() );


        /**
         * 수 계산하기
         */
        for( int i = 0; i < firstPrime.length; i++ ) {
            getNum2( n, firstPrime[ i ], 1 );
        }


    }

    static void getNum2( int n, int num, int len ){
        if( len == n ){
            System.out.println( num );
            return;
        }

        num *= 10;
        for( int i = 0; i < 10; i ++ ){
            int next = num + i;

            if( isPrime( next ) ){
                getNum2( n, next, len + 1 );
            }
        }

    }
    //주어진 소수에 맞춰서 계산
    static void getNum( int n, int num ) {
        Queue< int[] > q = new LinkedList<>();

        q.add( new int[] { 1, num } );

        while( !q.isEmpty() ) {

            int[] now = q.poll();
            int len = now[ 0 ];
            int number = now[ 1 ];

            if( len == n ) {
                System.out.println( number );
                continue;
            }

            // 다음 수
            number *= 10;

            for( int i = 0; i < 10; i ++ ) {
                int next = number + i;
                if( isPrime( next ) ) {
                    q.add( new int[] { len + 1, next } );
                }
            }

        }


    }
    // 소수 판별하기
    public static boolean isPrime( int n ) {

        for( int i = 2; i < ( Math.sqrt( n ) + 1 ); i++ ) {
            if( n % i == 0 ) {
                return false;
            }
        }


        return true;
    }

}
