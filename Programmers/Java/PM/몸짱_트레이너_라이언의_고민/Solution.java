package PM.몸짱_트레이너_라이언의_고민;

import java.util.*;
class Solution {

    /*

        * 구하고자 하는 것 : 손님들간 거리중 최소 거리

        그렇다면 시간대 1320 * 1000 =? 1320000 -> 132만 테이블에서 가장 많이 겹치는 시간대를 추출해서 그 시간대에 사람간의 최소거리를
        구하자.

        2차원 그래프로 하면 시간 초과가 난다.
        근데 굳이 그럴 필요가 있었을까?
        단순 boolean도 되지 않나?
        또한 저장한 좌표들을 저장하는 ArrayList도 유지하자.


        ---> 시간 초과

        그럼 위에서 부터 찾는 방향으로 진행을 해야할 것 같다. -> 찾으면 끝.

        생각을 해보자

            1. 거리가 최대인 경우 m이 2개이고 두개가 각 대각선에 있을 때 -> 이 거리는? 2 * ( n - 1 )
            여기서 부터 사람을 채울 수 있는가 형식으로 진행을 해보자 -> n-queen의 흐름 처럼.

            실패 4.8 88.5

            2. 직전만 보면 안된다 그 전전이 더 가까울 수 있음.

            실패 (24.46ms, 99.3MB)

            3. 시작점이 0,0이 아닐 수도 있다.

            성공 통과 (51.91ms, 119MB)
    */

    int Mx = 0;
    Time[] times;
    int n;
    boolean graph[][];
    ArrayList< Point > lst = new ArrayList<>();
    public int solution(int n, int m, int[][] timetable) {
        int answer = 0;
        this.n = n;
        // 600 to 1320
        times = new Time[ 721 ];
        for( int i = 0; i < 721; i++ ){
            times[ i ] = new Time( i );
        }

        for( int[] time : timetable ){
            int start = time[ 0 ] - 600;
            int end = time[ 1 ] - 600;

            for( int i = start; i <= end; i ++ ){
                times[ i ].person++;
            }
        }

        Arrays.sort( times, ( t1, t2 ) -> {
            return Integer.compare( t2.person, t1.person );
        });

        if( times[ 0 ].person == 1 ){
            return 0;
        }

        if( times[ 0 ].person == ( ( n * n ) ) ){
            return 1;
        }

        for( int dist = 2 * ( n - 1 ); dist > 0; dist -- ){

            if( canBe( n, dist, times[ 0 ].person ) ){
                return dist;
            }
        }

        return 0;
    }

    public boolean canBe( int n, int dist, int people ){


        // ArrayList<Point> lst = new ArrayList<>();
        // // System.out.println("n = " + n + " dist = " + dist + " people = " + people );
        // lst.add( new Point( 0, 0 ) );
        // int cnt = 1;
        for( int sy = 0; sy < n; sy ++ ){
            ArrayList<Point> lst = new ArrayList<>();
            // System.out.println("n = " + n + " dist = " + dist + " people = " + people );
            lst.add( new Point( 0, sy ) );
            int cnt = 1;


            for( int x = 0; x < n; x ++ ){
                for( int y = 0; y < n; y ++ ){
                    boolean flag = true;


                    // if( getDist( lst.get( lst.size() -1 ), new Point( x, y ) ) >= dist ){
                    //     flag = true;
                    // }

                    for( Point p : lst ){
                        if( getDist( p, new Point( x, y ) ) < dist ){
                            flag = false;
                            break;
                        }
                    }

                    if( flag ){
                        cnt++;
                        if( cnt == people ) return true;

                        lst.add( new Point( x, y ) );
                    }
                }
            }
        }


        return false;



    }

//     public int solution(int n, int m, int[][] timetable) {
//         int answer = 0;
//         this.n = n;
//         // 600 to 1320
//         times = new Time[ 721 ];
//         for( int i = 0; i < 721; i++ ){
//             times[ i ] = new Time( i );
//         }

//         for( int[] time : timetable ){
//             int start = time[ 0 ] - 600;
//             int end = time[ 1 ] - 600;

//             for( int i = start; i <= end; i ++ ){
//                 times[ i ].person++;
//             }
//         }

//         Arrays.sort( times, ( t1, t2 ) -> {
//            return Integer.compare( t2.person, t1.person );
//         });

//         // System.out.println( times[ 0 ].time + "// " + times[ 0 ].person );

//         if( times[ 0 ].person == 1 ){
//             return 0;
//         }

//         if( times[ 0 ].person == ( ( n * n ) ) ){
//             return 1;
//         }

//         graph = new boolean[ n ][ n ];
//         lst = new ArrayList<>();
//         findMx( 0 );


//         return Mx;
//     }

    public void findMx( int depth ){


        if( depth == times[ 0 ].person ){
            Mx = Math.max( findMinDist(), Mx );
            return;
        }

        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < n; y ++ ){
                if( !graph[ x ][ y ] ){
                    if( lst.size() > 0 ){
                        if( getDist( lst.get( depth - 1 ), new Point( x, y ) ) < Mx ) continue;
                    }
                    Point p1 = new Point( x, y );
                    lst.add( p1 );
                    graph[ x ][ y ] = true;
                    findMx( depth + 1 );
                    lst.remove( p1 );
                    graph[ x ][ y ] = false;

                }
            }
        }

    }

    public int findMinDist(){
        // for( int x = 0; x < n; x ++ ){
        //     System.out.println( Arrays.toString( graph[ x ] ) );
        // }
        // System.out.println("--");


        int minValue = n * n;


        for( int i = 0; i < lst.size(); i ++ ){
            for( int j = i + 1; j < lst.size(); j ++ ){
                if( minValue < Mx ){ return -1; }
                // System.out.println( getDist( lst.get( i ), lst.get( j ) ) );
                minValue = Math.min( minValue, getDist( lst.get( i ), lst.get( j ) ) );
            }
        }

        return minValue;
    }

    public class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Point point = (Point) obj;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return 31 * x + y;
        }
    }

    public class Time{
        int time;
        int person;

        public Time( int time ){
            this.time = time;
            this.person = 0;
        }
    }

    public int getDist( Point p1, Point p2 ){
        return Math.abs( p1.x - p2.x ) + Math.abs( p1.y - p2.y );
    }

    public int getDist( int x1, int y1, int x2, int y2 ){
        return Math.abs( x2 - x1 ) + Math.abs( y2 - y1 );
    }
}