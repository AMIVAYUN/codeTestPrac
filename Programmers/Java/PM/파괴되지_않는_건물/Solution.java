package PM.파괴되지_않는_건물;

import java.util.*;
class Solution {
    /*
        이거 몇일 전에 한 x1 y1 x2 y2 시뮬 아닌가?
        -> 불가능 각 좌표가 가변적

        2차원 누적합 공식이 의미가 있나? 평소 하던대로 전부 순회를 해버리면 그럼 스킬을 전부 돌며 n * m * 250000을 다 돌아야 하는데? 흠...

        그렇다면 시작점에 + 막행 막점마다 - 를 넣으면 어떻게 될까? O( 2 ) * 2500000

        다 돌고 각 행에 대해 * n 이건 괜찮은 것 같은데?

        정확성  테스트
            테스트 1 〉	통과 (0.03ms, 78.9MB)
            테스트 2 〉	통과 (0.04ms, 71.5MB)
            테스트 3 〉	통과 (0.05ms, 76.7MB)
            테스트 4 〉	통과 (0.09ms, 73.5MB)
            테스트 5 〉	통과 (0.14ms, 95.4MB)
            테스트 6 〉	통과 (0.33ms, 75.8MB)
            테스트 7 〉	통과 (0.27ms, 79.6MB)
            테스트 8 〉	통과 (0.37ms, 80.3MB)
            테스트 9 〉	통과 (0.83ms, 72.2MB)
            테스트 10 〉	통과 (0.71ms, 79.5MB)
        효율성  테스트
            테스트 1 〉	실패 (시간 초과)
            테스트 2 〉	실패 (시간 초과)
            테스트 3 〉	실패 (시간 초과)
            테스트 4 〉	실패 (시간 초과)
            테스트 5 〉	실패 (시간 초과)
            테스트 6 〉	실패 (시간 초과)
            테스트 7 〉	실패 (시간 초과)
        채점 결과
        정확성: 53.8
        효율성: 0.0
        합계: 53.8 / 100.0


    */
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int n = board.length;
        int m = board[ 0 ].length;
        int[][] graph = new int[ n ][ m ];

        for( int[] oskill : skill ){
            int type = oskill[ 0 ], x1 = oskill[ 1 ], y1 = oskill[ 2 ], x2 = oskill[ 3 ], y2 = oskill[ 4 ], degree = oskill[ 5 ];
            graph[ x1 ][ y1 ] += type == 1 ? degree * -1 : degree;;
            if( y2 + 1 != m )   graph[ x1 ][ y2 + 1 ] -= type == 1 ? degree * -1 : degree;;
            if( x2 + 1 != n )   graph[ x2 + 1 ][ y1 ] -= type == 1 ? degree * -1 : degree;;
            if( x2 + 1 != n && y2 + 1 != m )    graph[ x2 + 1 ][ y2 + 1 ] += type == 1 ? degree * -1 : degree;;

            // //O( k * n )
            // for( int x = x1; x < x2 + 1; x ++ ){
            //     graph[ x ][ y1 ] += type == 1 ? degree * -1 : degree;
            //     if( y2 + 1 != m ){
            //         graph[ x ][ y2 + 1 ] += type == 1 ? degree : degree * -1;
            //     }
            // }
        }

        // //O( 2 * n^2 )
        // for( int x = 0; x < n; x ++ ){
        //     for( int y = 1; y < m; y ++ ){
        //         graph[ x ][ y ] = graph[ x ][ y ] + graph[ x ][ y - 1 ];
        //     }
        //     for( int y = 0; y < m; y ++ ){
        //         if( board[ x ][ y ] + graph[ x ][ y ] > 0 ) answer++;
        //     }
        // }



        // for( int x = 0; x < n; x ++ ){
        //     System.out.println( Arrays.toString( graph[ x ] ) );
        // }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i > 0) graph[ i ][ j ] += graph[ i - 1 ][ j ];
                if (j > 0) graph[ i ][ j ] += graph[ i ][ j - 1 ];
                if (i > 0 && j > 0) graph[ i ][ j ] -= graph[ i - 1 ][ j - 1 ];
            }
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[ i ][ j ] + graph[ i ][ j ] > 0) answer++;
            }
        }

        return answer;
    }
}