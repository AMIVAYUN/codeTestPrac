import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {

        long sum1 = 0l;
        long sum2 = 0l;

        int n = queue1.length;
        ArrayDeque< Integer > dq1 = new ArrayDeque<>();
        ArrayDeque< Integer > dq2 = new ArrayDeque<>();
        for( int i = 0; i < n; i ++ ){
            sum1 += queue1[ i ];
            sum2 += queue2[ i ];
            dq1.add( queue1[ i ] );
            dq2.add( queue2[ i ] );
        }

        queue1 = null;
        queue2 = null;

        int answer = 0;
        for( int i = 0; i < n * 4; i ++ ){
            if( sum1 == sum2 ){
                return answer;
            }else if( sum1 > sum2 ){
                int val = dq1.poll();
                sum1 -= val;
                sum2 += val;
                dq2.add( val );
            }else{
                int val = dq2.poll();
                sum2 -= val;
                sum1 += val;
                dq1.add( val );
            }
            answer++;
        }


        return -1;
    }
}