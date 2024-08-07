package PM.공_이동_시뮬레이션;

class Solution {
    /**

     정순 -> n * m 의 모든 점을 찾아야 한다.
     역순 -> x, y에서 분기해서 해당 점들만 찾아주면 된다.

     n과 m이 10의 9승인데 n**2 한 로직으로 풀면 무조건 아웃일 것.

     20만개의 쿼리 기준 단방에 끝낼 방법을 찾아야 할 것 같다.
     좌표점 분기를 해버리면 뎁스상 아웃이 나는게 당연하닫.

     어제 푼 문제 처럼 직관적으로 봐보자.

     상하좌우로 움직임 -> 거기에 맞는 좌표 결과로 이동한다.

     0,0 0,1
     1,0 1,1

     이렇게 있으면 만약 쿼리가 우 한칸 아래 한칸이면

     격자를 벗어나지만 결국 결과는 직사각형이다.

     즉 특정 좌표들이 쿼리를 타고 결과를 나타낸다 한들 만약 그래프가 무한대라 가정하면 결국 넓이는 같고,

     벽이 있기에 이러한 점들이 모인다고 했을 때 이 또한 직사각형일 수 밖에 없다. -> ( 상하 좌우로 움직이는 대칭성 )

     거꾸로 간다고 가정했을 때 x, y에 모인 특정 결과 점들이 점점 다시 쿼리를 타고 원 위치로 가면 이 또한 직사각형이다.

     3*3 행렬에서 0,0 에서 도착지 0,2로 간다고 생각을 했을 때
     마지막 쿼리가 우로 2칸, 우로 3칸에 따라 가지수가 달라진다.

     우로 2칸은 그대로 움직이는 것이지만
     우로 3칸은 사이에 모든 점들도 가능성이 생긴다.

     단 이는 도착지가 끝점이라는 가정하이다.

     즉 내가 체크해야 할 것은

     끝점 일때, 원래 쿼리가 증가라면 그때가 바로 직사각형이 넓어지는 구간인 것.

     */
    public long solution(int n, int m, int x, int y, int[][] queries) {
        int x1 = x, y1 = y, x2 = x, y2 = y;

        for( int i = queries.length - 1; i >= 0; i -- ){
            // System.out.println( "i = " + i + "[" + x1 + ", " + y1 + "// " + x2 + ", " + y2 + "]");
            int dir = queries[ i ][ 0 ];
            int dist = queries[ i ][ 1 ];
            // System.out.println( "dir = " + dir + ", dist = " + dist );

            //y 감소
            if( dir == 0 ){
                y1 = y1 == 0 ? y1 : y1 + dist;
                y2 = y2 + dist >= m ? m - 1 : y2 + dist;
            }
            //y 증가

            else if( dir == 1){

                y1 = y1 - dist >= 0 ? y1 - dist: 0;
                y2 = y2 == m - 1 ? y2 : y2 - dist;

                // System.out.println("result = "+ y1 + "," + y2 );
            }
            //x 감소
            else if( dir == 2 ){
                x1 = x1 == 0 ? x1 : x1 + dist;
                x2 = x2 + dist >= n ? n - 1: x2 + dist;
            }
            //x 증가
            else{
                x1 = x1 - dist >= 0 ? x1 - dist : 0;
                x2 = x2 == n - 1 ? x2 : x2 - dist;
            }

            if( x1 >= n || y1 >= m || x2 < 0 || y2 < 0 ) return 0;
        }

        return ( x2 - x1 + 1 ) * ( y2 - y1 + 1 );
    }
}
