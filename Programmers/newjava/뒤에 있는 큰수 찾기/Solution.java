import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[ numbers.length ];

        Stack< int[] > nums = new Stack<>();
        nums.add( new int[]{ numbers[ 0 ], 0 } );

        for( int i = 1; i < numbers.length; i ++ ){
            while( !nums.isEmpty() && nums.peek()[ 0 ] < numbers[ i ] ){
                int[] num = nums.pop();
                answer[ num[ 1 ] ] = numbers[ i ];
            }
            nums.add( new int[]{ numbers[ i ], i } );
        }

        while( !nums.isEmpty() ){
            int[] num = nums.pop();
            answer[ num[ 1 ] ] = -1;
        }

        return answer;
    }
}