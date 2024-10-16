import java.util.*;
class Solution {
    /**

     r,c n개의 포인트 각 포인트 1~n 까지 서로 다른 번호

     운송경로 -> m개의 포인트로 구성 할당된 순서대로

     로봇은 x대 모두 0초에 동시 출발

     1초마다 상하좌우 한칸씩

     r좌표가 변하는 이동 << c좌표보다 먼저 이동

     운송 마치면 물류 센터 벗어남.

     같은 좌표에 2대이상 모이면 충돌 가능성 ->

     */
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;

        ArrayDeque< int[] > dq = new ArrayDeque<>();
        int[][][] mapper = new int[ 20001 ][ 101 ][ 101 ];
        for( int[] route: routes ){
            int n = route.length;
            int i = 1;
            int[] start = points[ route[ 0 ] - 1 ];
            int x = start[ 0 ];
            int y = start[ 1 ];
            int time = 1;
            int[] end = points[ route[ 1 ] - 1 ];
            // System.out.println( Arrays.toString( start ) + " " + Arrays.toString( end ) );
            mapper[ 0 ][ x ][ y ] ++;
            if( mapper[ 0 ][ x ][ y ] == 2 ){

                answer++;
            }
            while( i < n ){
                // System.out.println( route + " " + x + " " + y + " " + time);
                if( x != end[ 0 ] ){
                    int dx = end[ 0 ]  - x > 0 ? 1 : -1;
                    x += dx;
                }else{
                    int dy = end[ 1 ] - y > 0 ? 1 : -1;
                    y += dy;
                }
                mapper[ time ][ x ][ y ]++;
                if( mapper[ time++ ][ x ][ y ] == 2 ){
                    answer++;
                    // System.out.println( time + " " + x + " " + y + "here");
                }

                if( x == end[ 0 ] && y == end[ 1 ] ){
                    i++;
                    if( i < n ){
                        end = points[ route[ i ] - 1 ];
                    }
                }

            }
        }

//         int[][] mapper;
//         while( !dq.isEmpty() ){
//             int n = dq.size();
//             mapper = new int[ 101 ][ 101 ];
//             for( int i = 0; i < n; i ++ ){
//                 int[] now = dq.poll();
//                 int x = now[ 0 ];
//                 int y = now[ 1 ];
//                 int remainX = now[ 2 ];
//                 int remainY = now[ 3 ];

//                 mapper[ x ][ y ] ++;
//                 if( mapper[ x ][ y ] == 2 ){
//                     answer++;
//                 }

//                 if( remainX == 0 && remainY == 0 ) continue;

//                 if( remainX == 0 ){
//                     if( remainY < 0 ){
//                         dq.add( new int[]{ x, y - 1, remainX, remainY + 1 });
//                     }else{
//                         dq.add( new int[]{ x, y + 1, remainX, remainY - 1 });
//                     }
//                 }else{
//                     if( remainX < 0 ){
//                         dq.add( new int[]{ x - 1, y, remainX + 1, remainY });
//                     }else{
//                         dq.add( new int[]{ x + 1, y, remainX - 1, remainY });
//                     }
//                 }

//             }
//         }


        return answer;
    }
}