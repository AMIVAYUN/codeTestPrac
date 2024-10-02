import java.io.*;
import java.util.*;
class Solution {

    public int solution(int[] stones, int k) {
        int Mx = 0;
        int answer = 0;
        int n = stones.length;
        for( int i = 0; i < n; i ++ ){
            Mx = Math.max( stones[ i ], Mx );
        }

        int lt = 1; int rt = Mx;

        while( lt <= rt ){

            int mid = ( lt + rt ) / 2;

            int cnt = 0;

            for( int i = 0; i < n; i++ ){
                if( stones[ i ] < mid ){
                    cnt++;
                }else{
                    cnt = 0;
                }
                if( cnt >= k ){
                    break;
                }

            }

            if( cnt >= k ){
                rt = mid - 1;
            }else{
                lt = mid + 1;
                answer = mid;
            }

            // System.out.println( mid + ", " + cnt );

        }

        return answer;
    }
}