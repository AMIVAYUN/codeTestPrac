package PM.선입선출스케쥴링;

import java.util.*;
import java.io.*;
class Solution {
    /**

     이거 전에 청룡이가 비슷한거 문제로 준 적 있다. 요점은 매회 cores를 순회하면 n**2의 손해가 나기에 우리는 무조건 이분탐색과 같이
     이 순회 성능을 개선하는 방향으로 접근해야 한다.
     */
    public int solution(int n, int[] cores) {
        int answer = 0;
        int k = findValue( n, cores );
        // System.out.println( k );
        int value = 0;
        int coreCount = cores.length;

        int sum = coreCount;
        if( k != 0 ){
            for( int core : cores ){
                sum += k / core;
            }
        }

        sum -= n;
        for( int i = cores.length - 1; i >= 0; i-- ){
            if ( k % cores[ i ] == 0) {
                if ( sum == 0 ) {
                    answer = i + 1;
                    break;
                }
                sum--;
            }
        }


        return answer;
    }

    //1개 10000시간 50000개 500000000 5억
    public int findValue( int n, int[] cores ){
        int lt = 0; int rt = 50000001;
        int returnValue = -1;
        while( lt <= rt ){

            int mid = ( lt + rt ) / 2;

            int sum = cores.length;

            if( mid != 0 ){
                for( int core : cores ){
                    sum += mid / core;
                }
            }

            // System.out.println(" mid : " + mid + "sum = " + sum );
            if( sum >= n ){
                rt = mid - 1;
                returnValue = mid;
            }else{
                lt = mid + 1;
            }
        }

        return returnValue;
    }
}