package PM.N으로_표현;

import java.util.*;
class Solution {
    /**

     연산으로 못 만드는 수 이어 붙이기. >> 따로 만들자.
     8보다 크면 -1? 이러면 n**2으로 돌려도 문제없다.
     사칙연산은 전에 것들 더해주면 된다.
     역이 성립하지 않는 사칙연산 -> 빼기 나누기.

     풀다보니 n**4 까지도 필수이다.

     수는 32000이하

     */
    public int solution(int N, int number) {
        int answer = 0;
        if( N == number ) return 1;

        ArrayList<Integer>[] nums = new ArrayList[ 9 ];

        for( int i = 0; i < 9; i ++ ){
            nums[ i ] = new ArrayList<Integer>();
            if( i > 0 ){
                int targetNum = makeNumberByLevel( N, i );
                nums[ i ].add( targetNum );
            }
        }

        // for( int i = 1; i < 9; i ++ ){
        //     System.out.println( nums[ i ].toString() );
        // }

        for( int i = 2; i < 9; i ++ ){
            for( int j = 1; j < i / 2 + 1; j ++ ){
                for( int num : nums[ i - j ] ){
                    for( int num2 : nums[ j ] ){
                        int plus = num + num2;
                        if( isRightNum( plus ) ) nums[ i ].add( plus );
                        int minus = num - num2;
                        if( isRightNum( minus ) ) nums[ i ].add( minus );
                        int minus2 = num2 - num;
                        if( isRightNum( minus2 ) ) nums[ i ].add( minus2 );
                        int multiple = num * num2;
                        if( isRightNum( multiple ) ) nums[ i ].add( multiple );
                        if( num != 0 ){
                            int division = num / num2;
                            if( isRightNum( division ) ) nums[ i ].add( division );
                        }
                        if( num2 != 0 ){
                            int division2 = num2 / num;
                            if( isRightNum( division2 ) ) nums[ i ].add( division2 );
                        }

                    }
                }
            }

            for( int result : nums[ i ] ) if( number == result ) return i;
        }

        return -1;
    }

    public int makeNumberByLevel( int N, int depth ){
        int start = 0;
        for( int i = 0; i < depth; i ++ ){
            if( i != 0 ) start *= 10;
            start += N;
        }

        return start;
    }

    public boolean isRightNum( int num ){
        return num >= 1 && num <= 32000;
    }
}