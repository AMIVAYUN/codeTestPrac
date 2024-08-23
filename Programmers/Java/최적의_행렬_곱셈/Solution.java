package 최적의_행렬_곱셈;

class Solution {
    /**
     과거에 비슷한 걸 풀어봤던 경험이 있다.
     dp로 [i][j]는 i~j까지 행렬 곱 최소 수를 담으며 앞에 인덱스 부터 차례대로 계산해나가자.

     */
    public int solution(int[][] matrix_sizes) {
        int answer = 0;
        int n = matrix_sizes.length;
        int dp[][] = new int[ n ][ n ];

        for( int cnt = 0; cnt < n - 1; cnt ++ ){
            for( int i = 0; i < n - 1 - cnt; i ++ ){
                int j = i + cnt + 1;
                dp[ i ][ j ] = Integer.MAX_VALUE;
                for( int k = i; k < j; k ++ ){
                    dp[ i ][ j ] = Math.min( dp[ i ][ j ], dp[ i ][ k ] + dp[ k+1 ][ j ] + matrix_sizes[ i ][ 0 ] * matrix_sizes[ k ][ 1 ] * matrix_sizes[ j ][ 1 ] );
                }

            }
        }

        return dp[ 0 ][ n - 1 ];
    }
}
