import java.util.*;
class Solution {
    public long solution(int[] weights1) {
        long answer = 0;
        Integer weights[] = new Integer[ weights1.length ];
        for( int i = 0; i < weights1.length; i ++ ){
            weights[ i ] = weights1[ i ];
        }
        Arrays.sort( weights, Collections.reverseOrder());
        HashMap< Double, Integer > map = new HashMap<>();
        for(int i : weights) {
            double a = i * 1.0;
            double b = ( i * 3.0 ) / 2.0;
            double c = i * 2.0;
            double d = i * 4.0/3.0;
            if(map.containsKey(a)) answer += map.get(a);
            if(map.containsKey(b)) answer += map.get(b);
            if(map.containsKey(c)) answer += map.get(c);
            if(map.containsKey(d)) answer += map.get(d);
            map.put( ( i * 1.0 ), map.getOrDefault( ( i * 1.0 ), 0 ) + 1);
        }

        return answer;
    }
}