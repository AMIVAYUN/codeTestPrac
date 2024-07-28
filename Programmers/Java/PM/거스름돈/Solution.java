package PM.거스름돈;

class Solution {
    /**
     n 원을 줄 때 방법의 경우의 수

     5원을 거슬러 줘야 하고 1 2 5 원 있으면 각 금액의 수에 맞게 거스름돈을 만드는 경우의 수를 구할 것.
     dp다

     */
    int[] dp;
    public int solution(int n, int[] money) {
        int answer = 0;
        dp = new int[ n + 1 ];
        dp[ 0 ] = 1;
        for( int m : money ){
            for( int i = m; i <= n ; i ++ ){
                dp[ i ] += dp[ i - m ];
            }
        }


        // System.out.println( Arrays.toString( dp ) );

        return dp[ n ];
    }
}