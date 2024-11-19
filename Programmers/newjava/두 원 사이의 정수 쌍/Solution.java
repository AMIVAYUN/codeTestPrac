import java.lang.Math;

public class Solution {
    public static long solution(int r1, int r2) {
        long answer = 0;

        for (int i = 1; i <= r2; i++) {
            long lt = (long)Math.ceil(Math.sqrt(Math.max(0, (long)r1 * r1 - (long)i * i)));
            long rt = (long)Math.floor(Math.sqrt((long)r2 * r2 - (long)i * i));

            answer += (rt - lt + 1) * 4;
         
        }


        return answer;
    }
}