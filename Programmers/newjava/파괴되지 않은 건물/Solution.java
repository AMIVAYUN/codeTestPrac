import java.util.*;
class Solution {
    /**

     누적합 근데 이제 열을 곁들인

     */
    int[][] memo;
    public int solution(int[][] board, int[][] skills ) {
        int answer = 0;
        int n = board.length; int m = board[ 0 ].length;
        memo = new int[ n + 1 ][ m + 1 ];
        /**

         x, y, x2, y2
         => (x,y), (x2+1,y), (x,y2+1), (x2+1,y2+1)

         */
        for( int[] skill : skills ){
            int type = skill[ 0 ];
            int x1 = skill[ 1 ];
            int y1 = skill[ 2 ];
            int x2 = skill[ 3 ];
            int y2 = skill[ 4 ];
            int degree = skill[ 5 ];

            if( type == 1 ){
                degree *= -1;
            }

            memo[ x1 ][ y1 ] += degree;
            memo[ x2 + 1 ][ y1 ] -= degree;
            memo[ x1 ][ y2 +1 ] -= degree;
            memo[ x2 + 1 ][ y2 + 1 ] += degree;
        }

        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m + 1; j ++ ){
                if( i > 0 ) memo[ i ][ j ] += memo[ i - 1 ][ j ];
                if( j > 0 ) memo[ i ][ j ] += memo[ i ][ j - 1 ];
                if( i > 0 && j > 0 ) memo[ i ][ j ] -= memo[ i - 1 ][ j - 1 ];
            }
        }



        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( memo[ i ][ j ] + board[ i ][ j ] > 0 ) answer++;
            }
        }


        return answer;
    }
}