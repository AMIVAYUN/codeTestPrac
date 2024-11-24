import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int num = 1;
        Stack< Integer > stack = new Stack();
        while( num <= order.length ){
            int next = order[ answer ];
            if( !stack.isEmpty() && stack.peek() == next ){
                stack.pop();
                answer++;
                continue;
            }

            if( next == num ){
                num ++;
                answer++;
            }else{
                stack.add( num );
                num++;
            }
        }

        while( !stack.isEmpty() && stack.peek() == order[ answer ] ){
            stack.pop();
            answer++;
        }
        return answer;
    }
}