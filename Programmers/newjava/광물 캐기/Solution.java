import java.util.*;
class Solution {
    int n;
    int k;
    int mx;
    int[][] graph = new int[][]{ {1, 1, 1 }, { 5, 1, 1 }, {25, 5, 1}};
    int Mn = Integer.MAX_VALUE;
    int[] mins, picks;
    public int solution(int[] picks, String[] minerals) {
        n = 0;
        k = minerals.length;
        this.picks = picks;
        for( int i = 0; i < 3; i ++ ){
            n += picks[ i ];
        }
        mins = new int[ k ];

        for( int i = 0; i < k; i ++ ){
            mins[ i ] = 0;
            if( minerals[ i ].equals( "iron") ){
                mins[ i ] = 1;
            }else if( minerals[ i ].equals( "stone" ) ){
                mins[ i ] = 2;
            }

        }

        int answer = 0;

        /**

         다이아, 철, 돌 각각 0~5개

         철 -> 다이아 캘 때 피로도 5, 철과 돌 1
         각 곡괭이는 광물 5개를 캐고는 사용할 수 없다.

         최소한의 피로도로 광물을 캐려고 한다.

         한번 사용하면 끝까지

         주어진 순서대로만 광물을 캔다.

         더 사용할 곡괭이 x or 모든 광물 캘때 까지

         */

        dfs( 0, 0, 0 );

        return Mn;
    }

    void dfs( int depth, int val, int minIdx ){
        if( Mn < val ){
            return;
        }

        if( depth == n || minIdx == k ){
            Mn = val;
            return;
        }



        for( int i = 0; i < 3; i ++ ){
            if( picks[ i ] < 1 ) continue;
            picks[ i ]--;
            int sub = 0;
            int j = 0;
            for( j = 0; j < 5; j ++ ){
                if( minIdx + j == k ){
                    break;
                }

                sub += graph[ i ][ mins[ minIdx + j ] ];

            }

            dfs( depth + 1, val + sub, minIdx + j );
            picks[ i ]++;

        }
    }
}