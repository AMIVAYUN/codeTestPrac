import java.util.*;
class Solution {

    int answer, info[], edges[][];
    boolean[] visit;
    public int solution(int[] info, int[][] edges) {
        answer = 0;
        visit = new boolean[ info.length ];
        this.info = info;
        this.edges = edges;
        visit[ 0 ] = true;
        dfs( 1, 0 );

        return answer;
    }

    private void dfs( int sheep, int wolf ){
        if( sheep > wolf ){
            answer = Math.max( answer, sheep );
        }else{
            return;
        }

        for( int[] edge: edges ){
            int start = edge[ 0 ];
            int end = edge[ 1 ];

            if( visit[ start ] && !visit[ end ] ){
                visit[ end ] = true;
                if( info[ end ] == 1 ){
                    dfs( sheep , wolf + 1 );
                }else{
                    dfs( sheep + 1, wolf );
                }
                visit[ end ] = false;
            }


        }


    }
}